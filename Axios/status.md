# Status Axios

Diperbarui: 31 Oktober 2026.

## Posisi saat ini

Homepage locked oleh Sid. **Variant B** kartu ritual sudah dipasang di Homepage oleh pengguna (`376:4313`); Variant C/D dan section lama sudah dihapus dari canvas. Frame kerja aktif adalah **Desktop - 11** (`215:90`) di halaman **HiFi** (`11:2160`), tinggi 12341 px. Semua teks Plus Jakarta Sans; audit konsistensi terakhir 31 Oktober 2026 (keempat). Fondasi selesai (31 Oktober). Langkah 4 selesai 31 Oktober: Homepage desktop, tablet (768), mobile (390). **Berikutnya: langkah 5** — inner page (PDP, collection, cart drawer, our story, journal, contact/FAQ) di 3 breakpoint; menu drawer mobile.

## Terverifikasi pada sesi ini

- MCP Figma berhasil membaca file `69Z4JFbNdaEfbjMOHS7oTE`. Halaman: Moodboard (`0:1`), HiFi (`11:2160`), Archive (`112:2542`).
- Metadata Desktop - 11 berhasil dibaca: lebar 1512 px, tinggi 9128 px (sebelum revisi CTA).
- Struktur section sesuai daftar di [brief](./brief.md#struktur-halaman-desktop---11).
- Grid marker dan garis bingkai hanya ditemukan di hero dan banner foto.

Verifikasi ini hanya membaca struktur layer. Ini belum merupakan audit visual, audit spacing, atau audit copy.

## Sudah selesai (dari sesi sebelumnya)

- Spacing, tipografi, tombol, dan warna teks diseragamkan sesuai patokan.
- Typo diperbaiki ("everyday" → "every day", "Costumer" → "Customer").
- Ikon diganti ke Phosphor Regular dan dikonversi ke vector stroke.
- Klaim tanpa data dihapus. Copy ditulis ulang sesuai tema Axios.
- CTA penutup diubah menjadi layout tengah.
- Section "3 steps" diubah menjadi komposisi foto asimetris.
- "Moments of care" diubah menjadi 4 kolom dengan garis pemisah dan ikon 32 px.
- Hero dibuat ulang dengan bingkai garis, grid marker, dan headline uppercase 80 px.
- Banner foto diberi treatment garis yang sama dengan hero.
- 29 Oktober 2026: Closing CTA (`215:460`) disusun ulang mengikuti referensi pengguna. Baris atas berbingkai garis dengan pembagi vertikal: kiri 3 foto ritual bulat 96 px + label "Cleanse | Hydrate | Comfort"; kanan eyebrow + headline 64 px dua warna ("More room for [foto pill] *you.*" abu). Foto pill 104×64 px (tekstur krim Cloud Comfort) disisipkan di tengah kalimat, mengikuti treatment brand intro. Baris bawah: paragraf dan tombol, rata dengan kolom kanan. Warna oranye dan tombol panah slider dari referensi sengaja tidak dipakai. Tinggi Desktop - 11 menjadi 9294 px.
- 29 Oktober 2026: Rating 5 bintang (24 px, gap 8 px, bintang terisi warna teks kutipan) ditambahkan di bawah kutipan testimonial pada kartu Featured customer review (`215:428`), jarak 32 px dari kutipan.
- 29 Oktober 2026 (feedback Sid): Marquee "Daily care, simplified" (`215:228`) — ikon daun pemisah diganti 4 thumbnail foto pill 72×44 px (radius 22). Tinggi strip tetap 92 px (jarak garis ke isi 24 px).
- 29 Oktober 2026 (feedback Sid): 12 grid marker di hero dan banner foto diganti dari dua kotak 6 px menjadi satu kotak 8×8 px di titik pertemuan garis.
- 29 Oktober 2026 (feedback Sid): Countdown ditambahkan di banner foto (`215:119`), kolom kanan di atas tombol "Find your ritual": label "THE RITUAL SET ENDS IN", angka 32 px dan unit 12 px (Days/Hrs/Min/Sec). Angka dan label masih contoh untuk template. Posisi bawah konten banner tetap.
- 29 Oktober 2026: Announcement bar dengan countdown di atas header sempat dicoba, lalu dibatalkan atas permintaan pengguna.
- 29 Oktober 2026 (feedback Sid): 4 kartu produk di section Shop (`215:377`) dirombak. Kartu di-detach dari komponen `Axios / Product card` (192:1758, dipakai 24 instance) supaya frame lain tidak ikut berubah. Perubahan: garis putus-putus dan wishlist dihapus; harga 16 px Medium (tidak bold) dengan dukungan harga sale (harga coret abu) di kartu Soft Start Cleanser; tombol Add pindah ke kondisi hover (contoh di kartu Daily Dew Serum: tombol "Add to bag" di bawah foto); ditambah swatch warna (3 lingkaran 16 px) dan swatch ukuran (chip ml); dua badge berwarna per kartu (badge pertama sand, badge kedua clay di semua kartu; label: status + Sale/Morning/Night). Ukuran ml dipindah dari deskripsi ke swatch. Tinggi kartu tetap 544 px.
- 29 Oktober 2026: Kartu Soft Start Cleanser dijadikan patokan gaya kartu produk. Swatch terpilih 18 px di dalam cincin 24 px; warna swatch (#EDE6DA, #D8C7B0, #B9C2AE) dan warna badge disamakan di keempat kartu.
- 29 Oktober 2026: Kontras badge dinaikkan agar tidak menyatu dengan foto: badge pertama putih solid (teks #21211F, titik sage), badge kedua terakota #9A5540 (teks dan titik putih). Outline swatch warna yang tidak terpilih disembunyikan di semua kartu mengikuti kartu 1.
- 29 Oktober 2026 (feedback Sid): Garis atas "Moments of care" (`215:328`) dibuat edge to edge (1512 px, x 0). Outline atas grid dihapus dan diganti garis 1 px warna sama (#21211F 12%). Pembagi kolom vertikal tetap. Tinggi section Cloud Comfort tetap 1232 px.
- 29 Oktober 2026 (feedback Sid): Posisi section kartu ritual "Three simple steps" (`287:4146`) ditukar dengan product grid Shop (`215:377`). Urutan baru: marquee → Shop (y 2108) → Cloud Comfort (y 3108) → Three simple steps (y 4460) → ribbon review kedua (y 5288). Jarak antar section tetap 120 px; posisi section lain tidak berubah.
- 29 Oktober 2026 (feedback Sid): Section Cloud Comfort (`215:309`) dijadikan slider. Kontrol di atas foto, 32 px dari kiri, kanan, dan bawah: 3 titik indikator (Cleanse, Hydrate, Comfort; titik ketiga aktif berupa pill 24×8 px, sesuai "Step 03") dan tombol prev/next 48 px yang menyalin gaya Community. Kartu catatan kanan tidak diubah, jadi bisa dipakai untuk konten how to use / step 1, 2, 3.
- 29 Oktober 2026 (feedback Sid): Currency switcher "USD $" + caret ditambahkan di header (`215:156`), sebelum ikon akun, dalam pill glass tinggi 40 px (putih 16%, outline putih 24%, background blur 16, padding 8/12/8/16), teks 14 px Regular putih.
- 29 Oktober 2026 (feedback Sid): Announcement bar dengan countdown dipasang di atas header (48 px, semua konten turun 48 px).
- 29 Oktober 2026 (feedback Sid): 3 section baru — Collections / Shop by category (`300:2045`, setelah Shop, mengikuti referensi carousel kategori), Shoppable videos (`301:2022`, setelah Three simple steps), Before & after (`301:2096`, setelah banner foto). Jarak antar section 120 px; Desktop - 11 kini 12422 px.
- 29 Oktober 2026 (feedback Sid): Deretan 3 foto di atas brand intro diganti Stories (`301:2132`): 6 lingkaran 96 px dengan cincin 2 px dan label 12 px.
- 29 Oktober 2026: Layout Shoppable videos dieksplorasi ulang agar tidak monoton: heading split, video unggulan + 3 video 9:16 berundak, info produk jadi kartu mengambang di dalam video, gradien bawah untuk keterbacaan.
- 29 Oktober 2026: Shoppable videos — konsep "video aktif di kiri": pengguna menyisakan 2 video kecil di kanan (grup `299:4147`), lalu keduanya dibuat square 268×268.
- 29 Oktober 2026: Intro dan prev/next Shoppable videos dipindah ke kolom kanan (`305:2022`) di atas antrean; ditambah label "UP NEXT". Tinggi section 776 px.
- 29 Oktober 2026: Desktop - 11 kini berada di halaman HiFi (`11:2160`). Elemen baru disesuaikan dengan gaya section lama: headline letter-spacing -1%, teks pendukung 18 px Medium gelap, tombol "Add to bag" memakai pola pill Inter Display. Eyebrow diberi nomor urut ulang: 01 Axios care, 02 Shop by category, 03 Comfort ritual, 04 Watch & shop, 05 Our philosophy, 06 Before & after, 07 Community, 08 Your next little ritual.
- 30 Oktober 2026 (feedback Sid): Thumbnail marquee "Daily care, simplified" diperbesar dari 72×44 ke 96×56 px (radius 28). Tinggi strip 92 → 96 px (jarak garis ke isi 20 px), section di bawahnya turun 4 px.
- 30 Oktober 2026 (feedback Sid): Panah kecil kiri/kanan (Phosphor caret 16 px, putih) ditambahkan di ujung announcement bar (`300:2022`), 40 px dari tepi, sejajar margin halaman.
- 30 Oktober 2026: Kotak penanda putih 8×8 px (gaya hero) ditambahkan di titik pertemuan garis footer dan pembagi ml pada 3 kartu ritual (`215:186`).
- 30 Oktober 2026: Kartu produk di video unggulan Shoppable videos diganti footer bergaya kartu ritual (`330:2022`): menempel di bawah video, lapisan gelap transparan, garis atas putih 28%; kolom nama + deskripsi, kolom harga besar "$24 USD" (54 px), kolom tombol terang "Add to bag" (gaya tombol banner), dipisah garis vertikal putih 35%, plus 2 kotak penanda 8 px di titik pertemuan garis.
- 30 Oktober 2026: Dua video antrean (`299:4147`) memakai footer bergaya kartu ritual versi sederhana (tinggi 72 px): nama produk SemiBold 16 | harga 24 px, dipisah garis vertikal + kotak penanda 8 px. Thumbnail, tombol tambah, dan deskripsi dihapus.
- 30 Oktober 2026: Konten banner foto (`215:119`) diubah jadi pita bergaya kartu ritual (`332:2022`, 1100×184, x 206–1306, menempel di garis bawah bingkai): kolom pesan (teks 32 px), kolom countdown, dan kolom tombol, dipisah garis vertikal putih 35%. Kotak penanda 8 px ditambahkan di titik pertemuan garis atas pita (4) dan di garis bawah pada pembagi kolom (2).
- 30 Oktober 2026 — **Audit konsistensi Desktop - 11**:
  - Gaya teks unik turun dari 82 ke 43; IBM Plex Mono (3 teks ribbon) diganti Plus Jakarta Sans SemiBold 18; ukuran ganjil 17/15 px dihapus.
  - Warna teks dan elemen dirapikan: gelap #262623/#282723/#000000 → #21211F; abu #7C766E/#736B60/#625D55 → #807A73; #C4C4C4 → #807A73 60%.
  - Line-height/tracking diseragamkan per peran (lihat Skala tipografi di brief); judul 20 px semua Medium; eyebrow CTA dan judul kolom footer jadi gaya eyebrow standar; unit countdown announcement disamakan dengan banner (uppercase SemiBold 9%).
  - Tombol: radius/jarak CTA disamakan; tombol terang di atas foto putih #FFFFFF; label tombol hover "Add to bag" jadi Inter Display 16.
  - Stroke ikon 18 px dikoreksi ke 1.125 (rumus 16/256).
  - Section disusun ulang agar menempel tanpa tumpukan/celah (sebelumnya Cloud Comfort bertumpuk 8 px, philosophy→banner bercelah 7 px); Stories 256 px. Tinggi Desktop - 11 kini 12364 px.
  - Overflow teks diperbaiki (nama produk Cloud Comfort, deskripsi Moments of care); kolom Moments of care dibuat rata atas agar judul sejajar.
- 30 Oktober 2026: Nama produk di footer 2 video antrean dikembalikan ke SemiBold 16 (audit sempat mengubahnya ke Medium).
- 30 Oktober 2026: Atas permintaan pengguna, 2 video antrean dikembalikan ke kartu produk putih mengambang (foto 40 px, nama 14 Medium, harga 12 abu, tombol + 32 px); footer gelap bergaris dan kotak penanda di video antrean dihapus. Video unggulan tetap memakai footer bergaya kartu ritual.
- 30 Oktober 2026 — **Audit kedua**: 41 gaya teks, 2 font, 3 warna teks (#21211F, #807A73, putih); 0 overflow, 0 ikon salah stroke, section menempel tanpa celah. Dirapikan: #111111 (bintang/asterisk ribbon) dan #000000 12% (outline tombol panah) → #21211F; tracking teks marquee → -2%. Dibiarkan: tint #241A12 13% di kartu ritual, shape mask #D9D9D9, tombol #F4F4F4 "Meet Axios" (di atas latar putih). Metode audit disimpan sebagai skill repo `.claude/skills/figma-design-audit`.
- 30 Oktober 2026: Semua teks kini hanya Plus Jakarta Sans. 11 teks Inter Display (10 label tombol, logo header, wordmark footer) diganti dengan ketebalan sama. Wordmark footer diperkecil 619 → 590 px agar tetap satu baris (Plus Jakarta lebih lebar). Tidak ada overflow.
- 31 Oktober 2026 (Sid): Homepage dinyatakan **locked**. Sid suka section kartu ritual tetapi khawatir terlihat menyalin referensi Seoul clinic (3 kartu foto sama besar, judul kiri atas, pita bawah dengan pembagi vertikal, angka besar + satuan kecil di kanan). Dibuat **Variant B** di samping frame Homepage (`374:2022`, x 9068, sejajar section asli) tanpa mengubah Homepage: pill glass "STEP 0X · CLEANSE/HYDRATE/COMFORT" di kiri atas; pita bawah + angka besar dihapus, diganti judul 32 px, garis tipis dengan kotak penanda 8 px, baris produk (nama + volume kecil) dan tombol panah putih; gradasi bawah untuk keterbacaan. Menunggu pilihan Sid.
- 31 Oktober 2026: Eksplorasi tambahan kartu ritual di samping Variant B (Homepage tetap tidak diubah): **Variant C** (`375:2022`, x 10780) — foto bersih tanpa teks, garis ritual dengan kotak penanda + label "01 — CLEANSE" di atas tiap foto, judul 24 px + produk · volume dan tombol panah di bawah foto. **Variant D** (`375:2110`, x 12492) — kartu berundak 560/496/432 px rata bawah, pill STEP di atas, kartu produk putih mengambang di bawah.
- 31 Oktober 2026: Kartu video unggulan Shoppable videos (`303:2035`, di dalam Homepage, atas permintaan pengguna) diberi treatment Variant B: pill durasi glass "FEATURED · 0:24"; pita bawah bergaris + harga besar + tombol Add to bag dihapus, diganti judul 32 SemiBold, garis tipis dengan kotak penanda 8 px, baris deskripsi + harga kecil, dan tombol panah putih 40 px. Padding kartu 24 px.
- 31 Oktober 2026: Konten video unggulan dikembalikan seperti sebelumnya di dalam treatment Variant B: harga "$24" 40 px + "USD" kecil dan tombol terang "Add to bag" (menggantikan tombol panah), label durasi teks asli "Featured · 0:24" (tampil kapital via text case).
- 31 Oktober 2026 — **Audit ketiga** (skrip library): 1 font, 3 warna teks, 40 gaya teks, 0 flag, 0 overflow, 0 ikon salah stroke, section menempel tanpa celah (tinggi 12341 px). Diperbaiki: tombol "Explore rituals" di Variant B masih `#282723` (terbawa saat clone) → `#21211F`. Dicatat, dibiarkan: harga video unggulan 40 px (satu-satunya ukuran 40, peran display harga).
- 31 Oktober 2026 — **Audit keempat** (skrip library): 1 font, 3 warna teks, 40 gaya teks, 0 flag/overflow/ikon salah, section menempel tanpa celah. Kesiapan responsive: hero dan banner foto masih **group** (bukan auto-layout), header belum auto-layout, frame halaman absolute; 13 text style lokal lama (DM Sans/Instrument Serif/Ritual Card) **tidak dipakai**; 36 node masih terikat ke variable lama (`Axios / Botanical direction`, `Axios / Warm Editorial`); komponen hampir tidak dipakai (1 instance).

## Rencana berikutnya (disepakati 31 Oktober 2026 — menunggu persetujuan pengguna)

Homepage desktop sudah locked → saat yang tepat membangun design system **ringan** sebelum responsive dan inner page:

1. **Foundation**: bersihkan style/variable lama; buat variable warna, spacing, radius, dan ukuran teks dengan mode Desktop / Tablet / Mobile; text style per peran (mengikuti skala tipografi di brief).
2. **Komponen inti** (dengan varian ukuran/breakpoint): tombol (L/M, gelap/terang), tombol panah prev/next, pill/badge, section header (eyebrow + headline + teks), kartu produk (default/hover/sale), kartu ritual, kartu video (featured/antrean), header (desktop/mobile + menu), announcement bar, ribbon/marquee, footer.
3. **Rapikan Homepage desktop** memakai komponen + auto-layout penuh (hero & banner dari group ke auto-layout) — tampilan tidak berubah.
4. **Homepage tablet (768) dan mobile (390)** dari komponen yang sama.
5. **Inner page** (PDP, collection/PLP, cart drawer, our story, journal, contact/FAQ) langsung di 3 breakpoint.
- 31 Oktober 2026 — **Langkah 1 (fondasi) selesai**: 3 variable collection (98 variable: Primitives, Color semantik, Responsive Desktop/Tablet/Mobile), 27 text style `Axios/…` dengan ukuran terikat breakpoint, 1 effect style, dan halaman dokumentasi **Foundations** (`401:2023`). Semua diambil dari nilai Homepage; Homepage tidak diubah (0 binding/style baru). Detail: [foundations.md](./foundations.md).
- 31 Oktober 2026 — **Langkah 2 (komponen inti) selesai** di halaman **Components**: 18 komponen / 32 variant, disalin dari Homepage lalu disambungkan ke token hanya bila nilainya persis sama — Button (M/L × Dark/Light, properti Label), Icon button (Previous/Next/Shop), Badge (Light/Clay), Pill glass, Chip size, Swatch, Story (New/Seen), Product card (Default/Sale/Hover), Ritual card, Video card (Featured/Queue), Collection card, Before & after card, Section header (Split/Centered), Announcement bar, Header / Desktop, Ribbon review, Marquee, Footer. Homepage tidak berubah (tinggi tetap 12421 px). Semua teks dokumentasi Figma kini bahasa Inggris. Catatan: kartu belum memakai instance komponen kecil di dalamnya (badge, swatch, tombol masih layer biasa) — dirapikan saat pemasangan ke Homepage (langkah 3).
- 31 Oktober 2026 — **Langkah 3 (komponen + token di Homepage) selesai**:
  - Backup Homepage sebelum perubahan: halaman Archive, `407:2236` ("Homepage — backup before components (31 Oct 2026)").
  - 38 elemen Homepage diganti instance komponen (announcement bar, header, 2 ribbon, marquee, footer, 4 kartu produk, 3 kartu ritual, 3 kartu video, 5 kartu koleksi, 3 kartu before-after, 2 section header, 6 story, 6 tombol panah, 2 tombol); teks dan foto asli dipertahankan sebagai override.
  - Layer non-komponen disambungkan ke token: 186 warna, 39 text style, 187 spacing, 15 radius. Variable lama dilepas/dipetakan (color/ink #282723 → text/primary #21211F, color/muted #7C766E → text/secondary #807A73 — sesuai keputusan audit; selisih tidak terlihat). Koleksi lama `Axios / Botanical direction` dan `Axios / Warm Editorial` **dihapus**.
  - Verifikasi: tinggi tetap 12421 px; overlay Difference terhadap backup hitam (identik) kecuali bekas perubahan warna di atas.
  - Belum: hero dan banner foto masih group (bukan komponen/auto-layout) — dibangun ulang saat langkah 4 (tablet/mobile).
- 31 Oktober 2026 — **Langkah 4 (responsive) selesai** di halaman HiFi, di samping Homepage desktop (tidak diubah, tetap 1512×12421):
  - **Homepage / Mobile** (`409:2574`, 390 px, mode Responsive = Mobile) dan **Homepage / Tablet** (`411:3275`, 768 px, mode Tablet). Font, margin, dan padding section mengikuti token responsive.
  - Pola: baris kartu → carousel geser (produk, koleksi, ritual, before-after, story, video antrean; kartu 296–340 px); kolom berdampingan → bertumpuk; chip kategori → baris geser; brand intro → teks membungkus dengan foto inline.
  - Komponen baru: `Header / Mobile` (logo, tas, menu), `Announcement bar / Mobile`, `Footer / Mobile` (kolom bertumpuk, wordmark 140 px), variant `Video card / Type=Featured Mobile`. Komponen mobile dikunci ke mode Mobile.
  - Hero dan banner dibangun ulang sebagai frame auto-layout (`Hero / Mobile`, `Banner / Mobile`, versi tablet lebih tinggi) dengan garis + kotak penanda.
  - Tablet memakai header/menu mobile (pola umum Shopify < 990 px).
- 31 Oktober 2026 — **Koreksi responsive agar gaya = desktop** (atas masukan pengguna: ukuran boleh beda, gaya tidak):
  - Hero mobile/tablet dibangun ulang dari elemen desktop: tanpa gradasi (desktop tidak memakai gradasi), garis putih 1 px opasitas 40% (horizontal) / 50% (vertikal), kotak penanda 8 px di setiap pertemuan, label kiri + kanan, intro Medium 16 putih 85%, avatar, headline uppercase, tombol, dan wordmark italic "Axios Care" (77 px mobile, 156 px tablet).
  - Banner mobile/tablet: gradasi + bingkai garis + label kiri/kanan seperti desktop; pita gelap transparan (#1F1A14 22%, garis atas putih 28%) disusun bertumpuk dengan pembagi garis atas putih 35% dan kotak penanda.
  - `Announcement bar / Mobile` kini memakai countdown berkotak yang sama dengan desktop + panah (pesan & link disembunyikan karena tidak muat).
  - Rating "4.9" kembali -2%; Moments of care: mobile bertumpuk dengan garis atas, tablet 2×2 dengan garis kiri/atas (warna garis sama).
  - Verifikasi: 1 font, 3 warna teks, 0 overflow, perbandingan gaya layer-per-layer terhadap desktop tanpa selisih (kecuali garis pemisah yang dipindah sisi).
- 31 Oktober 2026 — **Audit detail responsive** (fokus adaptasi layout): elemen gepeng karena hug otomatis (lingkaran ikon tombol, tombol panah) dikembalikan ke ukuran desktop; kata patah "you." diperbaiki; strip ribbon/marquee mulai dari kiri; chip kategori mulai dari kiri; jarak judul→konten memakai token `layout/heading-gap` (32/48); foto Philosophy berdampingan; potret Community diperpendek; brand intro tablet tidak lagi bertumpuk; header Collections tablet kembali sejajar dengan panah.
- **Keputusan pengguna (31 Oktober 2026):** jangan memaksa komponen desktop beradaptasi lewat override. Buat **variant Breakpoint = Desktop / Tablet / Mobile** per komponen (section header, kartu, video featured, header, announcement, footer, dan section besar: hero, banner, Cloud Comfort, Community, CTA), lalu frame tablet/mobile cukup memakai instance variant tanpa override layout. Ini langkah berikutnya sebelum inner page.
- 31 Oktober 2026 — **Audit responsive lanjutan (font per breakpoint + error layout)**:
  - Text style dipasang ke teks komponen yang belum punya (deskripsi produk, harga, label, placeholder, dll.) sehingga ikut mengecil per breakpoint. Skala token tablet/mobile diperhalus: title/product 20/18/16, heading/h4 24/20/18, heading/h3 32/28/24, heading/h2 44/36/28, display/number 40/32/24, body/lead 18/17/16, ribbon 18/16/14, button/lg 18/18/16.
  - Ukuran manual per breakpoint untuk teks khusus: ribbon review 14/16, chip "All skincare" 14/16, countdown banner 28/32 (hero, wordmark, rating sudah diatur sendiri).
  - Error layout diperbaiki: navigasi Community (customer di atas, 01/04 kiri + panah kanan), CTA mobile "More room / for [foto] *you.*", kolom email 56 px satu baris, ikon Moments of care tidak menempel garis, paragraf tanpa enter manual, kartu produk video antrean menampilkan harga.
  - Audit akhir: 0 bentuk gepeng, 0 kata patah, 0 overflow, 1 font.
- 31 Oktober 2026 — **Section jadi komponen dengan variant Breakpoint** (keputusan pengguna: responsive lewat variant, bukan override):
  - Backup sebelum perubahan di Archive: `423:3727` (desktop), `423:4085` (tablet), `423:4434` (mobile).
  - 13 component set di halaman Components → frame **Axios / Sections**: `Section / Hero, Stories, Brand introduction, Shop, Collections, Cloud Comfort, Three simple steps, Shoppable videos, Philosophy, Banner, Before & after, Community, Closing CTA & footer`, masing-masing `Breakpoint=Desktop/Tablet/Mobile` (1512/768/390, tiap variant dikunci ke mode Responsive-nya). Hero dan banner desktop dibungkus dulu ke frame (group + garis + header) tanpa mengubah posisi.
  - Ketiga frame Homepage kini berisi instance variant tersebut (+ strip ribbon/marquee + announcement). Verifikasi Difference terhadap backup: desktop & tablet identik.
  - **Skala font per breakpoint dibuat adaptif** (bukan menyalin desktop): heading/h1 64/44/32, statement 48/32/24, heading/h2 44/32/24, heading/h3 32/26/22, display/hero 56/44/32; hero headline variant 56/44/32.
  - Perbaikan variant: brand intro (lebar & margin), footer tablet pakai mode Tablet + wordmark 281 px, judul Collections diberi margin kanan. Audit akhir: 0 teks menempel tepi, 0 kata patah.
  - Catatan: lebar variant sempat membengkak karena mengikuti isi carousel — semua variant kini dikunci lebarnya.

- 31 Oktober 2026 — **Rapikan mobile (brand intro & kartu Community)**:
  - Brand intro mobile: 3 baris kaku diganti satu paragraf mengalir (`Brand statement / flow`, auto-layout wrap rata tengah); teks dipecah per frasa dan foto inline (60×36, pasangan 36×36 tumpang -10, 36×36) ikut di alur kalimat, baris terakhir tetap abu.
  - Kartu ulasan Community mobile: padding 32/24, jarak tetap 24 (sebelumnya space-between sehingga bintang menempel garis), blok customer berjarak 24 dari garis, teks ritual bisa turun baris (tidak terpotong lagi).

- 31 Oktober 2026 — **Kartu Before & after responsive dipendekkan**: sebelumnya tinggi 560 sama dengan desktop sehingga terlalu tinggi; kini rasio 4:5 — tablet 340×424, mobile 300×376 (desktop tetap 464×560). Gradasi ikut menyesuaikan.

- 31 Oktober 2026 — **Marquee "Daily care, simplified" responsive**: komponen `Marquee` kini component set `Breakpoint=Desktop/Tablet/Mobile` (desktop tidak berubah). Tablet 768×80: thumbnail 80×48, jarak 20, margin kiri 32. Mobile 390×72: thumbnail 64×40, jarak 16, margin kiri 20. Strip mulai dari teks rata kiri (sebelumnya strip 1512 rata tengah sehingga di mobile hanya terlihat foto terpotong + satu frasa); foto pertama dipindah ke akhir. Instance di Homepage / Tablet dan / Mobile sudah di-swap.

- 31 Oktober 2026 — **Semua bagian tablet/mobile kini memakai komponen per breakpoint** (prinsip pengguna: mobile & tablet punya komponen sendiri agar layout fit):
  - `Ribbon review` → component set Desktop/Tablet/Mobile. Tablet 768×76: bintang 20 px, jarak 32, margin 32. Mobile 390×68: bintang 16 px, jarak 24, margin 20. Strip mulai rata kiri (sebelumnya versi 1512 dengan bintang 24 px dan teks terpotong di tepi).
  - `Announcement bar` → component set Desktop/Tablet/Mobile. Tablet 768×48 baru: panah di tepi (margin 32), countdown + link "Shop the set" di tengah (pesan panjang tetap hanya di desktop). Sebelumnya tablet memakai versi mobile.
  - Pemindaian akhir: semua instance tingkat atas di Homepage / Tablet dan / Mobile memakai variant Breakpoint masing-masing; tidak ada variant Desktop di dalamnya.

- 31 Oktober 2026 — **CTA + footer mobile/tablet dirapikan**:
  - `Footer` kini component set Desktop/Tablet/Mobile (sebelumnya tablet memakai Footer / Mobile).
  - Mobile: link jadi grid 2 kolom (Shop | Learn, Follow along | Here to help; jarak 12 seragam), kolom email selebar penuh dengan placeholder rata tengah, "All skincare" 14 → 16 seperti link lain, link legal berjejer (wrap) bukan bertumpuk 32 px, copyright + USD satu baris. Tinggi footer 1508 → ±1050.
  - Tablet 768: 4 kolom link sebaris, kolom email 480, wordmark 281, margin 32.
  - CTA tablet: celah lebar di "More room for [foto] you." hilang (teks tadinya lebar tetap 320).

- 31 Oktober 2026 — **Judul CTA mobile jadi 2 baris**: "A little care." / "More room for [foto] *you.*" (sebelumnya 3 baris). Foto inline 48×36, jarak 6; lebar baris 338 dari 350.

## Bagian yang tidak disentuh

Hero, brand intro, dan kartu ritual (mengacu ke Desktop - 6), ribbon review pertama, serta section lain yang tidak diminta.

## Catatan untuk dicek

- Nama layer di beberapa frame tidak lagi sama dengan teksnya, misalnya layer "Cleanse, hydrate and comfort. Three everyday essentials…". Teks di canvas yang menjadi acuan.
- Angka "34+" dan "190+ Customer Reviews" perlu dipastikan ke pengguna punya sumber datanya.
- Kartu produk di section Shop Desktop - 11 sudah di-detach (layer biasa). Komponen `Axios / Product card` versi lama tetap dipakai di frame lain.
- Foto di section baru (collection, video, before/after, stories) memakai ulang foto yang sudah ada sebagai placeholder; before/after belum memakai pasangan foto sebelum/sesudah asli.
- Copy before/after (durasi minggu, keluhan kulit) adalah contoh; perlu data nyata dari klien sebelum dipakai.
- Beberapa tinggi section bukan kelipatan 4 (Shop 1038, Collections 826, banner 669, Before & after 943, Community 970, footer 1794) karena tinggi teks; tidak mengganggu visual.
- Ada dua countdown untuk promo yang sama (announcement bar dan banner foto) — keduanya diminta Sid; pertimbangkan cukup satu.
- Harga sale ($24 dari $30), varian warna, dan ukuran di kartu produk adalah contoh template; perlu dikonfirmasi ke klien.

## Melanjutkan dari perangkat lain

1. Baca README, brief, status, dan riwayat.
2. Periksa autentikasi dan akses MCP Figma di sesi tersebut.
3. Baca kondisi terbaru Desktop - 11 sebelum mengedit.
4. Ikuti instruksi terbaru dan aturan di brief.
5. Perbarui file ini dengan hasil yang benar-benar diverifikasi.
