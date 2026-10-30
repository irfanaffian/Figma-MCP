#!/usr/bin/env python3
"""Ambil comment sebuah file Figma lewat REST API dan tampilkan per thread.

Pemakaian:
  python3 fetch_comments.py <link-figma | file_key> [--open | --pending] [--node 1:23] [--json] [--account NAMA]

Status thread: TERBUKA → SUDAH DIKERJAKAN (ada balasan berawalan ✅ atau reaksi ✅) → RESOLVED.

Mendukung beberapa akun Figma. Token dicari (tidak pernah dicetak):
  - env FIGMA_TOKEN (akun "utama") dan FIGMA_TOKEN_<NAMA> (akun lain) — sesi cloud
  - Keychain macOS: service "figma-token" (akun "utama") dan "figma-token-<nama>" — Mac
Tanpa --account, setiap token dicoba berurutan sampai ada yang punya akses ke file.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.figma.com/v1/files/{key}/comments?as_md=true"
PREFIX = "figma-token"


def keychain_secret(service):
    try:
        out = subprocess.run(["security", "find-generic-password", "-s", service, "-w"],
                             capture_output=True, text=True, check=True)
        return out.stdout.strip() or None
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def keychain_services():
    """Nama service figma-token* di Keychain (hanya atribut, tanpa membaca rahasia)."""
    try:
        out = subprocess.run(["security", "dump-keychain"], capture_output=True, text=True).stdout
    except FileNotFoundError:
        return []
    found = re.findall(r'"svce"<blob>="(%s(?:-[\w.-]+)?)"' % PREFIX, out)
    return sorted(set(found), key=lambda s: (s != PREFIX, s))


def get_tokens(account=None):
    """Daftar (nama_akun, token). Nama 'utama' = FIGMA_TOKEN / figma-token."""
    tokens = []
    for k, v in sorted(os.environ.items()):
        if v.strip() and (k == "FIGMA_TOKEN" or k.startswith("FIGMA_TOKEN_")):
            name = "utama" if k == "FIGMA_TOKEN" else k[len("FIGMA_TOKEN_"):].lower()
            tokens.append((name, v.strip()))
    if sys.platform == "darwin":
        for svc in keychain_services():
            name = "utama" if svc == PREFIX else svc[len(PREFIX) + 1:]
            if any(n == name for n, _ in tokens):
                continue
            secret = keychain_secret(svc)
            if secret:
                tokens.append((name, secret))
    tokens.sort(key=lambda t: t[0] != "utama")
    if account:
        tokens = [t for t in tokens if t[0] == account.lower()]
        if not tokens:
            sys.exit(f"ERROR: token untuk akun '{account}' tidak ditemukan "
                     f"(Keychain service '{PREFIX}-{account.lower()}' atau env FIGMA_TOKEN_{account.upper()}).")
    if not tokens and not account and sys.platform != "darwin":
        # Cloud dengan "Network secrets": proxy menyisipkan header X-Figma-Token sendiri.
        return [("cloud-secret", None)]
    if not tokens:
        sys.exit(
            "ERROR: token Figma tidak ditemukan.\n"
            "- Cloud: isi environment variable FIGMA_TOKEN (dan FIGMA_TOKEN_<NAMA> untuk akun lain).\n"
            "- Mac: security add-generic-password -a \"$USER\" -s figma-token -w\n"
            "       akun lain: ... -s figma-token-<nama> -w"
        )
    return tokens


def parse_target(target):
    """Kembalikan (file_key, node_id | None) dari link Figma atau file key."""
    if "figma.com" not in target:
        return target.strip(), None
    url = urllib.parse.urlparse(target)
    parts = [p for p in url.path.split("/") if p]
    key = None
    if "branch" in parts:
        key = parts[parts.index("branch") + 1]
    elif len(parts) >= 2 and parts[0] in ("design", "file", "board", "slides", "make", "proto"):
        key = parts[1]
    if not key:
        sys.exit(f"ERROR: tidak bisa membaca file key dari link: {target}")
    node = urllib.parse.parse_qs(url.query).get("node-id", [None])[0]
    if node:
        node = node.replace("-", ":")
    return key, node


class FetchError(Exception):
    def __init__(self, code, msg):
        super().__init__(msg)
        self.code = code


def fetch(key, token):
    req = urllib.request.Request(API.format(key=key), headers={"X-Figma-Token": token} if token else {})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        hints = {
            401: "token tidak valid / sudah dihapus — buat token baru (atau isi Network secrets di cloud)",
            403: "token salah/kedaluwarsa, tidak punya izin 'File comments: Read', atau akun tidak punya akses ke file ini",
            404: "file tidak ditemukan atau akun tidak punya akses — cek link/file key",
            429: "kena rate limit — tunggu sebentar lalu ulangi",
        }
        raw = e.read().decode(errors="replace")
        try:
            body = json.loads(raw)
            detail = body.get("err") or body.get("message") or raw
        except Exception:
            detail = raw
        detail = str(detail).strip()[:300]
        detail = f" | Pesan Figma: {detail}" if detail else ""
        raise FetchError(e.code, f"HTTP {e.code}: {hints.get(e.code, e.reason)}{detail}")
    except urllib.error.URLError as e:
        sys.exit(f"ERROR jaringan: {e.reason} (di cloud: pastikan api.figma.com diizinkan di Network access)")


def fetch_any(key, tokens):
    """Coba token satu per satu; kembalikan (nama_akun, data)."""
    errors = []
    for name, token in tokens:
        try:
            return name, fetch(key, token)
        except FetchError as e:
            errors.append(f"- akun '{name}': {e}")
            if e.code not in (403, 404):
                break
    sys.exit("ERROR: tidak ada akun yang bisa membaca comment file ini.\n" + "\n".join(errors))


def location(meta):
    """Ringkas client_meta: node_id bila comment ditempel ke frame, atau koordinat kanvas."""
    if not meta:
        return None, None
    if "node_id" in meta:
        off = meta.get("node_offset") or {}
        return meta["node_id"], f"offset ({off.get('x', 0):.0f}, {off.get('y', 0):.0f})"
    if "x" in meta and "y" in meta:
        return None, f"kanvas ({meta['x']:.0f}, {meta['y']:.0f})"
    return None, None


DONE_MARK = "✅"
DONE_EMOJI = {":white_check_mark:", ":heavy_check_mark:", "✅", "✔️"}


def status_of(c, replies):
    """resolved > dikerjakan (balasan berawalan ✅ atau reaksi ✅) > terbuka."""
    if c.get("resolved_at"):
        return "resolved", None
    for r in replies:
        if r["message"].strip().startswith(DONE_MARK):
            return "dikerjakan", r["message"].strip()
    if any(x.get("emoji") in DONE_EMOJI for x in (c.get("reactions") or [])):
        return "dikerjakan", "(reaksi ✅)"
    return "terbuka", None


def build_threads(comments):
    roots, replies = [], {}
    for c in comments:
        if c.get("parent_id"):
            replies.setdefault(c["parent_id"], []).append(c)
        else:
            roots.append(c)
    threads = []
    for c in sorted(roots, key=lambda c: c["created_at"]):
        node_id, where = location(c.get("client_meta"))
        rs = sorted(replies.get(c["id"], []), key=lambda r: r["created_at"])
        status, done_note = status_of(c, rs)
        threads.append({
            "id": c["id"],
            "order": c.get("order_id"),
            "author": c["user"]["handle"],
            "created_at": c["created_at"],
            "resolved_at": c.get("resolved_at"),
            "status": status,
            "done_note": done_note,
            "node_id": node_id,
            "where": where,
            "message": c["message"],
            "reactions": len(c.get("reactions") or []),
            "replies": [
                {"author": r["user"]["handle"], "created_at": r["created_at"], "message": r["message"]}
                for r in rs
            ],
        })
    return threads


def print_markdown(key, account, link_node, threads, counts):
    print(f"# Comment Figma — file {key}" + (f" (link menunjuk node {link_node})" if link_node else ""))
    print(f"Akun: {account}")
    print(f"{len(threads)} thread ditampilkan · total file: {counts['terbuka']} terbuka · "
          f"{counts['dikerjakan']} sudah dikerjakan (belum resolved) · {counts['resolved']} resolved\n")
    by_node = {}
    for t in threads:
        by_node.setdefault(t["node_id"] or "(tanpa frame — titik di kanvas)", []).append(t)
    for node, items in by_node.items():
        print(f"## Node {node}")
        for t in items:
            status = {"resolved": f"RESOLVED {(t['resolved_at'] or '')[:10]}",
                      "dikerjakan": "SUDAH DIKERJAKAN", "terbuka": "TERBUKA"}[t["status"]]
            num = f"#{t['order']} " if t["order"] else ""
            print(f"\n### {num}[{status}] {t['author']} · {t['created_at'][:16].replace('T', ' ')}")
            if t["where"]:
                print(f"_{t['where']}_  ·  id `{t['id']}`")
            print(t["message"].strip())
            for r in t["replies"]:
                print(f"  ↳ **{r['author']}** ({r['created_at'][:16].replace('T', ' ')}): {r['message'].strip()}")
        print()


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("target", help="link Figma atau file key")
    p.add_argument("--open", action="store_true", help="hanya thread yang belum resolved")
    p.add_argument("--pending", action="store_true",
                   help="hanya yang belum dikerjakan (bukan resolved, belum ada balasan/reaksi ✅)")
    p.add_argument("--node", help="hanya comment yang ditempel langsung ke node ini (mis. 1:23)")
    p.add_argument("--account", help="pakai token akun ini saja (mis. utama, app)")
    p.add_argument("--json", action="store_true", help="keluarkan JSON ringkas (untuk diolah lanjut)")
    a = p.parse_args()

    key, link_node = parse_target(a.target)
    account, data = fetch_any(key, get_tokens(a.account))
    threads = build_threads(data.get("comments", []))
    counts = {k: sum(1 for t in threads if t["status"] == k) for k in ("terbuka", "dikerjakan", "resolved")}

    node = a.node
    if a.open:
        threads = [t for t in threads if t["status"] != "resolved"]
    if a.pending:
        threads = [t for t in threads if t["status"] == "terbuka"]
    if node:
        # Hanya cocok langsung. Comment di dalam child frame perlu dicocokkan lewat Figma MCP (get_metadata).
        threads = [t for t in threads if t["node_id"] == node]

    if a.json:
        json.dump({"file_key": key, "account": account, "link_node_id": link_node, "node_filter": node, "counts": counts,
                   "threads": threads}, sys.stdout, ensure_ascii=False, indent=2)
        print()
    else:
        print_markdown(key, account, link_node, threads, counts)


if __name__ == "__main__":
    main()
