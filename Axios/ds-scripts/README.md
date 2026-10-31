# Skrip pembangun design system Axios

Ditempel di awal kode `use_figma` (Plugin API). Belum dijalankan untuk komponen — dipakai mulai langkah 2.

- `tokenize.js` — `axiosTokenize(node)`: sambungkan warna, text style, spacing, radius, dan efek ke token `Axios/…` **hanya bila nilainya persis sama** (tampilan tidak berubah). ID collection: Primitives `399:2022`, Color `399:2075`, Responsive `399:2099`.
- `build-components.js` — `ensurePage()` (halaman "Components"), `section(root,title,note)`, `makeSet(section,name,[[sourceNodeId,'Prop=Value'],…],{label:true})`: menyalin node dari Homepage, tokenize, jadikan komponen/variant, dan tambah properti teks `Label`. Homepage tidak diubah (yang diubah hanya salinannya).

## Rencana komponen (langkah 2) — sumber dari Homepage (`215:90`, halaman HiFi `11:2160`)

| Komponen | Variant | Node sumber |
| --- | --- | --- |
| Button | Size=M/L × Style=Dark/Light | `215:397` M Dark, `215:166` M Light, `215:469` L Dark, `221:2665` L Light |
| Icon button | Type=Previous/Next/Shop | `300:2052`, `300:2056`, `376:4340` |
| Badge | Tone=Light/Clay | `289:2047`, `289:2067` |
| Pill glass | — | `376:4329` |
| Chip size | Selected=True/False | `289:2083`, `289:2085` |
| Swatch | Selected=True/False | `289:2076`, `289:2078` |
| Story | State=New/Seen | `301:2133`, `301:2145` |
| Product card | Default/Sale/Hover | `289:2178`, `289:2044`, `289:2109` |
| Ritual card | — | `376:4326` |
| Video card | Featured/Queue | `303:2035`, `303:2054` |
| Collection card | — | `300:2061` |
| Before & after card | — | `301:2102` |
| Section header | Split/Centered | `300:2046`, `301:2097` |
| Announcement bar | — | `300:2022` |
| Header | Desktop (mobile di langkah 4) | `215:130` |
| Ribbon review / Marquee | — | `215:248`, `215:228` |
| Footer | — | `278:4088` |
