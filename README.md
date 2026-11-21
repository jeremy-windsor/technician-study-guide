# Amateur Radio Technician Exam Study Guide

Pass the FCC Technician class license exam. Every question in the official pool, answered and explained, with study guides, audio, and a study app.

**[Open the Study App](https://jeremy-windsor.github.io/technician-study-guide/apps/study-app/)**: flashcards, timed practice exams, drills, weak-area review, and progress tracking. Works offline and installs to your phone's home screen.

## The Exam

| | |
|---|---|
| **Questions** | 35 multiple choice, one from each topic group in the pool |
| **Passing** | 26 correct (74%) |
| **Prerequisite** | None |
| **Fee** | $35 FCC application fee plus a session fee of about $15 |
| **Where** | [Find an exam session](http://www.arrl.org/find-an-amateur-radio-license-exam-session) |
| **Question pool** | [2026–2030 pool](pools/2026-2030/), 409 questions, valid July 1, 2026 – June 30, 2030, with NCVEC's February 19, 2026 errata ([source](https://www.ncvec.org/index.php/2026-2030-technician-question-pool), public domain) |

Every possible question and answer is published, and this guide covers all of them.

## Study Materials

Each section has a narrative study guide, a question bank (every question with the correct answer and an explanation), and an MP3 of each.

| Section | Topic | Study guide | Question bank | Audio (guide + questions) | Exam Qs | Pool |
|---|---|---|---|---|:-:|:-:|
| T1 | Commission's Rules | [guide](subelements/T1-fcc-rules.md) | [questions](subelements/T1-fcc-rules-questions.md) | [16 min](subelements/T1-fcc-rules.mp3) + [54 min](subelements/T1-fcc-rules-questions.mp3) | 6 | 68 |
| T2 | Operating Procedures | [guide](subelements/T2-operating-procedures.md) | [questions](subelements/T2-operating-procedures-questions.md) | [10 min](subelements/T2-operating-procedures.mp3) + [27 min](subelements/T2-operating-procedures-questions.mp3) | 3 | 37 |
| T3 | Radio Wave Propagation | [guide](subelements/T3-radio-waves.md) | [questions](subelements/T3-radio-waves-questions.md) | [10 min](subelements/T3-radio-waves.mp3) + [25 min](subelements/T3-radio-waves-questions.mp3) | 3 | 35 |
| T4 | Amateur Radio Practices | [guide](subelements/T4-amateur-practices.md) | [questions](subelements/T4-amateur-practices-questions.md) | [8 min](subelements/T4-amateur-practices.mp3) + [17 min](subelements/T4-amateur-practices-questions.mp3) | 2 | 23 |
| T5 | Electrical Principles | [guide](subelements/T5-electrical-principles.md) | [questions](subelements/T5-electrical-principles-questions.md) | [8 min](subelements/T5-electrical-principles.mp3) + [27 min](subelements/T5-electrical-principles-questions.mp3) | 4 | 50 |
| T6 | Electronic and Electrical Components | [guide](subelements/T6-components.md) | [questions](subelements/T6-components-questions.md) | [8 min](subelements/T6-components.mp3) + [26 min](subelements/T6-components-questions.mp3) | 4 | 46 |
| T7 | Practical Circuits | [guide](subelements/T7-practical-circuits.md) | [questions](subelements/T7-practical-circuits-questions.md) | [11 min](subelements/T7-practical-circuits.mp3) + [29 min](subelements/T7-practical-circuits-questions.mp3) | 4 | 44 |
| T8 | Signals and Emissions | [guide](subelements/T8-signals-emissions.md) | [questions](subelements/T8-signals-emissions-questions.md) | [11 min](subelements/T8-signals-emissions.mp3) + [32 min](subelements/T8-signals-emissions-questions.mp3) | 4 | 47 |
| T9 | Antennas and Feed Lines | [guide](subelements/T9-antennas-feedlines.md) | [questions](subelements/T9-antennas-feedlines-questions.md) | [9 min](subelements/T9-antennas-feedlines.mp3) + [16 min](subelements/T9-antennas-feedlines-questions.mp3) | 2 | 23 |
| T0 | Safety | [guide](subelements/T0-safety.md) | [questions](subelements/T0-safety-questions.md) | [11 min](subelements/T0-safety.mp3) + [26 min](subelements/T0-safety-questions.mp3) | 3 | 36 |
| | **Total** | | | **6h 22m** | **35** | **409** |

Also included:

- **[Cram Sheet](CRAM-SHEET.md)** ([audio](CRAM-SHEET.mp3), 7 min): key facts, formulas, frequencies, and power limits on one page. Read it the morning of the exam.
- **[Study Plan](STUDY-PLAN.md)**: a 7-day schedule.
- **[Figures](figures/)**: the three official schematic diagrams (T-1, T-2, T-3) used by the T6 schematic questions. The app shows them with those questions.

## How to Study

1. Read each study guide (or listen to it), then drill its question bank.
2. Follow the [7-day plan](STUDY-PLAN.md): rules (T1), operating and propagation (T2, T3), station setup (T4), electrical theory (T5), components and circuits (T6, T7), then signals, antennas, and safety (T8, T9, T0). Spend the last day on the cram sheet and practice exams.
3. Take practice exams every session, in the app or from the command line:

   ```bash
   python3 scripts/practice-test.py          # one question per group, like the real exam
   python3 scripts/practice-test.py --drill  # 35 random questions from the whole pool
   ```

Tips: learn your privileges and the ID rules (T1) first, know the three schematic figures, and use the app's formula button for a quick reference.

## Maintaining

**New question pool:** download it from [NCVEC](https://ncvec.org/index.php/amateur-question-pools), parse it into `pools/YYYY-YYYY/questions.json` (see `scripts/parse-pool-2026-2030.py`), regenerate the question banks with `scripts/gen-question-files.py`, update the pool in `scripts/practice-test.py`, `apps/study-app/app.js`, and `apps/study-app/sw.js`, update the dates here, and regenerate the audio.

**Audio:** generated with a self-hosted [Open Speech](https://github.com/jeremy-windsor/open-speech) server, voice "will" (`am_puck(1)+am_liam(1)+am_onyx(0.5)` at 1.1× speed), as MP3. Text is prepared following the narration rules and vocabulary in [`tts/pronunciation.txt`](tts/pronunciation.txt). The cram sheet audio is read from [`tts/CRAM-SHEET-audio.md`](tts/CRAM-SHEET-audio.md), so keep it in agreement with `CRAM-SHEET.md`.

## License

Question pool content is public domain (NCVEC). Study guide explanations and scripts are MIT licensed.
