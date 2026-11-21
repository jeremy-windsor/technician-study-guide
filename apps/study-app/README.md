# Ham Radio Technician Study App

An offline-capable PWA for studying the FCC Technician Class (Element 2) amateur radio exam.

## Features

- **409 questions** — the complete NCVEC 2026–2030 Technician question pool
- **Flashcard mode** — flip through questions one at a time with instant answer reveal
- **Practice exam mode** — timed 35-question exams with one random question from each question group, like the real exam (passing = 26/35)
- **Drill mode** — 35 questions drawn at random from the whole pool, ignoring groups
- **Progress tracking** — per-question correct/incorrect counts stored in `localStorage`
- **Weak-spot focus** — filter to questions you've gotten wrong most
- **Offline support** — service worker caches the app after first load; no internet required
- **Installable PWA** — "Add to Home Screen" on Android/iOS or install from desktop Chrome/Edge

## Usage

No build step. The app must be served over HTTP(S) — it loads the question pool with `fetch()` and registers a service worker, and browsers block both on `file://`, so opening `index.html` directly from disk will not load questions.

For local use, serve the **repository root** (the app reads `../../pools/` and `../../figures/`), for example:

```bash
python3 -m http.server 8000
# then open http://localhost:8000/apps/study-app/
```

For GitHub Pages, the app is available at:
`https://<user>.github.io/technician-study-guide/apps/study-app/`

## Files

| File | Purpose |
|------|---------|
| `index.html` | App markup |
| `app.js` | App logic (flashcards, exams, progress) |
| `styles.css` | App styles |
| `sw.js` | Service worker for offline caching |
| `manifest.json` | PWA manifest (name, icons, display mode) |
| `icon-192.png` | App icon (192×192) |
| `icon-512.png` | App icon (512×512) |

Questions are not bundled in this folder. The app loads them at runtime from `../../pools/2026-2030/questions.json`, and the schematic figures from `../../figures/`.

## Question Pool

Questions come from the [NCVEC 2026–2030 Technician question pool](https://ncvec.org/index.php/2026-2030-technician-question-pool) (public domain), including the February 19, 2026 errata. Valid **July 1, 2026 – June 30, 2030**.
