# Brief Axios

Ringkasan arahan dan aturan dari sesi kerja sebelumnya. Instruksi pengguna terbaru dan kondisi Figma terkini menjadi acuan utama saat revisi.

## Lingkup

Retouch dan redesign visual landing page desktop Axios (lebar frame 1512 px), dari header sampai footer. Hasilnya dipakai sebagai template Shopify untuk klien Siddhesh.

## Karakter brand

- Tema: hangat, personal, tenang. Skincare sebagai jeda, bukan proyek.
- Copy pendek dan lembut, misalnya "Less rush. More ritual.", "Your skin. Your rhythm.".
- Fotografi close-up kulit, tekstur produk, dan momen perawatan sehari-hari.

## Aturan kerja

- Hanya layer yang bisa diedit. Jangan membuat komponen atau style baru.
- Pertahankan section yang tidak diminta untuk diubah.
- Selalu baca kondisi Figma terbaru sebelum mengedit, karena pengguna juga mengedit manual.
- Jangan menulis klaim tanpa data, misalnya "Verified buyer", "Free shipping", "Dermatologist tested", atau klaim klinis lainnya.

## Patokan visual

| Aspek | Patokan |
| --- | --- |
| Grid spacing | Kelipatan 4 px; micro spacing di dalam pill boleh angka genap (6, 10) |
| Antar section | Section menempel; padding atas/bawah tiap section 80 px (lihat Sistem jarak section) |
| Judul ke konten | 64 px |
| Eyebrow ke judul | 20 px |
| Warna teks | Gelap `#21211F`, abu `#807A73` |
| Headline | 64 px Medium, line-height 115%, letter-spacing -1% (hero 80 px uppercase) |
| Eyebrow | 12 px SemiBold, line-height 150%, letter-spacing 9%, #807A73, bernomor urut halaman (01 hero … 08 CTA) |
| Teks pendukung heading | 18 px Medium, #21211F, letter-spacing -1% |
| Body | 18 / 16 / 14 px, line-height 150% |
| Tombol | Pill, label Plus Jakarta Sans Medium 16 px (line-height 125%), ikon di lingkaran trailing, jarak 12 px, padding 8/8/8/20 |
| Radius dan gap | Mengikuti patokan Desktop - 9 (radius 8 px, gap 8 px), bukan Desktop - 7 |
| Ikon | Phosphor Icons Regular sebagai vector stroke; stroke-width = 16/256 dari ukuran ikon |

## Skala tipografi (hasil audit 30 Oktober 2026)

Hanya **1 keluarga font: Plus Jakarta Sans** untuk semua teks, termasuk label tombol, logo, dan wordmark footer (Inter Display dan IBM Plex Mono tidak dipakai lagi).

| Peran | Gaya |
| --- | --- |
| Headline section | 64 Medium, 115%, -1% (italic untuk aksen kata) |
| Statement besar (brand intro, philosophy) | 48 Medium, 72 px, -4% |
| Judul kartu besar / kutipan | 44 Medium, 125%, -2% |
| Judul di atas foto | 32 Medium/SemiBold, 125%, -1% |
| Judul kecil kartu | 24 Medium, 125% |
| Nama produk / judul item | 20 Medium, 130%, -1% |
| Teks pendukung & label 18 | 18 Medium, 150%, -1% |
| Body 18 / 16 / 14 / 12 | Regular, 150%, 0% |
| Ribbon | 18 SemiBold, 28 px, -2%, uppercase |
| Eyebrow / label kecil | 12 SemiBold, 150%, 9% |
| Label tombol | Plus Jakarta Sans Medium 16 (tombol 48 px) atau 18 (tombol 56 px), 125% |
| Wordmark footer | Plus Jakarta Sans Medium 590 px, 80%, -4% (pas satu baris selebar 1432 px) |

Warna teks hanya `#21211F` (gelap), `#807A73` (abu; 60% untuk teks pudar), dan putih (dengan opasitas di atas foto).

## Sistem jarak section (versi pengguna)

Section menempel satu sama lain (tanpa jarak antar frame); jarak visual berasal dari padding section **80 px atas/bawah** (Stories 64 px, ribbon 0).

## Treatment garis dan penanda

Garis tipis dengan penanda kotak hanya dipakai di **hero** dan **banner foto**. Penanda berupa **satu kotak putih 8×8 px** tepat di titik pertemuan garis (feedback Sid, 29 Oktober 2026; sebelumnya dua kotak 6 px).

Kotak penanda yang sama juga dipakai di **kartu ritual Three simple steps** (titik pertemuan garis atas footer dan pembagi vertikal ml) di footer video unggulan Shoppable videos, dan di pita konten banner foto, atas permintaan pengguna 30 Oktober 2026.

Pengecualian atas permintaan pengguna: **Closing CTA** memakai garis tipis tanpa grid marker (garis atas, bawah, dan pembagi vertikal), mengikuti referensi yang dilampirkan pengguna. Jangan diterapkan ke section lain tanpa instruksi.

## Struktur halaman (Desktop - 11)

0. Announcement bar 48 px gelap dengan countdown (Days/Hrs/Min/Sec), link "Shop the set", dan panah kiri/kanan di ujung (pengumuman bisa digeser).
1. Header: logo, menu Shop / Rituals / Our story / Journal, currency switcher (USD $, pill glass), ikon akun, keranjang, cari, tombol.
2. Hero: foto penuh, bingkai garis dengan grid marker, label kiri dan kanan, intro, avatar, headline uppercase, tombol.
3. Ribbon review pertama.
4. Stories: 6 lingkaran story (Cleanse, Hydrate, Comfort bercincin terakota = baru; Routines, Textures, Community bercincin abu = sudah dilihat).
5. Brand introduction dengan foto inline.
6. Ribbon "Daily care, simplified" dengan thumbnail foto.
7. Shop — Your daily essentials: kategori dan 4 kartu produk.
8. Collections — Shop by category: judul rata kiri + prev/next, 5 kartu kategori 320×400 (kartu kelima terpotong sebagai petunjuk carousel).
9. Cloud Comfort — slider (foto + catatan langkah, titik indikator, prev/next), lalu "Moments of care" 4 kolom.
10. Three simple steps — kartu produk ritual.
11. Shoppable videos — "Rituals in motion.": judul di atas; video aktif besar di kiri (856×600); kolom kanan: intro + prev/next di atas, label "UP NEXT" + 2 video antrean square 268×268 di bawah; video unggulan memakai treatment Variant B (pill glass, judul + garis bertanda) dengan konten asli: deskripsi, harga $24 USD, tombol Add to bag; video antrean memakai kartu produk putih mengambang (foto kecil, nama, harga, tombol +).
12. Ribbon review kedua.
13. Section "Skincare should feel like a pause" dengan foto asimetris.
14. Banner foto dengan bingkai garis; konten di pita bergaya kartu ritual (pesan | countdown | tombol) yang menempel di garis bawah.
15. Before & after — 3 kartu 560 px dengan toggle Before/After, disclaimer "Individual results vary."
16. Community — Small rituals, real stories.
17. Closing CTA dan footer.
