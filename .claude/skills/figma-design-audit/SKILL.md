---
name: figma-design-audit
description: Audit a Figma page/frame for visual consistency and fix it in place via the Figma MCP — fonts, text styles, colors, buttons, icon stroke weights, text overflow, section spacing. Use when the user asks to "audit", "cek konsistensi", "rapikan", "samakan style", "simplekan yang mirip", or check a design "detail" before handoff. Works on any project in this repo (Axios, True Health, …).
---

# Figma design audit

Audit lalu rapikan satu frame halaman (misalnya `Desktop - 11`) supaya elemen dengan fungsi sama memakai gaya yang sama. Semua perubahan dilakukan langsung di Figma lewat `use_figma`; tidak membuat komponen atau style baru kecuali pengguna meminta.

## Sebelum mulai

1. Baca `<Proyek>/brief.md` dan `<Proyek>/status.md` — di sana ada patokan (skala tipografi, warna, jarak) dan pengecualian yang sudah disepakati pengguna. Pengecualian **tidak boleh** "diseragamkan" ulang.
2. `create_session` untuk file Figma, lalu baca kondisi terbaru frame (pengguna sering mengedit manual).
3. Muat skill `figma-use` (wajib sebelum `use_figma`).

## Langkah audit (baca dulu, jangan langsung ubah)

Jalankan `scripts/inventory.js` (ganti `PAGE_ID` dan `FRAME_ID`). Skrip itu mengembalikan:

| Cek | Yang dicari |
| --- | --- |
| Keluarga font | Ikuti brief proyek (Axios: hanya Plus Jakarta Sans). Font lain = ganti ke font proyek dengan ketebalan sama; teks display lebar tetap (wordmark) perlu diukur ulang agar tidak turun baris |
| Gaya teks unik | Kombinasi family/style/size/line-height/tracking; kelompokkan per peran |
| Warna teks & non-teks | Variasi hitam/abu yang hampir sama (`#262623`, `#282723`, `#000000`, `#111111` vs token) |
| Ukuran ganjil | 15/17 px dsb. — hampir selalu salah ketik |
| Line-height | Body campur 125/135/145/150% untuk fungsi sama |
| Tombol | Kelompokkan tinggi/radius/gap/padding/fill/label — harus jadi beberapa varian jelas |
| Ikon | Stroke Phosphor Regular = `ukuran × 16/256` |
| Overflow | Teks keluar dari frame yang fixed/clip |
| Sambungan section | Celah/tumpukan antar section (harus 0 bila sistemnya section menempel) dan tinggi non-kelipatan 4 |

Laporkan temuan ke pengguna dalam bahasa sederhana (angka sebelum → sesudah), lalu perbaiki.

## Aturan perbaikan

- **Petakan ke token**, jangan menciptakan nilai baru: gelap → token gelap, abu → token abu, teks pudar → token abu dengan opasitas.
- **Satu peran = satu gaya**: nama produk, body, eyebrow, label tombol, dst. Ikuti tabel skala tipografi di `brief.md` proyek.
- **Jangan sentuh**: gaya display khusus (wordmark besar, angka statistik), shape mask, overlay/tint yang disengaja, dan semua pengecualian yang tercatat di brief/status.
- **Ganti font**: segment dengan `setRangeFontName`; muat font *lama dan baru* sebelum mengubah.
- **Setelah mengubah teks**, cek ulang overflow — line-height lebih besar bisa membuat teks meluap dari frame fixed. Perbaiki dengan `textAutoResize='HEIGHT'` + `FILL`, atau ubah frame jadi hug.
- **Kolom sejajar**: bila judul di grid kolom tidak sejajar karena isi rata bawah, ubah ke rata atas dengan jarak tetap.
- **Section menempel**: susun ulang `y` setiap section = akhir section sebelumnya; ubah tinggi frame halaman.
- **Wordmark / teks display lebar tetap**: setelah ganti font, ukur lebar alami lewat *clone sementara di luar auto-layout* (`textAutoResize='WIDTH_AND_HEIGHT'`), lalu skala `fontSize = size × lebarTarget / lebarAlami`. Mengukur langsung di dalam frame FILL tidak berhasil.
- **Paint tersembunyi**: bandingkan juga `visible` pada setiap fill/stroke. Outline yang disembunyikan pengguna (`visible:false`) adalah patokan — jangan dihidupkan lagi, dan samakan elemen saudaranya.
- **Edit manual pengguna = patokan**: bila satu elemen sudah diubah pengguna dan diminta "terapkan ke yang lain", salin *semua* properti (ukuran, posisi anak, visibilitas paint), bukan hanya warna/ukuran.
- **Varian hasil clone**: section/kartu yang di-clone dari versi lama membawa warna dan gaya lama. Setelah pengguna memasang varian ke halaman, jalankan audit lagi — biasanya ada sisa token lama (contoh: `#282723` di tombol).
- **Treatment vs konten**: bila pengguna minta "treatment seperti X", salin gaya/struktur visual X tetapi **pertahankan konten asli** elemen tujuan (harga, tombol, teks) kecuali diminta lain.
- **Bila pengguna minta "kembalikan"**: pastikan dulu bagian mana (gaya teks atau seluruh treatment). Kembalikan hanya yang diminta, lalu catat pengecualian itu di brief agar audit berikutnya tidak menyeragamkannya lagi.
- Kembalikan semua node ID yang diubah; ambil satu screenshot per area yang berubah besar.

## Setelah selesai

1. Jalankan inventory sekali lagi — laporkan sisa temuan dan alasannya bila dibiarkan.
2. Catat hasil di `<Proyek>/status.md` (ringkas, dengan angka) dan perbarui tabel skala tipografi/patokan di `brief.md` bila berubah.
3. Commit + push ke `main`.

## Hasil nyata (Axios, 30–31 Oktober 2026)

- Audit pertama: 82 → 43 gaya teks, 3 → 2 keluarga font, 9 varian warna → 3 token, 2 overflow, 2 sambungan section meleset.
- Audit kedua: 41 gaya, 30 warna non-teks dirapikan (`#111111`, `#000000` 12%), tracking marquee diseragamkan.
- Pengguna lalu meminta **1 font saja**: 11 teks Inter Display (label tombol, logo, wordmark) → Plus Jakarta Sans; wordmark footer 619 → 590 px agar tetap satu baris.
- Audit ketiga (31 Oktober): bersih kecuali 1 sisa warna lama dari varian yang di-clone.
