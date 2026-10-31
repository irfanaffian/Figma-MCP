# Fondasi design system Axios

Dibuat 31 Oktober 2026 dari nilai yang **benar-benar dipakai di Homepage** (Desktop - 11, `215:90`). Homepage tidak diubah dan belum dihubungkan ke token ini; pemasangan dilakukan di langkah berikutnya setelah disetujui.

Lokasi di Figma: halaman **Foundations** (`401:2023`), file `69Z4JFbNdaEfbjMOHS7oTE`.

## Variable collections

| Collection | Mode | Isi |
| --- | --- | --- |
| `Axios / Primitives` | Value | 32 warna (ink, stone, white, cream, sand 100–700, clay, sage, umber, swatch, alpha putih/ink/stone/umber), 16 spacing (2–96), 4 radius (4, 8, 12, pill 999). Tersembunyi dari picker (scope kosong untuk warna) |
| `Axios / Color` | Light | 23 token semantik (alias ke primitives): `text/primary · secondary · muted · inverse · inverse-secondary · inverse-label`, `bg/page · cream · sand · inverse · button-light`, `border/subtle · default · strong · footer`, `on-photo/line · marker`, `glass/fill · border`, `overlay/scrim · tint`, `accent/clay · sage` |
| `Axios / Responsive` | Desktop · Tablet · Mobile | Layout (`frame-width` 1440/768/390, `columns` 12/8/4, `margin` 40/32/20, `gutter` 20/16/12, `section-padding` 80/64/48, `heading-gap` 64/48/32) dan 17 ukuran font per peran |

Semua variable punya scope spesifik dan code syntax web (`var(--color-text-primary)`, dst.).

## Ukuran font per breakpoint (`Axios / Responsive`)

| Token | Desktop | Tablet | Mobile |
| --- | --- | --- | --- |
| display/hero | 56 | 44 | 36 |
| display/stat | 104 | 80 | 64 |
| display/number | 40 | 32 | 24 |
| heading/h1 | 64 | 48 | 36 |
| heading/statement | 48 | 36 | 28 |
| heading/h2 | 44 | 36 | 28 |
| heading/h3 | 32 | 28 | 24 |
| heading/h4 | 24 | 20 | 18 |
| title/product | 20 | 18 | 16 |
| body/lead | 18 | 17 | 16 |
| body/lg | 18 | 16 | 16 |
| body/md | 16 | 16 | 16 |
| body/sm | 14 | 14 | 14 |
| caption | 12 | 12 | 12 |
| ribbon | 18 | 16 | 14 |
| button/lg | 18 | 18 | 16 |
| button/md | 16 | 16 | 14 |

## Text styles (27, prefix `Axios/`)

Display (Hero, Stat, Number, Wordmark) · Heading (H1, H1 Italic, Statement, H2, H3, H3 Medium, H4) · Title/Product · Body (Lead, LG, MD, MD Medium, SM, SM Medium) · Caption (Regular, Medium) · Label (Eyebrow, Ribbon, Nav, Story) · Button (LG, MD, SM).

Ukuran font tiap style terikat ke variable responsive, jadi otomatis berubah saat frame memakai mode Tablet/Mobile. Pengecualian: `Display/Wordmark` (590 px, diatur manual per breakpoint).

## Effect style

`Axios/Glass blur` — background blur 16 (pill currency, pill STEP, durasi video).

## Catatan

- 12 text style lama (DM Sans, Instrument Serif, Ritual Card) **sudah dihapus** 31 Oktober 2026 — tidak dipakai di Homepage. Panel text style kini hanya berisi 27 style `Axios/…` (+1 style lain bila ada).
- Variable collection lama `Axios / Botanical direction` dan `Axios / Warm Editorial` **sudah dihapus** (31 Oktober 2026) setelah Homepage dipasangi token baru.
- Warna sekali pakai di Homepage (sand 200–700, neutral/100) dimasukkan sebagai primitives agar pemasangan nanti tidak mengubah tampilan.
