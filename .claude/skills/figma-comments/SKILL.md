---
name: figma-comments
description: Baca semua comment di file Figma (isi, pengirim, balasan, status resolved) lewat Figma REST API, lalu cocokkan ke frame/layer lewat Figma MCP. Use when the user says "cek komen", "cek comment", "baca komen", "ada feedback apa", "komen klien", "revisi dari comment", or shares a figma.com link and asks about comments/feedback. Figma MCP sendiri tidak bisa membaca comment — skill ini yang menjembatani.
---

# Cek comment Figma

Figma MCP tidak punya tool untuk comment, jadi comment diambil lewat REST API (`GET /v1/files/<file_key>/comments`) dengan script `scripts/fetch_comments.py`, lalu lokasi tiap comment dicocokkan ke frame dengan Figma MCP.

## Token (jangan pernah ditampilkan)

Script mencari token sendiri, berurutan:

1. env `FIGMA_TOKEN` — sesi cloud claude.ai/code (diisi pengguna di pengaturan environment).
2. Keychain macOS service `figma-token` — Mac mini / MacBook.

Aturan:
- **Jangan** `echo`, `cat`, `printenv`, atau mencetak token dalam bentuk apa pun; jangan menaruhnya di argumen command, file, commit, atau chat.
- Repo ini **public** — jangan menyimpan token, data klien sensitif, atau isi comment mentah ke repo kecuali pengguna meminta (ringkasan revisi di `status.md` boleh).
- Bila token tidak ada, script berhenti dengan pesan cara mengisinya. Sampaikan langkahnya ke pengguna; jangan minta token ditempel di chat.

Izin token yang cukup: **File comments: Read** (opsional *File content: Read* tidak diperlukan untuk skill ini).

## Langkah

1. **Ambil comment** (dari root repo):
   ```bash
   python3 .claude/skills/figma-comments/scripts/fetch_comments.py "<link-figma>" --json
   ```
   - `--open` → hanya yang belum resolved (pakai bila pengguna bilang "yang belum dikerjakan" / "yang masih open").
   - `--node 12:345` → hanya comment yang ditempel *langsung* ke node itu.
   - Tanpa `--json` → markdown siap baca, dikelompokkan per node.
   - Link branch (`/design/<key>/branch/<branchKey>/…`) otomatis memakai branch key.

2. **Cocokkan ke frame** (bila ada `node_id`):
   - `create_session` untuk file key tersebut, lalu `get_metadata` pada halaman/frame yang relevan untuk mendapatkan nama layer dan induknya.
   - Bila link pengguna menunjuk node tertentu (`link_node_id`), anggap comment relevan bila `node_id`-nya node itu **atau turunannya** (cek lewat metadata), bukan hanya yang sama persis.
   - Comment tanpa `node_id` hanya punya koordinat kanvas — sebut "titik di kanvas (x, y)" dan, bila perlu, cari frame yang membungkus koordinat itu dari metadata.
   - Ambil `get_screenshot` hanya bila pengguna minta atau comment-nya ambigu.

3. **Laporkan ke pengguna** dalam bahasa sederhana, urut dari yang terbuka:

   | # | Status | Frame / layer | Dari | Isi comment | Balasan |
   | --- | --- | --- | --- | --- | --- |

   Lalu ringkas: berapa terbuka vs resolved, dan daftar tindakan revisi yang tersirat (misal "perbesar tombol CTA di Hero"). Jangan langsung mengubah desain — tanyakan dulu, kecuali pengguna sudah meminta "kerjakan revisinya". Bila diminta mengerjakan, muat skill `figma-use` sebelum `use_figma`.

4. **Catat (opsional)**: bila comment terkait proyek di repo (Axios, True Health, …) dan pengguna setuju, tambahkan ringkasan revisi ke `<Proyek>/status.md` tanpa token atau data pribadi.

## Bila gagal

| Pesan | Artinya / tindakan |
| --- | --- |
| `token Figma tidak ditemukan` | Cloud: isi `FIGMA_TOKEN` di pengaturan environment. Mac: `security add-generic-password -a "$USER" -s figma-token -w` (token diketik, tidak tampil) |
| `HTTP 403` | Token salah/kedaluwarsa, izin *File comments: Read* belum dicentang, atau akun pemilik token tidak punya akses ke file |
| `HTTP 404` | File key salah — cek link |
| `HTTP 429` | Rate limit — tunggu sebentar |
| `ERROR jaringan` / `CONNECT tunnel failed 403` (cloud) | Network access environment memblokir `api.figma.com` — pengguna perlu menambahkannya di Allowed domains |
| `python3` tidak ada (Mac tanpa Command Line Tools) | Jalankan `xcode-select --install`, atau sementara ambil JSON dengan `curl -s -H "X-Figma-Token: $(security find-generic-password -s figma-token -w)" "https://api.figma.com/v1/files/<key>/comments" > /tmp/figma-comments.json` lalu baca file-nya |
