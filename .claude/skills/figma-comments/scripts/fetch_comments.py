#!/usr/bin/env python3
"""Ambil comment sebuah file Figma lewat REST API dan tampilkan per thread.

Pemakaian:
  python3 fetch_comments.py <link-figma | file_key> [--open] [--node 1:23] [--json]

Token dicari berurutan (tidak pernah dicetak):
  1. env FIGMA_TOKEN            (sesi cloud claude.ai/code)
  2. Keychain macOS, service "figma-token"  (Mac mini / MacBook)
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


def get_token():
    token = os.environ.get("FIGMA_TOKEN", "").strip()
    if token:
        return token
    if sys.platform == "darwin":
        try:
            out = subprocess.run(
                ["security", "find-generic-password", "-s", "figma-token", "-w"],
                capture_output=True, text=True, check=True,
            )
            if out.stdout.strip():
                return out.stdout.strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
    sys.exit(
        "ERROR: token Figma tidak ditemukan.\n"
        "- Cloud: isi environment variable FIGMA_TOKEN di pengaturan environment.\n"
        "- Mac: security add-generic-password -a \"$USER\" -s figma-token -w"
    )


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


def fetch(key, token):
    req = urllib.request.Request(API.format(key=key), headers={"X-Figma-Token": token})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        hints = {
            403: "token salah/kedaluwarsa, tidak punya izin 'File comments: Read', atau akun tidak punya akses ke file ini",
            404: "file tidak ditemukan — cek link/file key",
            429: "kena rate limit — tunggu sebentar lalu ulangi",
        }
        raw = e.read().decode(errors="replace")
        try:
            body = json.loads(raw)
            detail = body.get("err") or body.get("message") or raw
        except Exception:
            detail = raw
        detail = str(detail).strip()[:300]
        detail = f"\nPesan Figma: {detail}" if detail else ""
        sys.exit(f"ERROR HTTP {e.code}: {hints.get(e.code, e.reason)}{detail}")
    except urllib.error.URLError as e:
        sys.exit(f"ERROR jaringan: {e.reason} (di cloud: pastikan api.figma.com diizinkan di Network access)")


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
        threads.append({
            "id": c["id"],
            "order": c.get("order_id"),
            "author": c["user"]["handle"],
            "created_at": c["created_at"],
            "resolved_at": c.get("resolved_at"),
            "node_id": node_id,
            "where": where,
            "message": c["message"],
            "reactions": len(c.get("reactions") or []),
            "replies": [
                {"author": r["user"]["handle"], "created_at": r["created_at"], "message": r["message"]}
                for r in sorted(replies.get(c["id"], []), key=lambda r: r["created_at"])
            ],
        })
    return threads


def print_markdown(key, link_node, threads, total_open, total_resolved):
    print(f"# Comment Figma — file {key}" + (f" (link menunjuk node {link_node})" if link_node else ""))
    print(f"{len(threads)} thread ditampilkan · {total_open} terbuka · {total_resolved} resolved (total file)\n")
    by_node = {}
    for t in threads:
        by_node.setdefault(t["node_id"] or "(tanpa frame — titik di kanvas)", []).append(t)
    for node, items in by_node.items():
        print(f"## Node {node}")
        for t in items:
            status = f"RESOLVED {t['resolved_at'][:10]}" if t["resolved_at"] else "TERBUKA"
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
    p.add_argument("--node", help="hanya comment yang ditempel langsung ke node ini (mis. 1:23)")
    p.add_argument("--json", action="store_true", help="keluarkan JSON ringkas (untuk diolah lanjut)")
    a = p.parse_args()

    key, link_node = parse_target(a.target)
    data = fetch(key, get_token())
    threads = build_threads(data.get("comments", []))
    total_open = sum(1 for t in threads if not t["resolved_at"])
    total_resolved = len(threads) - total_open

    node = a.node
    if a.open:
        threads = [t for t in threads if not t["resolved_at"]]
    if node:
        # Hanya cocok langsung. Comment di dalam child frame perlu dicocokkan lewat Figma MCP (get_metadata).
        threads = [t for t in threads if t["node_id"] == node]

    if a.json:
        json.dump({"file_key": key, "link_node_id": link_node, "node_filter": node, "open": total_open,
                   "resolved": total_resolved, "threads": threads}, sys.stdout, ensure_ascii=False, indent=2)
        print()
    else:
        print_markdown(key, link_node, threads, total_open, total_resolved)


if __name__ == "__main__":
    main()
