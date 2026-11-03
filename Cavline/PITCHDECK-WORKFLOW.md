# Cavline Pitch Deck Redesign: Cara Kerja

Sumber: `PitchDeckSept2026New_compressed.pdf` (11 slide, investor overview, Sept 2026, raise $2.5M).

## Alur kerja
1. Irfan cari referensi (komposisi dan hierarki, bukan warna).
2. Irfan membuat **key layout** di Figma.
3. Irfan kirim link file Figma + frame acuan.
4. Claude membaca layout, komponen, dan variable lewat Figma MCP.
5. Claude mengembangkan slide lainnya dengan gaya yang sama.

## Key layout yang dibutuhkan
| # | Key layout | Mewakili slide | Wajib? |
|---|---|---|---|
| 1 | Cover / Closing (foto besar + headline + logo) | 1, 11 | Ya |
| 2 | Dua kartu berdampingan | 3, 7 | Ya |
| 3 | Visual + teks (mockup HP di satu sisi) | 4 | Ya |
| 4 | Data / angka besar (stat card, chart, donut) | 5, 6, 8, 10 | Ya |
| 5 | Grid orang / foto tim | 2 | Ya |
| 6 | Matriks kompetitor | 9 | Opsional |

## Yang perlu disertakan bersama key layout
- Style dasar: warna, font, ukuran judul, isi, dan label kecil (idealnya style/variable Figma).
- Komponen berulang: label section, kartu, stat angka, footer.
- Grid dan margin.

## Style sekarang (sudah ada di deck)
- Gelap (`#111`), aksen lime (`#B3FF0D`), judul bold, kartu rounded, label section huruf kapital hijau.
- Searah dengan design system app (lihat brief app Cavline).

## Catatan masalah di deck asli
- Slide Problem, Market, GTM: bagian tengah kosong, angka kurang menonjol.
- Foto tim tidak seragam.
- Slide Traction: label grafik saling menimpa.
- Slide Economics: batang roadmap tidak proporsional.
- Angka tidak konsisten: 68 layar (slide 8) vs ~100 (slide 5); $125/slot vs $104-117 di website; target 1M layar (slide 6) vs "4 million screens" (slide 11).

## Aset yang dibutuhkan
Logo vektor, foto tim resolusi tinggi, screenshot app terbaru. PDF yang ada sudah dikompres, jadi kualitas gambar rendah.

## Belum diputuskan
- Output akhir: Figma Slides, slide artifact, atau frame Figma biasa.
- Seberapa jauh perubahan: visual saja, atau juga alur cerita dan teks.
