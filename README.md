# Figma-MCP

Repository untuk konteks dan dokumentasi proyek desain yang dikerjakan melalui MCP Figma.

## Proyek

| Proyek | Fokus | Status |
| --- | --- | --- |
| [Axios](./Axios/) | Redesign visual landing page desktop (template Shopify) | Menunggu instruksi berikutnya; frame aktif Desktop - 11 |
| [Helge Heupel](./HelgeHeupel/) | Homepage + prototype, revisi art direction klien (W01–W28) | Revisi v1 sedang dikerjakan |
| [True Health](./TrueHealth/) | Creative refresh visual homepage desktop | Menunggu instruksi revisi; tiga frame desain dapat diakses di Figma |

## Struktur

Setiap proyek memiliki folder sendiri dengan README, brief, status, dan riwayat yang relevan. Folder proyek mengikuti riwayat Git repository utama; tidak menggunakan nested Git repository atau submodule.

Desain editable tetap berada di Figma. Penyimpanan konteks di GitHub tidak otomatis menyimpan file Figma, mengaktifkan koneksi MCP, atau memindahkan chat. Kode implementasi dan ekspor aset hanya ditambahkan ketika benar-benar tersedia.

## Skill

| Skill | Fungsi |
| --- | --- |
| [figma-design-audit](./.claude/skills/figma-design-audit/SKILL.md) | Audit dan rapikan konsistensi desain Figma (font, warna, tombol, ikon, overflow, jarak section) untuk proyek mana pun di repo ini |
| [figma-comments](./.claude/skills/figma-comments/SKILL.md) | Baca semua comment file Figma (isi, pengirim, balasan, resolved) lewat Figma REST API dan cocokkan ke frame. Butuh token Figma: env `FIGMA_TOKEN` (cloud) atau Keychain `figma-token` (Mac). Token tidak pernah disimpan di repo |

Skill di `.claude/skills/` otomatis tersedia di setiap sesi Claude Code yang memakai repo ini.
