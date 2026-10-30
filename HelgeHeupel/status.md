# Status Helge Heupel

Diperbarui: 30 Oktober 2026.

## Posisi saat ini

Revisi v1 dari feedback klien (`HH-Website-Art-Direction-OWW_v1.xlsx`) sudah dikerjakan di section baru **Homepage – Revisi v1** (`325:2`), Page 3, di sebelah kanan section asli. Section asli **Homepage** (`321:5660`, flow "Motion 1") tidak diubah, jadi bisa dibandingkan.

Prototype: flow **"Revisi v1"**, mulai dari `325:8509`. 16 frame, klik untuk lanjut. Smart Animate dipakai di hero→film→karakter→delivery dan intro→step 1→2→3; transisi lain Push (atas), 1,25 detik, Slow.

## Urutan frame Revisi v1 (setelah v1.1, 30 Okt)

| # | Frame | Baris feedback |
| --- | --- | --- |
| 01 | Hero `325:8509` — tombol utama "Book a digital twin briefing" + link film; still film "04 Connect the dots" di kanan atas | W01 |
| 01b | Film poster `325:8557` | W02 |
| 01c | Film – karakter `325:8576` | W03 |
| 02 | Delivery proof `325:8240` — area teks putih, kartu bukti anonim berisi copy W09 ("Built from the realities of global delivery.") + link case, globe kecil berlabel | W04, W05, W08, W09 |
| 03 | Evidence base `329:32` | W24 |
| 04 | How it works – intro `329:2` | W12 |
| 04a–b | Step 1 `330:2`, Step 2 `330:75` (copy + link W06 di kartu perbandingan) | W13, W14, W06 |
| 04c–d | Step 3 blocked `330:170` → resolved `339:2` (marker hilang, Smart Animate) | W15 |
| 04e | Technology `339:67` — panel navy + objek → keputusan → owner | W11 |
| 05 | Delivery approach `332:2` | W25 |
| 06 | Industries `325:4521` — klik Automotive / Banking and payments → halaman detail | W18 |
| 07 | Outcomes + People/Planet/Profit `332:67` | W16, W17, W26 |
| 08a | Trust `332:157` — kartu sertifikasi asli (desain pengguna) dengan copy baru | W20 |
| 08b | Company `325:983` — + contoh delivery | W22 |
| 09a | Closing + form `333:2` | W21, C09 |
| 09b | Footer `325:4940` | W23 |

Halaman detail industri (section `340:2`, desktop, scroll): **W27 Automotive** `340:3` dan **W28 Financial services** `340:131`. Klik di mana saja kembali ke Industries.

Visual kubus di Step 1–3, Technology, dan halaman detail memakai still film "04 — Connect the dots — Color matched" (halaman Verity), sesuai feedback H20 bahwa kubus dari video harus tetap terlihat.

Dihapus dari homepage: W05 (state pudar), W06/W07 kartu melayang, W08 globe layar penuh, W09 origin story, W10 dan W19 interstitial kubus, W11 detail DCIO (pindah ke halaman teknologi). Ini juga menghilangkan 3 link prototype yang macet di versi asli.

## Frame state UI (tanpa prototype, 30 Okt)

Diletakkan di kolom kanan section Revisi v1, sejajar frame asalnya:

- **Interaction states (C08)** `357:111` — default / hover / selected / focus untuk tombol utama, kartu terang, item industri, text link, dan link di panel navy. Hover tombol `#1A36B0`, hover kartu garis `#9FB0C2` + bayangan 12%, selected garis cobalt 2 px, focus ring 2 px navy dengan jarak 3 px (putih di panel gelap).
- **07 State – value card 1–4 detail (W17)** `356:57`, `358:5`, `358:114`, `358:223` — panel detail tiap kartu: Baseline / Action / Measure (contoh ukuran dari sheet F24: service resolution, customer-need satisfaction, approval delay, realised benefits), label *Illustrative definitions, not promised gains*; kartu yang dibuka diberi garis cobalt.
- **09a State – form sent (W21/C09)** `356:2` — konfirmasi setelah form dikirim: langkah berikutnya tanpa janji waktu balasan, plus email langsung.

Kartu Trust: lapisan gradasi cobalt di bagian bawah (`Contrast overlay (C06)`) dan teks roadmap dibuat putih penuh agar terbaca. Hapus layer overlay itu untuk kembali ke tampilan asli.

## Gaya yang dipakai

- Headline: **Gelasio Bold Italic** sebagai pengganti Georgia Bold Italic. Body/UI: **Arimo** sebagai pengganti Arial. Georgia dan Arial tidak tersedia di server Figma MCP; Gelasio dan Arimo ukurannya identik. Disepakati pengguna (30 Okt) untuk dipakai dulu; ditukar ke Georgia/Arial lewat *Replace fonts* di Figma desktop bila diperlukan. Wordmark logo tetap GT Maru.
- Warna: navy `#061F32` (teks/panel), cobalt `#2144DC` (tombol/terpilih), ice `#F2F8FC`, electric blue `#00A7F2` hanya untuk sinyal/forecast. Emas dan hijau dihapus.
- Kartu terang: putih, garis `#D5DEE6`, radius 16, padding 24–32, bayangan navy 6%. Panel gelap: navy solid. Ikon stroke 2 px, berbeda per kartu.

## Belum bisa dikerjakan (butuh klien/tim lain)

- **Still/poster film terbaru** (W01, W02): **Selesai 30 Okt:** poster film memakai still IMG_5012 versi bersih (tanpa label) dari pengguna — di media bawah hero (`325:8556`), frame 01b (`325:8559`), dan frame 01c (`325:8578`). Panel "Watch the 30-second film" dipindah ke kiri bawah agar tidak menutupi wajah. Pojok kanan atas hero memakai still "04 Connect the dots".
- ~~IMG_5012~~ **Selesai 30 Okt:** karakter ponytail dipasang di layer "Karakter – IMG_5012 (ponytail, visor, headset)" (`325:8578`), frame 01c. Kemudian diganti versi bersih tanpa label.
- **Video 30 detik**: ganti karakter dan perjelas forecast (C03, C07) — editor video.
- **Evidence base (W24)** — dikerjakan sesuai sheet (30 Okt): copy E31 persis; angka 23,000 dan 5,000 (subset) berdampingan; grafik bar subset + kalimat "5,000 adalah bagian, bukan tambahan"; penjelasan singkat comparable-project evidence; tanpa data performa dan tanpa klaim "world's largest". **Menunggu klien:** 4 kolom atribusi (Provider, Dataset edition, Counting unit, Access and attribution basis) masih "[to be confirmed by HH]" — sheet tidak menyebutkan nilainya.
- **Trust (W20)** — 30 Okt: sheet hanya mengubah copy, jadi layout kembali ke kartu sertifikasi asli (`355:2`, clone dari `321:14285`). Copy baru: headline, body, link "View trust and security", label status. TISAX 6.0.3 dan ISO 27001:2022 Stage 1 = *In progress*; GDPR = *Completed* (teks asli "Compliant; a regulation in force…" dipertahankan sebagai bukti); "Next on the roadmap" → *Planned*. Catatan: teks roadmap putih pudar di atas gradasi biru muda kontrasnya rendah (C06).
- **W11 vs Page sequence**: sheet bertentangan; section Technology dikembalikan sebagai section pendek. Bisa dihapus bila klien ingin detail teknologi hanya di halaman dalam.
- **Halaman detail W27/W28**: versi desktop sudah dibuat; contoh use case berlabel *Illustrative* dan perlu dicek klien.
- **Mobile 390/768 px** dan state hover/focus (C08) — ditunda; fokus desktop dulu (keputusan pengguna 30 Okt).
- Sel H20 (kolom H "HH key art-direction feedback", baris W13 Step 1) terpotong: "Today, the cubes in the video were absolutely brilliant, it is important that we …". Tanyakan lanjutannya ke klien.
- Status Trust disamakan dengan kartu sertifikasi asli: TISAX 6.0.3 dan ISO 27001:2022 Stage 1 = on-site assessment passed, menunggu evaluasi lembaga sertifikasi.

## Ditunda (keputusan pengguna 30 Okt)

- **W07 Governed AI** — copy dan diagram rekomendasi → approval → aksi menunggu halaman product detail.

## Audit ulang terhadap sheet (30 Okt) — diperbaiki

- **Page sequence G16 (satu CTA utama):** hanya "Book a digital twin briefing" yang berupa tombol biru penuh. "Explore our evidence base", "Explore our delivery approach", "Explore your industry", "Discuss your automotive challenge", "Discuss your financial services challenge" diubah jadi link teks cobalt dengan panah.
- **W15 F:** kartu di Step 3 (blocked dan resolved) bergaris navy; aksi terpilih tetap cobalt.
- **W22 F:** ikon diamond di section Company dihapus (bukan sekadar diwarnai ulang).
- **W18 F:** item industri terpilih ("Assurance") berwarna cobalt + panah.

Konflik di dalam sheet yang dibiarkan sesuai kolom E: tombol industri "Explore your industry" (Page sequence menulis "Discuss your industry challenge"); W11 tetap section pendek di homepage.

Fokus kerja: **desktop saja**. Mobile responsive dan prototype tidak dikerjakan sampai ada instruksi baru.

## Hasil baca ulang sheet (30 Okt) — yang benar-benar masih kurang

File Excel dibongkar (sheet, kolom, baris, drawing, shared strings): tidak ada konten tersembunyi.

- **Satu-satunya data yang tidak ada di sheet:** isi atribusi dataset W24 (provider, dataset edition, counting unit, access/attribution basis). Mungkin ada di brief awal klien ("the user brief" di D31).
- **Bukan pertanyaan untuk klien (sudah dijawab sheet):**
  - H20 terpotong di file asli, tetapi F20 sudah menyatakan kubus film dipertahankan sebagai objek bisnis — sudah dikerjakan.
  - W22/W23: kolom G = "checked by owner", tanggung jawab klien saat review.
  - W27/W28: use case berlabel *Illustrative* sesuai kolom G.
  - W11 tidak bertentangan: teaser di homepage + detail teknis di halaman dalam (Page sequence G15).
- Di luar desain: edit video (W02, W03, W14, C07).

## W24 atribusi (30 Okt)

Aturan kerja: hanya memakai isi sheet, tanpa sumber luar. Counting unit diisi dari kolom E W24: "One megaproject reference point". Provider, dataset edition, dan access/attribution basis tidak ada di sheet, jadi tetap "[to be confirmed by HH]".

## Audit detail kolom per kolom (30 Okt)

Cek otomatis: semua copy kolom E W01–W28 ada di Figma; semua teks memakai Gelasio Bold Italic / Arimo (wordmark GT Maru); tidak ada teks yang terpotong. Selisih kecil dari kolom F/G yang diperbaiki:

- **W08 F** — globe langsung setelah metrik endpoint 15,000+ (sebelumnya setelah 99.999%).
- **W14 G** — label "Decision" pada Option A, melengkapi alur question → dependency → comparison → decision.
- **W26 F** — ukuran di strip: People "rework, service quality", Planet "resource use, emissions", Profit "margin, cash, benefits" (frame utama + 4 frame detail).
- **W27 F** — kartu delivery case dipindah langsung setelah alur keputusan, sebelum use case.
- Perapian: sisa teks Company tersembunyi di frame footer dihapus; spasi berlebih di "Evidence"/"Security" dihapus.

## W24 atribusi jadi satu baris (30 Okt)

Tabel 4 baris diganti satu catatan sumber di bawah penjelasan reference class: "Source: [provider], [dataset edition]. Counting unit: one megaproject reference point. Used under [access and attribution basis]." Bagian dalam kurung siku diisi setelah HH memberi data.

## Cover film resmi (30 Okt)

Pengguna mengirim cover resmi film (2000×1167). Dipasang di media bawah hero (`325:8556`), frame 01b (`325:8559`), dan frame 01c (`325:8578`), menggantikan versi 1440 px. Film 30 detik sendiri masih dikerjakan pengguna. Still kanan atas hero tetap "04 Connect the dots" (W01: ganti ghost monogram dengan film still), agar tidak ada dua gambar karakter yang sama dalam satu layar.
