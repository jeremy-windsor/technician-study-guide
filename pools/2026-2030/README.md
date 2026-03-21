# 2026–2030 Technician Question Pool

**Source:** [NCVEC Question Pool Committee](https://ncvec.org/index.php/2026-2030-technician-question-pool)
**Effective:** July 1, 2026 – June 30, 2030
**Questions:** 409
**Exam draws:** 35 questions per exam
**Errata:** February 19, 2026 (T1C01, T5A05, T7A09, T0A10 updated)

## Files

- `questions.json` — Parsed question pool in structured JSON format
- Source PDF: [NCVEC 2026-2030 Pool (Feb 19 2026 errata)](https://ncvec.org/downloads/2026-2030%20Technician%20Pool%20and%20Syllabus%20Public%20Release%20Feb%2019%202026.pdf)

## JSON Structure

```json
{
  "pool": "2026-2030",
  "effective": "2026-07-01",
  "expires": "2030-06-30",
  "total": 409,
  "subelements": { ... },
  "questions": [
    {
      "id": "T1A01",
      "subelement": "T1",
      "group": "T1A",
      "question": "[97.1] Which of the following...",
      "correct": "C",
      "answers": { "A": "...", "B": "...", "C": "...", "D": "..." }
    }
  ]
}
```

## Subelement Question Counts

| Subelement | Topic | Pool | Exam |
|------------|-------|------|------|
| T1 | Commission's Rules | 68 | 6 |
| T2 | Operating Procedures | 37 | 3 |
| T3 | Radio Wave Characteristics | 35 | 3 |
| T4 | Amateur Radio Practices | 23 | 2 |
| T5 | Electrical Principles | 50 | 4 |
| T6 | Electronic Components | 46 | 4 |
| T7 | Practical Circuits | 44 | 4 |
| T8 | Signals and Emissions | 47 | 4 |
| T9 | Antennas and Feed Lines | 23 | 2 |
| T0 | Electrical and RF Safety | 36 | 3 |
| **Total** | | **409** | **35** |

## Generation

Parsed from the official NCVEC PDF using `scripts/parse-pool-2026-2030.py`.
