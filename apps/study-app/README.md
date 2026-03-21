# Ham Radio Technician Study App

An offline-capable PWA for studying the FCC Technician Class (Element 2) amateur radio exam.

## Features

- **411 questions** — the complete 2022–2026 FCC question pool
- **Flashcard mode** — flip through questions one at a time with instant answer reveal
- **Practice exam mode** — timed 35-question exams drawn randomly from the pool (passing = 26/35)
- **Progress tracking** — per-question correct/incorrect counts stored in `localStorage`
- **Weak-spot focus** — filter to questions you've gotten wrong most
- **Offline support** — service worker caches the app after first load; no internet required
- **Installable PWA** — "Add to Home Screen" on Android/iOS or install from desktop Chrome/Edge

## Usage

Open `index.html` directly in a browser — no build step, no server required. Works from the filesystem or served over HTTP/HTTPS.

For GitHub Pages, the app is available at:
`https://<user>.github.io/technician-study-guide/apps/study-app/`

## Files

| File | Purpose |
|------|---------|
| `index.html` | Single-file app (HTML + CSS + JS) |
| `questions.js` | All 411 FCC Element 2 questions as a JS array |
| `sw.js` | Service worker for offline caching |
| `manifest.json` | PWA manifest (name, icons, display mode) |
| `icon-192.png` | App icon (192×192) |
| `icon-512.png` | App icon (512×512) |

## Question Pool

Questions sourced from the [ARRL 2022–2026 Technician pool](https://www.arrl.org/question-pools). Valid through **June 30, 2026**.
