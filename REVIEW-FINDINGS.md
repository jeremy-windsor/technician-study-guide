# Study Guide Review Findings

**Reviewed by:** Forge (ham radio expert subagent)  
**Date:** 2025-07-17  
**Scope:** Complete review of all 411 questions, answers, explanations, cram sheet, practice test, README, and study plan

---

## Executive Summary

**Overall quality: Excellent.** This is a well-written, accurate study guide. All 411 questions are present and accounted for across all 10 subelement files. Every correct answer letter matches the official JSON question pool. The explanations are overwhelmingly accurate, genuinely helpful for memorization, and written in a style that aids understanding rather than just rote learning.

A handful of issues were found — mostly minor formatting/typo issues and a few content corrections in the cram sheet. No critical factual errors were found in any of the 411 question explanations.

**Findings count:**
- Critical: 2 (cram sheet content errors that could cause wrong answers)
- Minor: 5 (typos, formatting, slight inaccuracies)
- Suggestion: 5 (improvements that would make an already-good guide better)

---

## Critical Findings

### CRIT-1: Cram Sheet — 10m Band Privileges Wrong Range for RTTY/Data
**File:** `CRAM-SHEET.md`  
**What's wrong:** The first 10m row shows:
```
| **10m** | 28.000–28.500 MHz | CW, RTTY, data | 200W PEP |
```
This incorrectly implies Technicians have RTTY and data privileges across the entire 28.000–28.500 MHz range.

**What it should be:**
```
| **10m** | 28.000–28.300 MHz | CW, RTTY, data | 200W PEP |
```
RTTY and data are only permitted in 28.000–28.300 MHz. Phone (SSB) privileges begin at 28.300 MHz. CW is available across the full 28.000–28.500 range, but the row as written tells students they can do RTTY up to 28.500, which is wrong.

**Severity:** Critical — could cause students to answer band privilege questions incorrectly on the exam.

---

### CRIT-2: Cram Sheet — Transmitting Without ID Exception is Wrong
**File:** `CRAM-SHEET.md`  
**What's wrong:** The License Rules table says:
```
| When can you transmit without ID | **Never (except brief tests)** |
```
This is doubly wrong:
1. **Brief tests DO require identification** — per T2A06, even test transmissions require station identification
2. **The actual exception is radio control model craft** — per T1D11, transmitting signals to control model craft is the ONLY time you can transmit without identifying

**What it should be:**
```
| When can you transmit without ID | **Only when controlling model craft** |
```

**Severity:** Critical — this teaches the wrong exception and could cause students to miss both T1D11 and T2A06.

---

## Minor Findings

### MINOR-1: T1-fcc-rules.md — T1B Group Header Typo
**File:** `subelements/T1-fcc-rules.md`  
**What's wrong:** Group T1B header reads:
```
## Group T1B — Frequency allocations; emission modes; spectrum sharing; transmissions near combband edges; power limits
```
"combband" should be "band" — the official topic is "transmissions near band edges."

**Severity:** Minor — typo, doesn't affect learning but looks unprofessional.

---

### MINOR-2: T1-fcc-rules.md — T1C Group Header Has Garbled Unicode
**File:** `subelements/T1-fcc-rules.md`  
**What's wrong:** Group T1C header reads:
```
## Group T1C — Licensing; call signs; classes of licensees;ும renewal; grace periods; vanity call signs
```
There's garbled Unicode text "ும" between the semicolon and "renewal."

**What it should be:**
```
## Group T1C — Licensing; call signs; classes of licensees; renewal; grace periods; vanity call signs
```

**Severity:** Minor — rendering artifact, doesn't affect content.

---

### MINOR-3: T0-safety.md — T0B09 Answer D Formatting Break
**File:** `subelements/T0-safety.md`  
**What's wrong:** In question T0B09, there's a blank line between answer C and answer D:
```markdown
- **C) The antenna could contact high-voltage power lines** ✅

- D) All these choices are correct
```
The blank line between C and D breaks the visual flow of the answer list. In some markdown renderers, this will appear as two separate lists rather than one continuous answer list.

**What it should be:**
```markdown
- **C) The antenna could contact high-voltage power lines** ✅
- D) All these choices are correct
```

**Severity:** Minor — visual formatting issue, answer D is still present and readable.

---

### MINOR-4: Cram Sheet — Encryption Exception Incomplete
**File:** `CRAM-SHEET.md`  
**What's wrong:** The License Rules table says:
```
| Encryption allowed when | **Only for satellite control** |
```
Per T1D03, the exception covers "control commands to space stations **or radio control craft**" — not just satellites.

**What it should be:**
```
| Encryption allowed when | **Only for space station or radio control craft commands** |
```

**Severity:** Minor — the satellite part is correct, but omitting radio control craft is an incomplete answer. The exam question (T1D03) specifically includes both.

---

### MINOR-5: Practice Test — Doesn't Match Real Exam Group Selection
**File:** `scripts/practice-test.py`  
**What's wrong:** The script uses `random.sample(pool, count)` from each subelement's entire question pool. The real exam selects exactly one question from each group within a subelement. This means the practice test could theoretically select 2 questions from group T1A and skip group T1B entirely.

**What it should do:** Select one question from each group:
```python
def generate_exam(questions):
    by_group = {}
    for q in questions:
        by_group.setdefault(q["group"], []).append(q)
    
    exam = []
    for group, pool in by_group.items():
        exam.append(random.choice(pool))
    
    random.shuffle(exam)
    return exam
```

**Severity:** Minor — the current approach still gives a valid practice experience (correct total count per subelement), but doesn't perfectly simulate real exam group distribution. In practice, the difference is small since groups within a subelement cover different topics.

---

## Suggestions

### SUGG-1: Add Question Count Verification to Each File Header
**What:** Each subelement file header shows the exam question count (e.g., "3 questions on the exam from a pool of 36"), but doesn't show the group count. Adding "drawn from X groups" would help students understand the exam structure.

**Example:**
```markdown
# T0 — Safety
*3 questions on the exam (one from each of 3 groups) from a pool of 36*
```

---

### SUGG-2: Cram Sheet — Add the SSB Sideband Convention Dividing Point
**What:** The Modulation Types table mentions "USB above 10 MHz, LSB below" but doesn't call out that this is a convention, not a rule. Adding a note about this being by convention would prevent confusion.

---

### SUGG-3: Cram Sheet — Add 1.25m National Calling Frequency
**What:** The Key Frequencies table lists calling frequencies for 2m, 70cm, and 6m but doesn't include 223.500 MHz (1.25m FM national calling frequency). While less commonly tested, it would make the table complete.

---

### SUGG-4: Add Pool Expiration Warning
**What:** The README mentions the 2022-2026 pool and notes the next pool starts July 1, 2026. Consider adding a prominent banner or note at the top of the README warning that this guide is only valid through June 30, 2026, since the repo will likely still be live after that date.

---

### SUGG-5: Schematic Figure References
**What:** Questions T6C02-T6C12 reference Figures T-1, T-2, and T-3 but the study guide doesn't include these figures. Students would need to find these diagrams elsewhere. Consider adding them to a `figures/` directory or linking to the NCVEC source.

---

## Verification Summary

### Question Completeness
| Subelement | Expected | Found | Status |
|:---:|:---:|:---:|:---:|
| T0 | 36 | 36 | ✅ |
| T1 | 67 | 67 | ✅ |
| T2 | 36 | 36 | ✅ |
| T3 | 34 | 34 | ✅ |
| T4 | 24 | 24 | ✅ |
| T5 | 52 | 52 | ✅ |
| T6 | 47 | 47 | ✅ |
| T7 | 43 | 43 | ✅ |
| T8 | 48 | 48 | ✅ |
| T9 | 24 | 24 | ✅ |
| **Total** | **411** | **411** | **✅** |

### Answer Accuracy
All 411 correct answer letters match the official JSON question pool. Zero mismatches.

### Explanation Accuracy
All 411 explanations reviewed for factual correctness:
- **0 factual errors found** in any question explanation
- Math calculations (Ohm's Law, power, wavelength, decibels) all verified correct
- FCC rule references accurate
- Component descriptions accurate
- Propagation descriptions accurate
- Safety guidance accurate

### Exam Distribution (Practice Test)
| Subelement | Script | Real Exam | Match |
|:---:|:---:|:---:|:---:|
| T0 | 3 | 3 | ✅ |
| T1 | 6 | 6 | ✅ |
| T2 | 3 | 3 | ✅ |
| T3 | 3 | 3 | ✅ |
| T4 | 2 | 2 | ✅ |
| T5 | 4 | 4 | ✅ |
| T6 | 4 | 4 | ✅ |
| T7 | 4 | 4 | ✅ |
| T8 | 4 | 4 | ✅ |
| T9 | 2 | 2 | ✅ |
| **Total** | **35** | **35** | **✅** |

### Unicode/Encoding
The JSON pool uses smart quotes (U+2018/U+2019/U+201C/U+201D) and a private-use multiplication symbol (U+F0B4). The study guide normalizes these to straight ASCII quotes and proper Unicode × (U+00D7). This is actually an improvement for terminal/plaintext rendering. Not a bug.

### Files Reviewed
- [x] `subelements/T0-safety.md` — 36 questions ✅
- [x] `subelements/T1-fcc-rules.md` — 67 questions ✅
- [x] `subelements/T2-operating-procedures.md` — 36 questions ✅
- [x] `subelements/T3-radio-waves.md` — 34 questions ✅
- [x] `subelements/T4-amateur-practices.md` — 24 questions ✅
- [x] `subelements/T5-electrical-principles.md` — 52 questions ✅
- [x] `subelements/T6-components.md` — 47 questions ✅
- [x] `subelements/T7-practical-circuits.md` — 43 questions ✅
- [x] `subelements/T8-signals-emissions.md` — 48 questions ✅
- [x] `subelements/T9-antennas-feedlines.md` — 24 questions ✅
- [x] `CRAM-SHEET.md` ✅
- [x] `scripts/practice-test.py` ✅
- [x] `README.md` ✅
- [x] `STUDY-PLAN.md` ✅
- [x] `pools/2022-2026/questions.json` ✅

---

*Note: T7D05 is absent from the question pool (T7D goes T7D01-T7D04, T7D06-T7D11). This is correct — the NCVEC pool simply doesn't have a T7D05. The study guide correctly reflects this.*
