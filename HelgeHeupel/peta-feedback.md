# Peta feedback klien — HH Website Art Direction (v1, 29 Okt 2026)

Sumber: `HH-Website-Art-Direction-OWW_v1.xlsx` (3 sheet: Website review W01–W28, Page sequence, Creative direction C01–C10).
Figma: file `gyUoGAL8zMRWZ7CChDeNTu`, Page 3, section **Homepage** (`321:5660`), prototype flow "Motion 1".

## Inti feedback dalam 5 kalimat

1. Homepage sekarang terlalu banyak "scroll stop" dekoratif (kubus, globe, Berlin). Klien ingin satu alur jualan: **janji → bukti → cara kerja → metode → industri → nilai → trust → kontak**.
2. Semua headline/copy diganti dengan copy baru di kolom E (sudah ditulis klien, tinggal dipasang).
3. Gaya visual: **Georgia Bold Italic** untuk headline terpilih, **Arial** untuk body/UI. Warna: navy `#061F32`, putih, ice `#F2F8FC`, cobalt `#2144DC` (tombol/selected), electric blue `#00A7F2` (sinyal saja). Tanpa emas/hijau. Kartu terang putih + teks navy, panel gelap navy solid; radius 16, padding 24–32, ikon 2 px berbeda-beda (bukan diamond berulang). Hapus glow bawah kartu.
4. Logo: simbol HH di atas, wordmark "Helge Heupel" di tengah bawahnya — di header dan footer.
5. "Aviation" → **"Aerospace"** di semua tempat; urutan 5 industri tetap.

## Struktur baru (sheet "Page sequence")

| # | Section baru | Dari baris | Frame Figma sekarang |
| --- | --- | --- | --- |
| 01 | Promise + film | W01–W03 | #1 `321:14167` (hero), #2 `321:14215` (Berlin), #3 `321:14234` (karakter cewek) |
| 02 | Delivery proof (+globe kecil) | W04, W05, W08, W09 | #4–#8 deployment, #10 `321:5661` globe, #11–#12 origin story |
| 03 | Evidence base (BARU) | W24 | — |
| 04 | Cara kerja digital twin (3 langkah) | W12–W15, W06 | #15–#21 How it works, kartu di #6/#9 |
| 05 | Delivery approach (BARU) | W25 | — |
| 06 | Industri | W18 (+W27/W28 halaman detail) | #24 `321:10179` |
| 07 | Value + people/planet/profit | W16, W17, W26 | #22 `321:10110`, #23 `321:6437` |
| 08 | Trust + leadership | W20, W22 | #26 `321:10203`, #28 `321:6641` |
| 09 | Closing CTA + footer | W21, W23 | #27 `321:10449`, #29 `321:10598` |

Dipindah ke halaman lebih dalam (keluar dari homepage): W07 Governed AI, W11 detail teknologi (DCIO/kriptografi/paten), detail deployment.

## Per baris: apa maksudnya dan apa yang dikerjakan

Prioritas: **P1** = wajib sebelum launch, **P2** = penyempurnaan.

| ID | Frame | Maksud klien (bahasa sederhana) | Tindakan di Figma |
| --- | --- | --- | --- |
| W01 P1 | #1 hero | Hero harus jual hasil + digital twin, bukan "always up to date" | Ganti eyebrow/headline/body/CTA ke copy baru; nav jadi *Digital twin / Industries / Delivery / Outcomes / Company*; CTA utama "Book a digital twin briefing" + sekunder "Watch the 30-second film"; headline Georgia Bold Italic; monogram transparan (garis HH besar di kanan) diganti still dari film |
| W02 P1 | #2 Berlin | Video Berlin tidak relevan (lokasi, bukan produk) | Ganti dengan poster film 30 detik + label "See how insight becomes action." dan tombol play. **Video final = pekerjaan tim video**, di Figma cukup poster/placeholder |
| W03 P1 | #3 karakter | Karakter cewek rambut bob sudah tidak dipakai | Ganti dengan IMG_5012 (ponytail, visor, headset, jaket silver). **Butuh file IMG_5012 dari klien** |
| W04 P1 | #4 deployment | Angka 99% salah → **99.999%**. Bukti delivery dulu, nama cloud pindah ke detail | Headline "Global software. Accountable delivery." + body + 3 poin delivery; metrik 15,000+ dan 99.999% navy di atas putih; nama cloud dipisah jadi "Explore deployment options"; kubus tetap |
| W05 P2 | #5 | Ini cuma versi pudar W04 | Gabung ke W04, jangan jadi section sendiri |
| W06 P1 | #6 kartu "Understand the impact" | Benefit bagus tapi jadi kartu melayang dekoratif | Pindah ke Step 2 (W14): "Choose the levers with the greatest impact." + perbandingan 2 opsi berlabel "Illustrative" |
| W07 P2 | #9 kartu AI | AI tampil sebagai produk terpisah terlalu awal | Keluarkan dari homepage (halaman detail) |
| W08 P2 | #10 globe | Globe besar tanpa penjelasan | Globe kecil berlabel di samping metrik endpoint W04, caption "Global delivery, illustrated schematically." |
| W09 P1 | #11–#12 origin | Mengulang angka dealer | Gabung ke W04: 1 klaim, 1 kartu bukti, 1 link case; hapus paragraf di atas globe |
| W10 P2 | #13 kubus kosong | Interstitial kubus memperlambat | Hapus frame |
| W11 P1 | #14 DCIO | Terlalu teknis sebelum benefit | "Know what changed. See what it affects." di panel navy solid; detail DCIO/paten pindah ke halaman teknologi |
| W12 P1 | #15 How it works | Pesan "selalu update" diulang + terlalu banyak ruang kosong | Section intro ringkas: "Find opportunities. Understand the levers. Remove the barriers." + 3 langkah bernomor horizontal |
| W13 P1 | #16 Step 1 | Mulai dari input data, bukan keputusan | "Find opportunities." + pertanyaan ilustratif; kubus = objek bisnis berlabel |
| W14 P1 | #17 Step 2 | Diagram radial tidak menunjukkan sebab-akibat | Ganti radial dengan rantai dependensi → perbandingan → forecast (panel navy, baseline + 2 opsi, garis solid/dashed) |
| W15 P1 | #18–#21 Step 3 | Kartu dampak berulang, aksi "buka blokir" kurang terlihat | Rantai: blocked → owner/approval → milestone → outcome; marker "Blocked" navy, aksi terpilih cobalt |
| W16 P1 | #22 value | Benefit generik + ikon diamond berulang | Grid 4 kartu putih, teks navy, ikon 2 px berbeda (programme, operations, customer, capital); hapus glow bawah |
| W17 P1 | #23 | Lanjutan yang mengulang headline | Jadi kartu 3–4 dari grid W16 + link "Discuss your value case" |
| W18 P1 | #24 industri | Pertahankan list, Aviation → Aerospace | Ganti label, perkuat kontras opsi abu, item terpilih cobalt + panah, body baru |
| W19 P2 | #25 kubus | Interstitial kubus kedua | Hapus frame |
| W20 P1 | #26 sertifikasi | Bangun ulang trust | Headline "Evidence you can examine. Accountability you can trust." + status Completed / In progress / Planned, permukaan tenang kontras tinggi |
| W21 P1 | #27 closing | Mengulang copy industri di atas kubus | Panel navy penutup: "Bring us your hardest transformation challenge." + form (nama, email kerja, organisasi, tantangan) + alternatif email |
| W22 P1 | #28 tim | Quantum/iklim terlalu awal, warna emas & hijau | Headline "Independent thinking. Integrity in execution."; navy + aksen biru; hapus diamond emas & teks hijau; bukan kutipan pribadi |
| W23 P1 | #29 footer | Terlalu banyak grup, ada peta kantor | 5 grup (Digital twin / Industries / Delivery / Company / Trust), logo bertumpuk penuh, hapus peta kecuali lokasi akurat |
| W24 P1 | BARU | Database 23.000 proyek referensi belum ada | Section baru setelah delivery proof: 23,000 reference points (5,000 IT transformations sebagai subset) + atribusi dataset |
| W25 P1 | BARU | Metode delivery | Diagram 4 langkah: Define outcomes → Design architecture → Resolve dependencies → Deliver working increments (grafik OS X/Vista **tidak** ditampilkan) |
| W26 P1 | BARU | Value terlalu finansial | Strip People / Planet / Profit di dalam section value |
| W27 P1 | Halaman baru | Detail industri Automotive | Halaman terpisah (di luar homepage) |
| W28 P1 | Halaman baru | Detail Financial services | Halaman terpisah (di luar homepage) |

## Di luar Figma / butuh klien

- **Video** (W02, W03, C03, C07): ganti karakter cewek dan perjelas animasi forecast — pekerjaan editor video.
- **Aset**: IMG_5012.png, still/poster film terbaru, logo HH resmi (hh-official.png), atribusi dataset 23.000 proyek.
- **Legal/konten**: catatan EY Law, status sertifikasi, alamat/entitas di footer — dicek klien, bukan desainer.
- **Implementasi web** (C09 form, reduced motion, aksesibilitas keyboard, mobile 390/768) — untuk developer.
- Baris H20 terpotong di sheet ("Today, the cubes in the video were absolutely brilliant, it is important that we …") — tanyakan lanjutannya ke klien.
- Kolom I (OWW response) dan J (Status) disebut di instruksi sheet tapi belum ada — bisa diisi tim saat membalas.
