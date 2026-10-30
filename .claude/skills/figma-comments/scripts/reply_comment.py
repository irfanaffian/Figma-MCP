#!/usr/bin/env python3
"""Balas sebuah comment Figma, opsional menandainya "sudah dikerjakan".

Pemakaian:
  python3 reply_comment.py <link-figma | file_key> <#nomor | comment_id> "pesan" [--done] [--dry-run] [--account NAMA]

--done     awali balasan dengan "✅ " dan beri reaksi ✅ di comment utama,
           sehingga fetch_comments.py menampilkannya sebagai SUDAH DIKERJAKAN.
--dry-run  tampilkan apa yang akan dikirim tanpa mengirim.

Butuh token dengan izin file_comments:write (selain file_comments:read).
Figma API tidak bisa me-resolve comment; resolve tetap dilakukan manual di Figma.
"""
import argparse
import json
import sys
import urllib.error
import urllib.request

from fetch_comments import DONE_MARK, fetch_any, get_tokens, parse_target

BASE = "https://api.figma.com/v1/files/{key}/comments"


def post(url, token, body):
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(), method="POST",
        headers={"X-Figma-Token": token, "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read().decode(errors="replace")
            try:
                return json.loads(raw) if raw.strip() else {}
            except ValueError:
                return {}
    except urllib.error.HTTPError as e:
        raw = e.read().decode(errors="replace")
        try:
            body = json.loads(raw)
            detail = body.get("err") or body.get("message") or raw
        except Exception:
            detail = raw
        hint = " (token perlu izin file_comments:write)" if e.code == 403 else ""
        sys.exit(f"ERROR HTTP {e.code}{hint} | Pesan Figma: {str(detail).strip()[:300]}")
    except urllib.error.URLError as e:
        sys.exit(f"ERROR jaringan: {e.reason}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("target", help="link Figma atau file key")
    p.add_argument("comment", help="nomor comment (#13 atau 13) atau comment id")
    p.add_argument("message", help="isi balasan")
    p.add_argument("--done", action="store_true", help="tandai sudah dikerjakan (✅ + reaksi)")
    p.add_argument("--dry-run", action="store_true", help="jangan kirim, hanya tampilkan")
    p.add_argument("--account", help="pakai token akun ini saja")
    a = p.parse_args()

    key, _ = parse_target(a.target)
    tokens = get_tokens(a.account)
    account, data = fetch_any(key, tokens)
    token = dict(tokens)[account]

    roots = [c for c in data.get("comments", []) if not c.get("parent_id")]
    ref = a.comment.lstrip("#")
    match = [c for c in roots if c["id"] == ref] or [c for c in roots if str(c.get("order_id")) == ref]
    if not match:
        sys.exit(f"ERROR: comment '{a.comment}' tidak ditemukan di file ini.")
    c = match[0]

    message = a.message.strip()
    if a.done and not message.startswith(DONE_MARK):
        message = f"{DONE_MARK} {message}"

    print(f"File {key} · akun {account}")
    print(f"Comment #{c.get('order_id')} ({c['user']['handle']}): {c['message'].strip()[:200]}")
    print(f"Balasan: {message}" + ("  + reaksi ✅" if a.done else ""))
    if a.dry_run:
        print("(dry-run: tidak dikirim)")
        return

    res = post(BASE.format(key=key), token, {"message": message, "comment_id": c["id"]})
    print(f"Terkirim · id balasan {res.get('id')}")
    if a.done:
        post(f"{BASE.format(key=key)}/{c['id']}/reactions", token, {"emoji": ":white_check_mark:"})
        print("Reaksi ✅ ditambahkan")


if __name__ == "__main__":
    main()
