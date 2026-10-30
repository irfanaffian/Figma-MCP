---
name: figma-comments
description: Baca, balas, dan lacak status comment di file Figma (isi, pengirim, balasan, terbuka / sudah dikerjakan / resolved) lewat Figma REST API, lalu cocokkan ke frame/layer lewat Figma MCP. Use when the user says "cek komen", "cek comment", "baca komen", "balas komen", "reply comment", "komen mana yang belum dikerjakan", "tandai sudah dikerjakan", "ada feedback apa", "komen klien", "revisi dari comment", or shares a figma.com link and asks about comments/feedback. Figma MCP sendiri tidak bisa membaca comment — skill ini yang menjembatani.
---

# Cek, balas & lacak comment Figma

Figma MCP tidak punya tool untuk comment, jadi comment diambil lewat REST API (`GET /v1/files/<file_key>/comments`) dengan script `scripts/fetch_comments.py`, lalu lokasi tiap comment dicocokkan ke frame dengan Figma MCP.

## Token (jangan pernah ditampilkan)

Pengguna punya **lebih dari satu akun Figma** (akun di browser ≠ akun di aplikasi Figma). Satu token = satu akun, dan hanya bisa membaca file yang bisa dibuka akun itu. Script mencari semua token:

| Akun | Mac (Keychain service) | Cloud (env) |
| --- | --- | --- |
| `utama` | `figma-token` | `FIGMA_TOKEN` |
| akun lain, mis. `app` | `figma-token-app` | `FIGMA_TOKEN_APP` |

Tanpa `--account`, token dicoba berurutan (utama dulu) sampai ada yang punya akses; hasil menyebut akun mana yang berhasil (`Akun: …` / `"account"`). Pakai `--account app` bila pengguna menyebut akun tertentu.

Menambah akun baru di Mac (token diketik saat diminta, tidak tampil):
```bash
security add-generic-password -a "$USER" -s figma-token-<nama> -w
```
Menimpa token yang kedaluwarsa: tambahkan `-U`.

Aturan:
- **Jangan** `echo`, `cat`, `printenv`, atau mencetak token dalam bentuk apa pun; jangan menaruhnya di argumen command, file, commit, atau chat.
- Repo ini **public** — jangan menyimpan token, data klien sensitif, atau isi comment mentah ke repo kecuali pengguna meminta (ringkasan revisi di `status.md` boleh).
- Bila token tidak ada, script berhenti dengan pesan cara mengisinya. Sampaikan langkahnya ke pengguna; jangan minta token ditempel di chat.

Izin token: **`file_comments:read`** untuk membaca; tambah **`file_comments:write`** untuk membalas/menandai. Token lama yang hanya read akan gagal 403 saat membalas — minta pengguna membuat token baru dengan kedua izin lalu menimpanya (`-U`).

## Status "sudah dikerjakan"

Figma API **tidak bisa me-resolve** comment. Jadi status dilacak sendiri:

| Status | Artinya |
| --- | --- |
| `terbuka` | belum ada tanda apa pun |
| `dikerjakan` | ada balasan berawalan **✅** atau reaksi ✅ di comment utama (dibuat lewat `reply_comment.py --done`, atau manual di Figma) |
| `resolved` | sudah di-resolve manual di Figma |

`fetch_comments.py --pending` → hanya yang `terbuka` (jawaban untuk "mana yang belum dikerjakan?").

## Langkah

1. **Ambil comment** (dari root repo):
   ```bash
   python3 .claude/skills/figma-comments/scripts/fetch_comments.py "<link-figma>" --json
   ```
   - `--pending` → hanya yang belum dikerjakan (pakai bila pengguna bilang "yang belum dikerjakan").
   - `--open` → semua yang belum resolved (termasuk yang sudah dikerjakan tapi belum di-resolve).
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

4. **Balas / tandai selesai** — setelah revisi dikerjakan, atau bila pengguna minta membalas:
   ```bash
   # cek dulu tanpa mengirim
   python3 .claude/skills/figma-comments/scripts/reply_comment.py "<link>" "#13" "Sudah diganti jadi Axios Joss" --done --dry-run
   # kirim
   python3 .claude/skills/figma-comments/scripts/reply_comment.py "<link>" "#13" "Sudah diganti jadi Axios Joss" --done
   ```
   - `#13` = nomor comment di Figma (atau comment id). `--done` menambah awalan ✅ + reaksi ✅.
   - Balasan **terlihat oleh semua orang di file** (termasuk klien) dan atas nama pemilik token. Tampilkan dulu draf balasannya ke pengguna dan kirim **hanya setelah disetujui**, kecuali pengguna sudah eksplisit bilang "balas langsung".
   - Tulis balasan singkat, dalam bahasa yang dipakai di comment, menyebut apa yang diubah (sebelum → sesudah).
   - Ingatkan pengguna bahwa resolve tetap manual di Figma.

5. **Catat (opsional)**: bila comment terkait proyek di repo (Axios, True Health, …) dan pengguna setuju, tambahkan ringkasan revisi ke `<Proyek>/status.md` tanpa token atau data pribadi.

## Bila gagal

| Pesan | Artinya / tindakan |
| --- | --- |
| `token Figma tidak ditemukan` | Cloud: isi `FIGMA_TOKEN` di pengaturan environment. Mac: `security add-generic-password -a "$USER" -s figma-token -w` (token diketik, tidak tampil) |
| `HTTP 403` | Token salah/kedaluwarsa, izin *File comments: Read* belum dicentang, atau akun pemilik token tidak punya akses ke file |
| `Invalid scope: ["current_user:read"]` | Token dibuat dengan centang yang salah. Buat ulang dengan `file_comments:read` (bagian **Files**), lalu timpa: `security add-generic-password -U -a "$USER" -s figma-token -w` |
| `tidak ada akun yang bisa membaca comment file ini` | File hanya bisa dibuka akun Figma lain — tambahkan token akun itu (`figma-token-<nama>`) |
| `reply_comment.py` → `HTTP 403 (token perlu izin file_comments:write)` | Buat token baru dengan `file_comments:read` **dan** `file_comments:write`, timpa dengan `-U` |
| `HTTP 404` | File key salah — cek link |
| `HTTP 429` | Rate limit — tunggu sebentar |
| `ERROR jaringan` / `CONNECT tunnel failed 403` (cloud) | Network access environment memblokir `api.figma.com` — pengguna perlu menambahkannya di Allowed domains |
| `python3` tidak ada (Mac tanpa Command Line Tools) | Jalankan `xcode-select --install`, atau sementara ambil JSON dengan `curl -s -H "X-Figma-Token: $(security find-generic-password -s figma-token -w)" "https://api.figma.com/v1/files/<key>/comments" > /tmp/figma-comments.json` lalu baca file-nya |
