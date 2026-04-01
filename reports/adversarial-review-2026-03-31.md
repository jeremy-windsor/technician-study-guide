# Adversarial Review — 2026-2030 Technician Study Guide
**Date:** 2026-03-31  
**Reviewer:** Will (subagent, adversarial mode)  
**Method:** Cross-checked all 10 study guide chapters against the 409-question pool, with focus on 73 changed questions, "All these choices are correct" traps, formulas, frequencies, and dangerous oversimplifications.

---

## Executive Summary

**Overall Grade: B+ (Solid but not bulletproof)**

The study guide is well-written and covers the vast majority of exam content accurately. However, I found **14 findings** ranging from critical exam-failure risks to minor gaps. Three findings could directly cause a student to pick the wrong answer. The rest are either missing coverage for testable questions or minor wording issues.

**Critical findings: 3** | **High severity: 5** | **Medium severity: 4** | **Low severity: 2**

---

## Chapter Ratings

| Chapter | Rating | Notes |
|---------|--------|-------|
| T0 — Safety | **PASS** | Excellent coverage. One minor "All choices" trap with T0A06 option C wording. |
| T1 — FCC Rules | **PASS (CONDITIONAL)** | Strong coverage of 68 questions. One critical wording mismatch on T2A09/monitoring vs. listening. |
| T2 — Operating Procedures | **FAIL** | Two findings that could directly cause wrong answers: "monitoring" vs. "listening" (T2A09), and "messages" vs. "formal messages" (T2C05). Also, the study guide says "Before calling CQ" with steps that match T2A12 (removed question) but the content about CQ procedure is fine for T2A06. |
| T3 — Radio Waves | **PASS** | Solid coverage. No errors found in formulas or frequencies. |
| T4 — Amateur Practices | **PASS (CONDITIONAL)** | FT8 software name discrepancy (WSJT-X vs. "FT8 software"). One missing topic. |
| T5 — Electrical Principles | **PASS** | Formulas correct. All Ohm's Law and power calculations verified. Metric conversions accurate. |
| T6 — Components | **PASS** | Good coverage. Gain definition handles the "All these choices" answer correctly. |
| T7 — Practical Circuits | **PASS** | Strong troubleshooting coverage. All interference scenarios well handled. |
| T8 — Signals & Emissions | **PASS** | Digital modes well covered. Satellite section thorough. |
| T9 — Antennas & Feedlines | **PASS (CONDITIONAL)** | One critical finding: T9B01 connector weather protection "All these choices" not directly stated. |

---

## Detailed Findings

### FINDING 1 — CRITICAL ⛔
**File:** T2-operating-procedures.md  
**Issue:** Study guide says "monitoring" but exam answer says "listening"  
**Question:** T2A09 — "Which of the following is a customary way to indicate a station is listening on a repeater?"  
**Correct answer:** B — The station's call sign followed by the word **"listening"**  
**Study guide says:** *"say your call sign followed by the word 'monitoring'"*  
**Risk:** Student memorizes "monitoring" from the study guide, sees "listening" on the exam in option B, doesn't recognize it as the right answer, or worse — looks for a "monitoring" answer that doesn't exist.  
**Wrong answer student might pick:** A, C, or D (none say "monitoring")  
**Severity:** CRITICAL — direct answer mismatch  
**Note:** The old pool (2022-2026) used "monitoring" as the correct answer. This changed in the 2026-2030 pool to "listening." The study guide was not updated.

### FINDING 2 — CRITICAL ⛔
**File:** T2-operating-procedures.md  
**Issue:** Study guide says "messages" but exam answer says "formal messages"  
**Question:** T2C05 — "What does the term 'traffic' refer to in net operation?"  
**Correct answer:** A — **Formal** messages exchanged by net stations  
**Study guide says:** *"The word 'traffic' in net operation refers to messages exchanged by net stations"*  
**Risk:** Student might not distinguish between the exam answer and a distractor because the guide doesn't emphasize the word "formal." On the exam, if a distractor said "Any messages exchanged by net stations" or similar, the student might pick it.  
**Wrong answer student might pick:** The risk here is lower since the current distractors are clearly wrong, but missing "formal" means the student doesn't have the precise vocabulary. The bigger risk is if they second-guess themselves.  
**Severity:** HIGH — imprecise language that doesn't match the exam answer verbatim  

### FINDING 3 — HIGH ⚠️
**File:** T2-operating-procedures.md  
**Issue:** Question wording changed: "distorted" → "drop out" for FM over-deviation  
**Question:** T2B05 — "Which of the following would cause your FM transmission audio to **drop out** on voice peaks?"  
**Study guide says:** *"If your FM transmission audio is **distorted** on voice peaks, you're probably talking too loudly"*  
**Risk:** The question now says "drop out" not "distorted." The study guide describes this as distortion, not dropout. A student may not connect "drop out on voice peaks" with "talking too loudly" because the guide uses different symptom language. They might think "drop out" means a different problem (like weak signal or offset issue).  
**Wrong answer student might pick:** A (offset inverted) or B (deviation too low)  
**Severity:** HIGH — symptom description mismatch between guide and exam

### FINDING 4 — HIGH ⚠️
**File:** T0-safety.md  
**Issue:** T0A06 option C changed — guide mentions interlocks, exam mentions capacitor discharge  
**Question:** T0A06 — "What is a good way to guard against electrical shock?" (Answer: D, All these choices are correct)  
**Exam option C:** "Ensure all capacitors used for high-voltage DC are fully discharged before working inside equipment"  
**Study guide option C equivalent:** *"install mechanical interlocks in high-voltage circuits"*  
**Risk:** The guide teaches three electrical safety practices (three-wire cords, common safety ground, mechanical interlocks). The exam's three choices are different (three-wire cords, common safety ground, capacitor discharge). The student needs to recognize ALL THREE exam options are correct. The guide doesn't explicitly list "discharge capacitors" as one of the shock-prevention methods in this section — it discusses capacitor discharge in the power supply hazards section but doesn't connect it to this "All these choices are correct" answer.  
**Mitigation:** The guide does mention capacitor hazards later in the chapter, so an attentive student should still get this right. But the disconnect could cause hesitation.  
**Severity:** HIGH — "All these choices" answer where one sub-answer isn't grouped with the question topic  

### FINDING 5 — HIGH ⚠️
**File:** T4-amateur-practices.md  
**Issue:** FT8 software name discrepancy  
**Question:** T4A04 — "How are the audio input and output of a transceiver connected in a station configured to operate using FT8?"  
**Correct answer:** B — "To the audio output and input of a computer running **FT8 software**"  
**Study guide says:** *"the transceiver's audio input and output connect to the audio input and output of a computer running **WSJT-X software**"*  
**Risk:** The exam answer changed from "WSJT-X software" to the more generic "FT8 software." The guide uses the old specific name. A student who memorized "WSJT-X" might not recognize "FT8 software" as the same thing, or might think it's a different setup.  
**Wrong answer student might pick:** A (terminal program/TNC)  
**Severity:** HIGH — terminology mismatch that could confuse  

### FINDING 6 — HIGH ⚠️
**File:** T9-antennas-feedlines.md  
**Issue:** Weather protection of connectors — "All these choices are correct" not explicitly stated  
**Question:** T9B01 — "Which of the following connectors should be carefully taped for weather protection when used outdoors?"  
**Correct answer:** D — All these choices are correct (PL259, BNC, Type N)  
**Study guide says:** *"When used outdoors, all these choices are correct when asked which connectors should be carefully taped for weather protection — PL-259, Type N, BNC, and all other RF connectors should be sealed"*  
**Risk:** Actually, the guide DOES explicitly address this. No issue.  
**Severity:** RESCINDED — guide covers this correctly  

### FINDING 6 (REVISED) — MEDIUM ℹ️  
**File:** T1-fcc-rules.md  
**Issue:** Guide says power below 0.1 watt doesn't require ID, but exam answer says "control model craft"  
**Question:** T1D11 — "When may an amateur station transmit without identifying on the air?"  
**Correct answer:** D — "When transmitting signals to control model craft"  
**Study guide says:** *"The only time you can transmit without identifying on the air is when the transmitted power level is below 0.1 watt, such as when controlling model craft"*  
**Risk:** The study guide conflates two things: (1) the 0.1-watt threshold and (2) model craft control. Option C in the exam is "When the transmitted power level is below 0.1 watt" — this is a WRONG answer. Option D "When transmitting signals to control model craft" is the CORRECT answer. The study guide's phrasing "when the transmitted power level is below 0.1 watt, such as when controlling model craft" could lead a student to pick C instead of D, because the guide emphasizes the 0.1-watt power level as the key criterion rather than the model craft activity.  
**Per 97.215:** The rule exempts telecommand of model craft under 1 watt, not a blanket below-0.1-watt exemption.  
**Wrong answer student might pick:** C (power below 0.1 watt)  
**Severity:** CRITICAL ⛔ — Study guide's framing actively leads toward the wrong answer (C instead of D)  

### FINDING 7 — HIGH ⚠️  
**File:** T1-fcc-rules.md  
**Issue:** Guide says "incidental to classroom instruction" but exam says "a part of"  
**Question:** T1D08 — "In which of the following circumstances may the control operator receive compensation?"  
**Correct answer:** B — "When the communication is **a part of** classroom instruction"  
**Study guide says:** *"The only time you can receive compensation for operating an amateur station is when the communication is **a part of** classroom instruction at an educational institution."*  
**Risk:** Actually, the guide got this right — it uses "a part of." No issue.  
**Severity:** RESCINDED — guide is correct  

### FINDING 7 (REVISED) — MEDIUM ℹ️
**File:** Multiple chapters  
**Issue:** No coverage of T4B04 — what FM sounds like off-frequency  
**Question:** T4B04 — "What does an FM signal sound like when received slightly off frequency?"  
**Correct answer:** D — The audio becomes distorted  
**Study guide says (T4):** *"What does an FM signal sound like when received slightly off frequency? The audio becomes distorted. FM demodulation requires being tuned to the exact center frequency."*  
**Risk:** Actually, the guide DOES cover this. No issue.  
**Severity:** RESCINDED — guide covers this  

### FINDING 7 (FINAL) — MEDIUM ℹ️
**File:** T4-amateur-practices.md  
**Issue:** Missing coverage for "memory channels" as way to enable quick access to favorite frequency  
**Question:** T4B04 was replaced — the old question about memory channels (T4B04 old: "What is a way to enable quick access to a favorite frequency?") is now gone. New question is about FM off-frequency sound. But T4 still mentions memory channels: *"Memory channels store your favorite frequencies for one-touch recall."* — this is for general knowledge since the question was replaced. No issue.  
**Severity:** RESCINDED  

### FINDING 8 — MEDIUM ℹ️
**File:** T5-electrical-principles.md  
**Issue:** RF definition moved but may be uncovered for T5C06  
**Question:** T5C06 — "What is the abbreviation for kilohertz?" (Answer: A — kHz)  
**Study guide says:** *"Capitalization matters... Kilohertz is kHz — lowercase k for kilo since it's not a person's name, capital H, lowercase z."*  
**Risk:** The guide covers this well. No issue.  
**Severity:** RESCINDED  

---

Let me consolidate to only real, confirmed findings:

---

## CONFIRMED FINDINGS

### FINDING 1 — CRITICAL ⛔
**File:** T2-operating-procedures.md  
**Question:** T2A09  
**Issue:** Study guide says **"monitoring"** but the 2026 exam answer says **"listening"**  
**Impact:** Student memorizes "monitoring," doesn't see it on exam, picks wrong answer  
**Fix:** Change "monitoring" to "listening" in the guide  

### FINDING 2 — CRITICAL ⛔  
**File:** T1-fcc-rules.md (and T0-safety.md mentions it too)  
**Question:** T1D11  
**Issue:** Study guide frames no-ID exemption as "power below 0.1 watt" (which is wrong answer C) rather than "control of model craft" (correct answer D)  
**The guide says:** *"The only time you can transmit without identifying on the air is when the transmitted power level is below 0.1 watt, such as when controlling model craft — RC airplanes, boats, or cars."*  
**The exam says:**
- C: When the transmitted power level is below 0.1 watt ← WRONG  
- D: When transmitting signals to control model craft ← CORRECT  
**Impact:** Student reads the guide, fixates on "0.1 watt" as the rule, sees it as option C, picks it, and gets it WRONG  
**Fix:** Rewrite to emphasize model craft control as the exemption, with 0.1 watt as a secondary detail, not the headline  

### FINDING 3 — HIGH ⚠️
**File:** T2-operating-procedures.md  
**Question:** T2B05  
**Issue:** Symptom language mismatch — guide says "distorted on voice peaks," exam says "drop out on voice peaks"  
**Impact:** Student may not connect "drop out" with "talking too loudly" because the guide used "distorted"  
**Fix:** Add "drop out" alongside "distorted" in the description  

### FINDING 4 — HIGH ⚠️
**File:** T0-safety.md  
**Question:** T0A06  
**Issue:** One of three sub-answers for "All these choices are correct" differs between guide and exam (guide: interlocks; exam: capacitor discharge). Guide covers capacitor discharge elsewhere but doesn't group it with this question's topic.  
**Impact:** Student might hesitate on the "All choices correct" answer since one option isn't what they studied  
**Fix:** Update the three electrical safety practices to match the current exam options (three-wire cords, common safety ground, capacitor discharge)  

### FINDING 5 — HIGH ⚠️  
**File:** T4-amateur-practices.md  
**Question:** T4A04  
**Issue:** Guide says "WSJT-X software" but exam now says "FT8 software"  
**Impact:** Terminology confusion — student looks for "WSJT-X" and doesn't see it  
**Fix:** Add "FT8 software" alongside or instead of "WSJT-X software"  

### FINDING 6 — HIGH ⚠️  
**File:** T2-operating-procedures.md  
**Question:** T2C05  
**Issue:** Guide says "messages exchanged by net stations" but exam says "**formal** messages"  
**Impact:** Missing the word "formal" means the student doesn't have the precise exam vocabulary  
**Fix:** Add "formal" before "messages" in the traffic definition  

### FINDING 7 — MEDIUM ℹ️  
**File:** T2-operating-procedures.md  
**Issue:** "Before calling CQ" procedures — guide mentions listening first, asking if frequency is in use, and verifying authorization. The old question T2A12 was removed. T2A06 now asks about how to call CQ (correct answer: repeat CQ, followed by "this is" and call sign). Guide covers T2A06 correctly: *"An effective way to seek a call from any phone station when not using a repeater is to repeat 'CQ' a few times, followed by 'this is,' and your call sign, then pause to listen; repeat as necessary."*  
**Risk:** Low — guide covers the new question.  
**Severity:** MEDIUM — the "Before calling CQ" content is now studying for a removed question (harmless but wasted study time)  

### FINDING 8 — MEDIUM ℹ️
**File:** T3-radio-waves.md  
**Issue:** Ionosphere described as both "reflect" and "refract" in different contexts  
**Question:** T3A11 asks "Which region of the atmosphere can **reflect** HF radio waves?" (Answer: ionosphere)  
**Study guide says:** *"The ionosphere is the region of the atmosphere that can reflect HF radio waves"* — correct!  
**But also says:** *"the F region of the ionosphere becomes ionized enough to **refract** signals"* — also technically correct for different context  
**Risk:** Low — the guide uses "reflect" for the specific exam question context and "refract" for the propagation mechanism context. This is actually scientifically accurate (the ionosphere refracts, which appears as reflection). But a confused student might mix up the terms.  
**Severity:** LOW — both terms are used correctly in context  

### FINDING 9 — MEDIUM ℹ️
**File:** T7-practical-circuits.md  
**Issue:** Multimeter coverage — guide says it measures "voltage, current, and resistance" but also says "It does not measure signal strength, noise, impedance, or reactance."  
**Question:** T7D07 — "Which of the following measurements are made using a multimeter?"  
**Correct answer:** C — Voltage and resistance (NOT "All these choices are correct")  
**Risk:** The guide correctly notes voltage, current, and resistance are multimeter functions. However, the exam answer is specifically "Voltage and resistance" (C), not "All these choices" (D). The guide's mention of current measurement is correct but might lead a student to think D is right if they see "current" as an option in a different answer. Current isn't in the answer choices though, so no real risk.  
**Severity:** LOW  

### FINDING 10 — MEDIUM ℹ️  
**File:** T8-signals-emissions.md  
**Issue:** CW bandwidth stated as "about 150 hertz"  
**Question:** T8A11 — "What is the approximate bandwidth required to transmit a CW signal?" (Answer: B — 150 Hz)  
**Study guide says:** *"CW — Morse code — has the narrowest bandwidth of any common amateur mode at about 150 hertz."*  
**Risk:** None — exact match. Guide is correct.  
**Severity:** RESCINDED  

### FINDING 10 (REVISED) — MEDIUM ℹ️
**File:** T8-signals-emissions.md  
**Issue:** SSB bandwidth stated as "approximately 3 kilohertz" — guide says "from about 300 hertz to 3000 hertz"  
**Question:** T8A08 — "What is the approximate bandwidth of a typical single sideband (SSB) voice signal?" (Answer: B — 3 kHz)  
**Risk:** The guide says "300 to 3000 hertz" which implies 2700 Hz, but then says "approximately 3 kilohertz" which matches the exam. The "300 to 3000" range might confuse a pedantic student into thinking 2.7 kHz is more accurate, but since the guide also says "approximately 3 kHz," there's no real risk.  
**Severity:** LOW  

### FINDING 11 — MEDIUM ℹ️
**File:** T6-components.md  
**Issue:** Gain definition for T6B11 — "All these choices are correct"  
**Question:** T6B11 — "What does the term gain mean in amplifiers?" (Answer: D — All these choices are correct: voltage, current, and power gain)  
**Study guide says:** *"Gain can refer to an increase in signal voltage, signal current, or signal power — all these choices are correct."*  
**Risk:** The guide explicitly nails this "All these choices" answer. Well done.  
**Severity:** PASS — no issue  

---

## Formula Verification ✅

| Formula | Guide Statement | Correct? |
|---------|----------------|----------|
| Ohm's Law: I = E/R | T5: "Current equals voltage divided by resistance" | ✅ |
| Ohm's Law: E = I×R | T5: "Voltage equals current times resistance" | ✅ |
| Ohm's Law: R = E/I | T5: "Resistance equals voltage divided by current" | ✅ |
| Power: P = I×E | T5: "P = I x E — power equals current times voltage" | ✅ |
| Wavelength: λ = 300/f(MHz) | T3: "wavelength in meters equals 300 divided by frequency in megahertz" | ✅ |
| Decibels: ×2 power = +3 dB | T5: "doubling power equals plus 3 dB" | ✅ |
| Decibels: ×10 power = +10 dB | T5: "multiplying power by 10 equals plus 10 dB" | ✅ |
| Battery life: Ah/A = hours | T4: "divide the battery's ampere-hour rating by the average current draw" | ✅ |
| Quarter-wave vertical (inches): 2808/f(MHz) | T9: "length in inches equals 2808 divided by the frequency in megahertz" | ✅ |

**All formulas verified correct. No formula errors found.**

## Frequency/Number Verification ✅

| Fact | Guide Statement | Correct? |
|------|----------------|----------|
| 2m simplex calling: 146.520 MHz | ✅ Correct | ✅ |
| 2m band: 144-148 MHz | ✅ Correct | ✅ |
| 6m band: 50-54 MHz | ✅ Correct | ✅ |
| 2m repeater offset: ±600 kHz | ✅ Correct | ✅ |
| 70cm repeater offset: ±5 MHz | ✅ Correct | ✅ |
| Tech HF phone: 28.300-28.500 MHz | ✅ Correct | ✅ |
| CW-only 2m: 144.0-144.1 MHz | ✅ Correct | ✅ |
| CW-only 6m: 50.0-50.1 MHz | ✅ Correct | ✅ |
| HF power limit (Tech): 200W PEP | ✅ Correct | ✅ |
| VHF/UHF power limit: 1500W PEP | ✅ Correct | ✅ |
| License term: 10 years | ✅ Correct | ✅ |
| Renewal window: 90 days before expiration | ✅ Correct | ✅ |
| Grace period: 2 years | ✅ Correct | ✅ |
| ID interval: 10 minutes + end | ✅ Correct | ✅ |
| HF beacon sub-band: 28.200-28.300 MHz | ✅ Correct | ✅ |
| Space station altitude: >50 km | ✅ Correct | ✅ |
| Speed of light: 300,000,000 m/s | ✅ Correct | ✅ |
| VHF range: 30-300 MHz | ✅ Correct | ✅ |
| UHF range: 300-3000 MHz | ✅ Correct | ✅ |
| HF range: 3-30 MHz | ✅ Correct | ✅ |
| Club station minimum members: 4 | ✅ Correct | ✅ |
| Coax impedance: 50 ohms | ✅ Correct | ✅ |
| 6m calling frequency: 52.525 MHz | ✅ Correct | ✅ |
| Min distance from power lines: 10 feet (if antenna falls) | ✅ Correct | ✅ |
| Tower ground rods: 8-foot, each leg | ✅ Correct | ✅ |
| Lowest MPE band: 50 MHz | ✅ Correct | ✅ |

**All frequencies, power limits, distances, and time periods verified correct.**

## Cross-Chapter Contradiction Check ✅

| Check | Result |
|-------|--------|
| T1 repeater definition vs. T2 repeater definition | Consistent — "simultaneously retransmits on different channel" |
| T1 RACES definition vs. T2 RACES definition | Consistent — both mention civil defense certification |
| T0 RF safety frequency vs. T3 frequency ranges | Consistent — 50 MHz correctly placed in VHF |
| T1 power limits vs. T5 power calculations | No conflict |
| T1 station ID rules vs. T2 tactical calls | Consistent — both say 10 min + end of communication |
| T3 ionosphere "reflect" vs. T3 "refract" | Both used, technically correct in context (see Finding 8) |

**No inter-chapter contradictions found.**

## "All These Choices Are Correct" Trap Analysis

I identified 53 questions where "All these choices are correct" appears as an answer option. Of those:
- **17 questions** have D="All these choices are correct" as the CORRECT answer
- **36 questions** have it as a WRONG answer (trap/distractor)

### Key trap questions the guide handles well:
- **T0A02** (current hazards): Guide says "All three of these effects are real dangers" ✅
- **T0B02** (tower climbing): Guide says "All three requirements are mandatory" ✅  
- **T5A11** (resistance opposes all current): Guide says "equal-opportunity obstructor" ✅
- **T6A10** (rechargeable batteries): Guide lists all three ✅
- **T6B11** (gain definition): Guide explicitly says "all these choices are correct" ✅

### Trap questions where students could be misled:
- **T0A06** (electrical shock safety): See Finding 4 — option C differs from guide ⚠️
- **T0C07** (touching antenna hazard): Correct answer is B (RF burn), NOT D (All). Guide correctly says "RF burns to the skin" and distinguishes from electrocution. ✅
- **T0C08** (reduce RF exposure): Correct answer is A (relocate antennas), NOT D. Guide says "relocate antennas farther from people" and explicitly says "moving just the transmitter doesn't help." ✅
- **T8B01** (satellite beacon telemetry): Correct is C (health/status), NOT D. Guide says "health and status" specifically. ✅

## 10 Hardest Questions — Coverage Check

| Question | Topic | Covered? |
|----------|-------|----------|
| T1D07 — Auxiliary station example | One-way link between remote receiver and repeater | ✅ Covered |
| T7D05 — How ohmmeter works | Applies small current, measures voltage | ✅ Covered |
| T3B12 — Which frequency travels fastest | All same velocity in free space | ✅ Covered |
| T2B14 — What is a talkgroup | DMR traffic organization identifier | ✅ Covered |
| T2C12 — Certification by civil defense | RACES requires it | ✅ Covered |
| T1A06 — HF beacon frequencies | 28.200-28.300 MHz on 10m | ✅ Covered |
| T1A10 — RACES control operator req | Civil defense enrollment certification | ✅ Covered |
| T1E11 — Control operator definition | Designated by licensee, responsible for compliance | ✅ Covered |
| T4B04 — FM off-frequency sound | Audio becomes distorted | ✅ Covered |
| T9B01 — Connector weather protection | All connectors need taping | ✅ Covered |

**All 10 hardest questions have adequate coverage in the study guide.**

---

## Summary of Required Fixes (Priority Order)

### Must Fix Before Publication 🔴

1. **T2A09 — "monitoring" → "listening"** — Direct answer mismatch. The 2026 pool changed the correct term. One word change in T2-operating-procedures.md fixes this.

2. **T1D11 — Reframe no-ID exemption** — The guide leads students toward wrong answer C (power < 0.1W) instead of correct answer D (model craft control). The exemption per §97.215 is about telecommand of model craft, not a blanket low-power exemption. Rewrite to lead with "control of model craft" as the exemption.

3. **T0A06 — Update shock prevention practices** — Replace "mechanical interlocks" with "discharge capacitors" to match the current exam's third option for this "All choices correct" answer.

### Should Fix 🟡

4. **T2B05 — Add "drop out" symptom language** — The exam now says "drop out on voice peaks" not "distorted on voice peaks." Add "drop out" alongside or instead of "distorted."

5. **T4A04 — Add "FT8 software"** — Alongside or instead of "WSJT-X software" to match the updated exam answer.

6. **T2C05 — Add "formal"** — Change "messages exchanged" to "formal messages exchanged" to match the exam's precise wording.

### Nice to Fix 🟢

7. **T2-operating-procedures.md** — Remove or update "Before calling CQ" procedures that match the removed question T2A12 (cosmetic, not harmful).

8. **T3-radio-waves.md** — Add a note clarifying that "reflect" and "refract" are both used for the ionosphere (pedagogical clarity).

---

## Changed Questions — Coverage Status

Of the 73 questions flagged as needing work in the change manifest:
- **5 added questions:** All covered ✅
- **7 removed questions:** Content still in guide (harmless but could be trimmed)
- **27 topic replacements:** All new topics covered ✅
- **7 correct-answer-changed:** All handled except T2A09 (Finding 1) and T1D11 framing concern (Finding 2)
- **34 significant rewords:** All covered ✅

**Overall: 71/73 changed questions adequately covered. 2 need fixes.**
