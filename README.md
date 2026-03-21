# Amateur Radio Technician Exam Study Guide

> 📅 **Two pools available:** Study guide content covers the **2022–2026 pool** (valid through June 30, 2026).
> The **[2026–2030 pool](pools/2026-2030/)** (409 questions, effective July 1, 2026) is available in the PWA study app — it auto-selects the correct pool based on today's date.

Pass the FCC Technician class license exam. All questions, all answers, explained.

## What's Inside

- **411 real exam questions** (2022–2026 pool) + **409 questions** (2026–2030 pool) with correct answers
- **10 study sections** organized by topic (subelements T1–T0)
- **Cram sheet** for last-minute review
- **Practice test script** to simulate the real exam
- **7-day study plan** to get you from zero to licensed

## The Exam

| | |
|---|---|
| **Questions** | 35 multiple choice |
| **Passing** | 26 correct (74%) |
| **Time** | No time limit |
| **Fee** | $35 (ARRL VEC) |
| **Where** | Find a session at [arrl.org/find-an-amateur-radio-license-exam-session](http://www.arrl.org/find-an-amateur-radio-license-exam-session) |

The exam pulls from a **fixed public question pool** — every possible question and answer is published. This guide covers all of them.

## Question Pools

| Pool | Effective | Expires | Questions | Status |
|------|-----------|---------|-----------|--------|
| [2022–2026](pools/2022-2026/) | July 1, 2022 | June 30, 2026 | 411 | Expires soon |
| [2026–2030](pools/2026-2030/) | July 1, 2026 | June 30, 2030 | 409 | Active July 2026 |

The **PWA study app** auto-selects the correct pool based on today's date, with a manual override if you want to study ahead.

## How to Study

### Quick Path (7 days)

See [STUDY-PLAN.md](STUDY-PLAN.md) for the full day-by-day plan.

| Day | Topic | Section |
|-----|-------|---------|
| 1 | FCC Rules | [T1](subelements/T1-fcc-rules.md) |
| 2 | Operating & Radio Waves | [T2](subelements/T2-operating-procedures.md), [T3](subelements/T3-radio-waves.md) |
| 3 | Station Setup | [T4](subelements/T4-amateur-practices.md) |
| 4 | Electrical Theory | [T5](subelements/T5-electrical-principles.md) |
| 5 | Components & Circuits | [T6](subelements/T6-components.md), [T7](subelements/T7-practical-circuits.md) |
| 6 | Signals, Antennas, Safety | [T8](subelements/T8-signals-emissions.md), [T9](subelements/T9-antennas-feedlines.md), [T0](subelements/T0-safety.md) |
| 7 | Review + Practice Test | [Cram Sheet](CRAM-SHEET.md) + `python3 scripts/practice-test.py` |

### Study Sections

Each subelement has three files:

- **`T{N}-{name}.md`** — Study guide: a narrative walkthrough of the topic, written for learning
- **`T{N}-{name}.mp3`** — Audio version of the study guide (listen while driving, working out, etc.)
- **`T{N}-{name}-questions.md`** — Exam question bank: every question with the correct answer highlighted and explained

Start with the study guide to learn the material, then drill the question bank to lock in the answers.

| Section | Topic | Study Guide | Question Bank | Exam Qs | Pool Size |
|---------|-------|-------------|---------------|:-:|:-:|
| T1 | FCC Rules | [guide](subelements/T1-fcc-rules.md) | [questions](subelements/T1-fcc-rules-questions.md) | 6 | 67 |
| T2 | Operating Procedures | [guide](subelements/T2-operating-procedures.md) | [questions](subelements/T2-operating-procedures-questions.md) | 3 | 36 |
| T3 | Radio Wave Propagation | [guide](subelements/T3-radio-waves.md) | [questions](subelements/T3-radio-waves-questions.md) | 3 | 34 |
| T4 | Amateur Radio Practices | [guide](subelements/T4-amateur-practices.md) | [questions](subelements/T4-amateur-practices-questions.md) | 2 | 24 |
| T5 | Electrical Principles | [guide](subelements/T5-electrical-principles.md) | [questions](subelements/T5-electrical-principles-questions.md) | 4 | 52 |
| T6 | Components | [guide](subelements/T6-components.md) | [questions](subelements/T6-components-questions.md) | 4 | 47 |
| T7 | Practical Circuits | [guide](subelements/T7-practical-circuits.md) | [questions](subelements/T7-practical-circuits-questions.md) | 4 | 43 |
| T8 | Signals & Emissions | [guide](subelements/T8-signals-emissions.md) | [questions](subelements/T8-signals-emissions-questions.md) | 4 | 48 |
| T9 | Antennas & Feed Lines | [guide](subelements/T9-antennas-feedlines.md) | [questions](subelements/T9-antennas-feedlines-questions.md) | 2 | 24 |
| T0 | Safety | [guide](subelements/T0-safety.md) | [questions](subelements/T0-safety-questions.md) | 3 | 36 |
| | **Total** | | | **35** | **411** |

### Practice Test

```bash
python3 scripts/practice-test.py
```

Generates a random 35-question exam from the real pool, scores it, and shows which areas need work.

### Audio Study Guide 🎧

Every section and the cram sheet are available as MP3 audio — study while driving, working out, or doing chores.

| File | Duration |
|------|----------|
| `subelements/T1-fcc-rules.mp3` | 52 min |
| `subelements/T2-operating-procedures.mp3` | 24 min |
| `subelements/T3-radio-waves.mp3` | 24 min |
| `subelements/T4-amateur-practices.mp3` | 17 min |
| `subelements/T5-electrical-principles.mp3` | 29 min |
| `subelements/T6-components.mp3` | 26 min |
| `subelements/T7-practical-circuits.mp3` | 29 min |
| `subelements/T8-signals-emissions.mp3` | 33 min |
| `subelements/T9-antennas-feedlines.mp3` | 17 min |
| `subelements/T0-safety.mp3` | 27 min |
| `CRAM-SHEET.mp3` | 9 min |
| **Total** | **4h 47m** |

Each MP3 is the audio version of the corresponding study guide narrative. Pronunciation of ham radio acronyms follows standard conventions (see `tts/pronunciation.md`).

### Cram Sheet

[CRAM-SHEET.md](CRAM-SHEET.md) — one page of key facts, formulas, frequencies, and power limits. Read this the morning of your exam.

## Regenerating Audio

Audio is generated via [Kokoro](https://github.com/remsky/Kokoro-FastAPI) (OpenAI-compatible TTS). Requires Python 3.6+, `curl`, `ffmpeg`.

```bash
export SPEECH_URL="https://your-server:8100/v1/audio/speech"
python3 tts/generate-audio.py --all --voice af_heart
```

Pronunciation rules are in `tts/pronunciation.md`. Use `--dry-run` to preview spoken text.

## Updating for a New Pool

1. Download the new pool PDF from [ncvec.org](https://ncvec.org/index.php/amateur-question-pools)
2. Parse into `pools/YYYY-YYYY/questions.json`
3. Regenerate subelement files and update practice test pool path
4. Update dates in this README
5. Regenerate audio with the TTS pipeline above

## Question Pool Source

All questions are from the official NCVEC Technician Class Question Pool, released into the public domain.

- **Source:** [ncvec.org](https://ncvec.org/index.php/amateur-question-pools)
- **Current pool:** 2022–2026 (effective July 1, 2022 – June 30, 2026)
- **Next pool:** 2026–2030 (effective July 1, 2026)

## Interactive Study App 📱

The [`apps/study-app/`](apps/study-app/) directory contains a browser-based PWA for active practice:

- **Flashcard mode** — flip through all 411 questions with instant answer reveal
- **Practice exam mode** — timed 35-question exams drawn randomly from the pool
- **Progress tracking** — remembers which questions you've gotten wrong
- **Offline capable** — works without internet after first load
- **Installable** — add to Home Screen on mobile or install from desktop Chrome/Edge

**[→ Open the Study App](https://isriam.github.io/technician-study-guide/apps/study-app/)** — works on phone, tablet, or desktop. Add to home screen for offline access.

## License

Question pool content is public domain (NCVEC). Study guide explanations and scripts are MIT licensed.
