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
| Antar section | 120 px |
| Judul ke konten | 64 px |
| Eyebrow ke judul | 20 px |
| Warna teks | Gelap `#21211F`, abu `#807A73` |
| Headline | 64 px, line-height 115% (hero 80 px uppercase) |
| Body | 18 / 16 / 14 px, line-height 150% |
| Tombol | Pill, jarak label ke ikon 12 px, line-height 125% |
| Radius dan gap | Mengikuti patokan Desktop - 9 (radius 8 px, gap 8 px), bukan Desktop - 7 |
| Ikon | Phosphor Icons Regular sebagai vector stroke; stroke-width = 16/256 dari ukuran ikon |

## Treatment garis dan penanda

Garis tipis dengan penanda kotak hanya dipakai di **hero** dan **banner foto**. Penanda berupa **satu kotak putih 8×8 px** tepat di titik pertemuan garis (feedback Sid, 29 Oktober 2026; sebelumnya dua kotak 6 px).

Pengecualian atas permintaan pengguna: **Closing CTA** memakai garis tipis tanpa grid marker (garis atas, bawah, dan pembagi vertikal), mengikuti referensi yang dilampirkan pengguna. Jangan diterapkan ke section lain tanpa instruksi.

## Struktur halaman (Desktop - 11)

0. Announcement bar 48 px gelap dengan countdown (Days/Hrs/Min/Sec) dan link "Shop the set".
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
11. Shoppable videos — "Rituals in motion.": 4 poster video 480 px (durasi, tombol play) + baris produk (thumbnail, nama, harga, tombol tambah).
12. Ribbon review kedua.
13. Section "Skincare should feel like a pause" dengan foto asimetris.
14. Banner foto dengan bingkai garis dan countdown.
15. Before & after — 3 kartu 560 px dengan toggle Before/After, disclaimer "Individual results vary."
16. Community — Small rituals, real stories.
17. Closing CTA dan footer.
