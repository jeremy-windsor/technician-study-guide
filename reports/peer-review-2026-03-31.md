# Peer Review: 2026–2030 Technician Study Guide
**Reviewer:** Senior Ham Radio Instructor / Content Editor (AI)  
**Date:** March 31, 2026  
**Pool:** 2026–2030 Technician Class Question Pool (409 questions)  
**Files Reviewed:** All 10 subelement study guides (T0–T9)

---

## Overall Grade: **A-**

This is an impressively thorough and well-written study guide. The conversational tone makes complex material accessible without dumbing it down. All 5 newly added questions, all 7 correct-answer changes, and all 27 topic replacements appear to be properly addressed in the guide content. The factual accuracy is very high. The issues found are mostly minor wording mismatches and a few places where precision could be improved.

---

## Issues Found

### ISSUE 1 — Wrong keyword for repeater monitoring
- **File:** `T2-operating-procedures.md`, line ~25
- **What's wrong:** The study guide says: *"say your call sign followed by the word 'monitoring.'"* However, the correct answer for T2A09 is: *"The station's call sign followed by the word 'listening'"*. The pool answer specifically says **"listening"**, not "monitoring."
- **Severity:** **CRITICAL** — A student memorizing the guide's keyword would select the wrong answer on the exam.
- **Suggested fix:** Change `"monitoring"` to `"listening"` throughout. The sentence should read: *"say your call sign followed by the word 'listening.'"*

---

### ISSUE 2 — "Distorted" vs. "drops out" for FM over-deviation
- **File:** `T2-operating-procedures.md`, line ~61
- **What's wrong:** The study guide says: *"If your FM transmission audio is distorted on voice peaks…"* However, T2B05 asks: *"Which of the following would cause your FM transmission audio to **drop out** on voice peaks?"* The correct answer is C: "You are talking too loudly." While the underlying concept (over-deviation from talking too loudly) is the same, the pool uses the specific term "drop out" — not "distorted." A student who only read the guide might not connect "distorted" with "drop out."
- **Severity:** **HIGH** — The correct answer choice is still clearly identifiable, but the guide's wording doesn't match the exam's specific phrasing, which could cause confusion.
- **Suggested fix:** Update to: *"If your FM transmission audio drops out on voice peaks, you're probably talking too loudly and over-deviating the signal."* Optionally note that over-deviation can cause both audio dropout and distortion.

---

### ISSUE 3 — Missing "Group D" terminology for call sign format
- **File:** `T1-fcc-rules.md`, line ~23
- **What's wrong:** The study guide describes the Technician call sign format as "two-by-three" (e.g., KF1XXX) but T1C05 now asks: *"Which of the following is a valid **Group D** call sign format for Technician class?"* The term "Group D" does not appear anywhere in the study guide. A student encountering "Group D" on the exam might not know it means two-by-three.
- **Severity:** **HIGH** — New exam terminology not introduced in the study material.
- **Suggested fix:** Add a parenthetical: *"A valid Technician class call sign follows a two-by-three format — also called **Group D** — that's a two-letter prefix, one numeral, and a three-letter suffix, like KF1XXX."*

---

### ISSUE 4 — SSB bandwidth: "3 kHz" vs. "2400 Hz" apparent contradiction
- **File:** `T8-signals-emissions.md` (line ~21) vs. `T4-amateur-practices.md` (line ~51)
- **What's wrong:** T8 says *"SSB voice occupies approximately 3 kilohertz."* T4 says *"The best filter bandwidth for SSB reception is 2400 hertz. This matches the bandwidth of an SSB voice signal."* These statements appear to contradict each other — is SSB bandwidth 3 kHz or 2.4 kHz? The pool answer for T8A08 is "3 kHz" (signal bandwidth), and T4B10 correct answer is "2400 Hz" (optimal filter bandwidth). Both are technically correct for their context — signal bandwidth is ~3 kHz, optimal receive filter is 2.4 kHz — but the T4 guide explicitly says "This matches the bandwidth of an SSB voice signal" when referring to 2400 Hz, which contradicts the 3 kHz figure in T8.
- **Severity:** **MEDIUM** — Could confuse a careful student who reads both sections. The pool has two different "correct" numbers for what appears to be the same concept.
- **Suggested fix:** In T4, change to: *"The best filter bandwidth for SSB reception is 2400 hertz. This is slightly narrower than the ~3 kHz signal bandwidth, providing the best balance between passing enough voice audio and rejecting noise."* This resolves the contradiction by explaining the filter is intentionally slightly narrower than the full signal bandwidth.

---

### ISSUE 5 — T0A01 wording doesn't mention "lacks internal protection circuitry"
- **File:** `T0-safety.md`, line ~1–3
- **What's wrong:** The study guide discusses 12-volt battery hazards but doesn't mention the new qualifier in T0A01: *"a 12-volt storage battery **that lacks internal protection circuitry**."* The new wording specifically calls out unprotected batteries. The guide's explanation is still correct but doesn't prepare the student for the more specific question framing.
- **Severity:** **LOW** — The correct answer (B: shorting terminals causes burns/fire/explosion) is still clearly the right choice regardless. The qualifier is in the question stem, not the answer choices.
- **Suggested fix:** Add a brief mention: *"Even something as simple as a 12-volt storage battery — especially one that lacks internal protection circuitry — can be dangerous…"*

---

### ISSUE 6 — T5A05 coverage gap: "difference in voltage causes electron flow"
- **File:** `T5-electrical-principles.md`, line ~5
- **What's wrong:** T5A05 asks: *"A difference in which of the following causes electron flow?"* (Answer: Voltage). The study guide says *"Voltage is the electrical force that pushes those electrons through the circuit"* but never explicitly states that it is a **difference** in voltage (potential difference) that causes electron flow. The concept is implied but not directly stated.
- **Severity:** **LOW** — Most students would still select "Voltage" as the correct answer since the guide clearly associates voltage with causing electron flow.
- **Suggested fix:** Add: *"It's actually a difference in voltage — a potential difference — between two points that causes electrons to flow."*

---

### ISSUE 7 — T6C12 not explicitly covered
- **File:** `T6-components.md`
- **What's wrong:** T6C12 asks: *"Which of the following is accurately represented in electrical schematics?"* (Answer: C = "Component connections"). The study guide says schematics show *"how components are electrically connected — not their physical size, shape, or wire lengths."* This conveys the right idea but doesn't use the exact phrase "component connections," which is the correct answer choice.
- **Severity:** **LOW** — The guide's explanation leads clearly to the right answer. It explicitly says schematics show connections, not physical attributes.
- **Suggested fix:** Consider adding: *"What schematics accurately represent is the component connections — the electrical relationships between parts."*

---

### ISSUE 8 — T2A05 question file explanation mismatch (questions file, not study guide)
- **File:** `T2-operating-procedures-questions.md`, under T2A05
- **What's wrong:** The explanation paragraph after T2A05 ("How should you respond to a station calling CQ?") discusses simplex channels instead of how to respond to CQ. The explanation belongs to a different question — it appears to be a copy/paste error where the T2A09 or T2A11 explanation was placed under T2A05.
- **Severity:** **HIGH** — A student relying on the question-by-question explanations gets wrong guidance for this question.
- **Suggested fix:** Replace the T2A05 explanation with: *"When answering someone calling CQ, transmit their call sign first, then your call sign. This tells the calling station who is responding and who you are."*

---

### ISSUE 9 — No mention of "unprotected battery" context for T0A10
- **File:** `T0-safety.md`, battery safety section
- **What's wrong:** T0A10 now asks about *"rapidly charging or discharging an **unprotected** battery"* — the word "unprotected" was added. The study guide discusses rapid charging hazards but doesn't use this specific qualifier.
- **Severity:** **LOW** — Same situation as Issue 5. The answer ("Overheating or out-gassing") is unaffected.
- **Suggested fix:** Add "unprotected" to align with the new question wording: *"Charging or discharging an unprotected battery too quickly creates a serious hazard…"*

---

### ISSUE 10 — Beacon definition retained but no longer tested
- **File:** `T1-fcc-rules.md`, line ~27
- **What's wrong:** The study guide retains the full Part 97 definition of a beacon: *"an amateur station transmitting communications for the purposes of observing propagation…"* This definition was part of old T1A06, which has been replaced with a question about HF beacon frequencies (28.200–28.300 MHz). While the definition is factually correct and doesn't hurt, it takes up space that could be used for other tested material. The new question doesn't test the definition — it tests the frequency range.
- **Severity:** **LOW** — Extra correct information is never harmful, but it could be trimmed for efficiency.
- **Suggested fix:** Optional: Shorten to focus on the frequency range since that's what's tested. Keep the definition as a one-line aside if desired.

---

## Coverage Verification (20 Random Questions)

I sampled 20 questions across all subelements and verified that the study guide provides sufficient explanation for a student to answer each correctly:

| Question | Topic | Covered? | Notes |
|----------|-------|----------|-------|
| T0A02 | Electrical current body hazards | ✅ Yes | All three hazards explicitly listed |
| T0A08 | Fuse installation location | ✅ Yes | "Series with the hot conductor only" |
| T1C06 | Operating from vessel | ✅ Yes | Covered under international waters section |
| T1C09 | Grace period for renewal | ✅ Yes | "Two-year grace period" |
| T1D02 | One-way transmission prohibition | ✅ Yes | Broadcasting clearly identified as prohibited |
| T2A07 | Repeater offset definition | ✅ Yes | First concept introduced in T2 |
| T2A09 | Indicating you're listening | ⚠️ Partial | Says "monitoring" instead of "listening" (Issue #1) |
| T3A06 | Picket fencing | ✅ Yes | "Rapid flutter on mobile signals" |
| T3C11 | Radio horizon beyond visual | ✅ Yes | Atmospheric refraction explained |
| T4B07 | DMR code plug | ✅ Yes | "Configuration data loaded onto your radio" |
| T5A03 | Term for electron flow | ✅ Yes | "Current" clearly defined |
| T5C04 | Unit of inductance | ✅ Yes | "Henry" explicitly stated |
| T6A02 | Adjustable volume control | ✅ Yes | Potentiometer well explained |
| T6A06 | Stores energy in magnetic field | ✅ Yes | Inductor clearly identified |
| T7B03 | Causes of RFI | ✅ Yes | All three causes listed |
| T7B04 | Low RF power output cause | ✅ Yes | High SWR explained as cause |
| T8C09 | Protocol without radio initiation | ✅ Yes | EchoLink described correctly |
| T8D04 | NTSC meaning | ✅ Yes | "Analog fast-scan color TV signal" |
| T9A01 | Beam antenna definition | ✅ Yes | "Concentrates signals in one direction" |
| T9B12 | SWR definition | ✅ Yes | "Measure of how well a load is matched" |

**Coverage Rate: 19/20 fully covered, 1/20 partially covered (wrong keyword)**

---

## Factual Accuracy Audit

### Frequencies Verified ✅
- 28.300–28.500 MHz (Tech phone on 10m) — Correct
- 28.200–28.300 MHz (HF beacon sub-band) — Correct  
- 146.520 MHz (2m FM simplex calling) — Correct
- 52.525 MHz (6m FM simplex calling) — Correct
- 50.0–50.1 MHz (6m CW only) — Correct
- 144.0–144.1 MHz (2m CW only) — Correct

### Power Limits Verified ✅
- 200W PEP for Technician HF segments — Correct
- 1500W PEP for Technician above 30 MHz — Correct

### Formulas Verified ✅
- P = I × E — Correct
- I = E / R — Correct
- Wavelength = 300 / frequency(MHz) — Correct
- All Ohm's Law numerical examples checked — All correct

### Decibel Rules Verified ✅
- +3 dB = double power — Correct
- +10 dB = 10× power — Correct
- 12W → 3W = -6 dB — Correct

### Part 97 References Verified ✅
- License term: 10 years — Correct
- Grace period: 2 years — Correct  
- Renewal window: 90 days — Correct
- Control operator requirement: Always — Correct
- Station ID: Every 10 minutes + end — Correct
- Low-power ID exemption: Below 0.1 watt — Correct

---

## Stale Content Check

No references to "2022–2026 pool" or outdated pool identifiers found. The study guide appears to have been written fresh for the 2026–2030 pool rather than edited from an older version. **No stale content detected.**

---

## Writing Quality Assessment

### Strengths
- **Excellent conversational tone** — reads like a knowledgeable instructor explaining concepts
- **Strong memory aids** — "QRM: M for man-made," "black equals hot," analogies throughout
- **Good exam awareness** — explicitly calls out common traps and distractors
- **Logical flow** — concepts build on each other within each section
- **Practical relevance** — connects abstract rules to real-world radio operation

### Minor Writing Issues
- Some sections could use subheadings for easier scanning (T1 is quite long)
- The T8 section on digital modes could benefit from a summary table comparing FT8, DMR, APRS, Packet
- A few sections repeat information covered in the T1 regulatory section (e.g., RACES is defined in both T1 and T2) — this could be intentional for reinforcement but may confuse students about which section to study

---

## Summary of Issues by Severity

| Severity | Count | Issues |
|----------|-------|--------|
| CRITICAL | 1 | #1 (monitoring vs. listening) |
| HIGH | 2 | #2 (distorted vs. drops out), #3 (Group D term missing), #8 (question file explanation mismatch) |
| MEDIUM | 1 | #4 (SSB bandwidth contradiction) |
| LOW | 5 | #5, #6, #7, #9, #10 |
| **Total** | **10** | |

---

## Recommendations

1. **Fix Issue #1 immediately** — wrong keyword will cause exam failures
2. **Fix Issue #3 soon** — "Group D" is new pool terminology students need
3. **Fix Issue #8** — question file explanation is flat-out wrong for T2A05
4. **Clarify Issue #4** — resolve the 3 kHz vs. 2400 Hz apparent contradiction
5. **Consider adding a quick-reference frequency table** — consolidate all the frequencies students need to memorize into one table
6. **Consider adding a "New for 2026–2030" callout box** — flag the 5 added and 7 changed-answer questions so students coming from the old pool know what's different

---

*Review completed March 31, 2026. All 409 questions in the 2026–2030 pool were available for cross-reference. Twenty questions were sampled for detailed coverage verification. All 10 study guide files were read in full.*
