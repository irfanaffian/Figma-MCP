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
- **Semua teks di Figma berbahasa Inggris** (klien berbahasa Inggris): copy, catatan dokumentasi, nama dan deskripsi komponen/style. Instruksi pengguna boleh bahasa Indonesia.
- **Lingkup kerja hanya Homepage di halaman HiFi** (`11:2160`). Halaman Moodboard, Archive, dan lainnya diabaikan — pemakaian di sana tidak menghalangi pembersihan style/variable.
- **Comment Figma tidak dibaca langsung** (keputusan pengguna 1 November 2026). Jangan memakai skill `figma-comments` atau REST API; feedback disampaikan pengguna lewat chat.
- **Inner page tersambung ke library** (keputusan pengguna 2 November 2026, menggantikan aturan "tanpa sambungan" sebelumnya). Teks memakai text style `Axios/...`, warna token `Axios / Color`, dan elemen yang ada komponennya dipasang sebagai instance. Jangan membuat komponen/variant/style baru tanpa diminta.
- **Gaya mirip Homepage, layout dieksplorasi** (pengguna, 2 November 2026): jangan menyalin section Homepage 100% (termasuk memasang instance section Homepage di inner page). Tiap section boleh punya layout baru, asalkan look and feel sama: satu font Plus Jakarta Sans dengan skala tipografi yang sama, palet cream/ink/stone, garis tipis 12% + kotak penanda 8 px, pill glass, tombol pill dengan lingkaran ikon, ikon Phosphor Regular, padding section 80 px, eyebrow bernomor, copy pendek yang tenang. Komponen global (announcement, header, marquee, ribbon, footer, tombol, kartu produk) tetap dipakai ulang.
- Audit singkat di area yang berubah (font, text style, token, overflow, stroke ikon).
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

Kotak penanda yang sama juga dipakai di **kartu ritual Three simple steps** (ujung kiri garis di atas nama produk), di **video unggulan Shoppable videos** (ujung kiri garis di bawah judul), dan di pita konten banner foto, atas permintaan pengguna 30 Oktober 2026.

Pengecualian atas permintaan pengguna: **Closing CTA** memakai garis tipis tanpa grid marker (garis atas, bawah, dan pembagi vertikal), mengikuti referensi yang dilampirkan pengguna. Jangan diterapkan ke section lain tanpa instruksi.

## Breakpoint responsive (usulan 31 Oktober 2026)

Mengikuti breakpoint tema Shopify Dawn (dasar paling umum template Shopify), supaya desain langsung cocok saat dibangun.

| Breakpoint | Rentang | Frame desain | Kolom / margin / gutter | Padding section | Headline / statement / body |
| --- | --- | --- | --- | --- | --- |
| Mobile | < 750 px | 390 px (cek juga 360) | 4 / 20 / 12 | 48 px | 36 / 28 / 16 |
| Tablet | 750–989 px | 768 px | 8 / 32 / 16 | 64 px | 48 / 36 / 16 |
| Desktop | ≥ 990 px | 1440 px (cek 1280; desain saat ini 1512) | 12 / 40 / 20 | 80 px | 64 / 48 / 18 |

Konten desktop maksimal 1432 px (margin 40 px di 1512). Judul ke konten: 64 / 48 / 32 px.

Frame di Figma (halaman HiFi): `Homepage` (desktop 1512), `Homepage / Tablet` (768), `Homepage / Mobile` (390). Di tablet/mobile: header mobile + menu, kartu jadi carousel geser, kolom bertumpuk.

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
10. Three simple steps — kartu ritual **Variant B** (`376:4313`, dipilih 31 Oktober 2026): pill glass "STEP 0X · …" di kiri atas; judul 32, garis tipis + kotak penanda 8 px, nama produk + volume, tombol panah putih di bawah; gradasi bawah. Pita bawah + angka besar ala referensi Seoul tidak dipakai lagi.
11. Shoppable videos — "Rituals in motion.": judul di atas; video aktif besar di kiri (856×600); kolom kanan: intro + prev/next di atas, label "UP NEXT" + 2 video antrean square 268×268 di bawah; video unggulan memakai treatment Variant B (pill glass, judul + garis bertanda) dengan konten asli: deskripsi, harga $24 USD, tombol Add to bag; video antrean memakai kartu produk putih mengambang (foto kecil, nama, harga, tombol +).
12. Ribbon review kedua.
13. Section "Skincare should feel like a pause" dengan foto asimetris.
14. Banner foto dengan bingkai garis; konten di pita bergaya kartu ritual yang menempel di garis bawah — desktop 2 kolom (judul + tombol | countdown), tablet/mobile bertumpuk (countdown di atas, lalu judul + tombol). Feedback Sid 31 Oktober 2026: tombol tidak lagi di blok terpisah.
15. Before & after — 3 kartu 560 px dengan toggle Before/After, disclaimer "Individual results vary."
16. Community — Small rituals, real stories.
17. Closing CTA dan footer.

## Collection page (desktop, mulai 1 November 2026)

Frame `Collection page` (`496:9103`) di halaman HiFi, kanan frame tablet. Struktur section mengikuti referensi pengguna (Moodboard `491:10449`), gaya visual mengikuti Homepage. Fokus visual desktop dulu; responsive dan komponen dibuat belakangan.

0. Announcement bar.
1. Hero koleksi 600 px: foto penuh + header, bingkai garis dan kotak penanda seperti hero Homepage, breadcrumb, label kiri/kanan, judul uppercase "ALL SKINCARE", intro di kanan bawah.
2. Marquee.
3. Shop by step: 4 kartu foto bergaya kartu ritual (pill STEP, garis bertanda, jumlah produk, tombol panah).
4. Daftar produk:
   - Toolbar: jumlah produk, filter aktif, sort.
   - Sidebar filter 296 px: skin concern, product type, texture, price, availability, kartu promo set.
   - Grid 3 kolom kartu produk Homepage, dengan tile editorial cream di baris 2.
   - "Load more" dengan indikator progres (bukan nomor halaman).
5. Banner countdown (treatment banner Homepage, foto berbeda).
6. Catatan layanan 3 kolom bernomor di latar cream. Tanpa klaim ongkir atau batas hari retur.
7. Ribbon review, lalu footer.

## Product page (desktop, mulai 2 November 2026)

Frame `Product page` (`556:6584`, 1512 × 7133) di halaman HiFi, x 17800. Produk contoh: Soft Start Cleanser. Tidak tersambung ke design system (lihat Aturan kerja).

0. Announcement bar dan header versi gelap di latar terang (garis bawah tipis).
1. Breadcrumb, lalu baris produk:
   - Galeri: 5 thumbnail 72×90 vertikal (aktif bergaris) + foto utama 760×950 (4:5; galeri sticky saat panel info di-scroll) dengan pill glass "STEP 01 · CLEANSE" dan tombol prev/next.
   - Panel info 520 px: badge, nama (H2), deskripsi singkat, rating, harga $24 USD + harga coret, garis + kotak penanda, pilihan ukuran, jumlah + tombol "Add to bag", catatan pengiriman tanpa klaim, kartu cream "Complete the ritual" (2 produk + tombol +), accordion Details / How to use / Ingredients / Delivery & returns.
2. Marquee.
3. 01 / How to use — 3 kolom foto + nomor + judul + teks, garis atas dan pembagi bertanda.
4. 02 / The details — latar cream, 4 kolom ikon (treatment Moments of care): Texture, When to use, Skin feel, Size.
5. 03 / Build your ritual — 3 produk (foto 280×360 + pill STEP) dipisah lingkaran "+", panel cream: checklist 3 item, garis bertanda, total $92 USD, tombol "Add the ritual".
6. 04 / Reviews (latar cream) — ringkasan 4.9 + bintang + sebaran rating + tombol "Write a review", 3 kartu ulasan putih. Isi ulasan contoh template (untuk app ulasan Shopify).
7. 05 / Questions — kiri judul + tombol "Write to us", kanan accordion 5 pertanyaan.
8. 06 / Complete the ritual — 4 kartu produk (garis atas).
9. Ribbon review dan footer.

State terpisah di samping frame: `Product page — sticky add to bag (on scroll)` (1512×88): foto, nama + step, chip ukuran, harga, tombol "Add to bag".

## About us (desktop, 2 November 2026)

Frame `About us` (`596:9937`, 1512 × 5883, x 21100). Eyebrow 01–05.

0. Announcement bar.
1. Hero tipografis: header gelap; baris meta bergaris (01 / OUR STORY · breadcrumb · THREE STEPS · ONE RITUAL) + kotak penanda di kedua ujung; judul Display/Stat dua baris "Skincare [foto pill] for the / quiet [foto pill] *moments.*" (baris 2 rata kanan, kata akhir abu); intro + tombol; foto sinematik 1432×520 dengan treatment banner foto Homepage (`423:10802`): gradasi keterbacaan bawah, 2 garis horizontal putih 40% masuk 40 px dari tepi, 2 garis vertikal putih 50% di kolom margin (x 166/1266) hanya di antara garis horizontal, 5 kotak penanda (4 sudut + tengah atas), label 2 baris kiri "THE AXIOS / RITUAL" dan kanan "THREE STEPS / ONE RITUAL".
2. Marquee.
3. The beginning — layout esai: kolom teks tengah 568 px (eyebrow, H1, standfirst H4, body 2 kolom dengan garis + penanda di atas tiap kolom, baris tanda tangan: nama + peran | 3 foto ritual bulat 40 px bertumpuk), foto kecil kiri atas (344×440) dan kanan bawah (344×480) dengan caption; garis atas tepi ke tepi + penanda.
4. How we make it — heading split, lalu satu foto lebar 1432×640 dengan garis on-photo dan 4 kotak penanda sebagai titik tahap; teks tahap (Idea, Texture, Ritual, Your shelf) putih di atas gradasi.
5. What we believe (cream): daftar tipografi 4 baris bergaris (nomor | judul H2 | body) + penanda.
6. Ribbon review, band penutup gelap split (Statement + tombol Light + link | daftar ritual bergaris putih), footer.

## Lookbook (desktop, 2 November 2026)

Frame `Lookbook` (`599:10145`, 1512 × 7694, x 22732). Eyebrow 01–05.

0. Announcement bar.
1. Sampul editorial: header gelap, baris meta issue bergaris, judul "The slow edit" (Wordmark 250 px, ukuran manual), 3 foto (380 / 624 / 380, foto trio di tengah sebagai fokus; samping diagonal: kiri turun 200, kanan 80) dengan caption di bawah: garis + penanda, label eyebrow, keterangan kanan (6:30 AM / The trio / 9:45 PM). Intro + tombol.
2. Chapter one · Morning — pembuka bab: angka chapter besar (Display/Stat, abu pudar) | eyebrow + H1 | jam "6:30 AM" + keterangan dengan pembagi vertikal, garis bawah + penanda. Lalu foto look besar 880×1040 dengan hotspot glass + tag produk mengambang, look kedua + caption bergaris.
3. Interlude foto full-bleed 720 px dengan bingkai garis on-photo + 4 kotak penanda (treatment hero/banner), judul H1 putih + intro.
4. Chapter two · Night — pembuka bab sama (02, "9:45 PM"), lalu 3 look berundak (400/560/400 px, offset 0/120/48) dengan hotspot, garis bertanda, caption + panah.
5. Shop the look (Look 02): satu foto lebar 1432×800 dengan hotspot bernomor, panel putih 520 px mengambang di kanan bawah (melewati tepi bawah foto) berisi judul H2, daftar 3 produk bergaris, tombol "Add the look to bag".
6. All looks (cream): pembuka judul kiri + angka besar "06 LOOKS" kanan, lalu indeks tipografi 2 kolom × 3 baris (nomor, thumbnail pill, judul H4, chapter, panah) bergaris + kotak penanda.
7. Ribbon review dan footer.

