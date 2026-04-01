# T1 — FCC Rules & Regulations: Adversarial Review

**Reviewer:** Adversarial Subagent (CCIE-examiner scrutiny level)  
**Date:** 2026-03-31  
**Files Reviewed:**
- `subelements/T1-fcc-rules.md` (narrative study guide)
- `subelements/T1-fcc-rules-questions.md` (question bank with explanations)
- `pools/2026-2030/questions.json` (official 2026-2030 question pool, T1* questions)

---

## 1. ANSWER VERIFICATION — Correct Answer Letters vs. Pool JSON

**All 68 of 68 T1 question answers match the official pool.** Zero mismatches.

| Group | Questions | All Match? |
|-------|-----------|------------|
| T1A   | 01–11     | ✅ 11/11    |
| T1B   | 01–12     | ✅ 12/12    |
| T1C   | 01–11     | ✅ 11/11    |
| T1D   | 01–12     | ✅ 12/12    |
| T1E   | 01–11     | ✅ 11/11    |
| T1F   | 01–11     | ✅ 11/11    |

**Verdict: PASS — No answer key errors.**

---

## 2. EXAM READINESS — Coverage Completeness

All 68 T1 questions from the official 2026-2030 pool appear in the questions file with full answer choices and explanations. The narrative study guide covers every concept tested. No pool questions are orphaned.

**Verdict: PASS — 100% coverage.**

---

## 3. CRITICAL ISSUES

### 🔴 ISSUE #1: T1D11 — Dangerously Wrong Explanation (EXAM-FAILING RISK)

**Question:** *When may an amateur station transmit without identifying on the air?*
- A) When the transmissions are of a brief nature to make station adjustments
- B) When the transmissions are unmodulated
- C) When the transmitted power level is below 0.1 watt ← **TRAP ANSWER**
- **D) When transmitting signals to control model craft** ← **CORRECT (pool: D)**

**What the study guide says (narrative):**
> "The only time you can transmit without identifying on the air is when the transmitted power level is below 0.1 watt, such as when controlling model craft"

**What the questions file explanation says:**
> "An amateur station may transmit without on-air identification when the transmitted power is below 0.1 watt, which applies to model craft control under Part 97.215. At such low power levels for radio control, the identification requirement is waived."

**What the actual FCC rule says (47 CFR 97.215):**
> (a) The station identification procedure is not required for transmissions directed only to the model craft, provided that a label indicating the station call sign and the station licensee's name and address is affixed to the station transmitter.  
> (c) The transmitter power must not exceed **1 W**.

**THREE problems here:**

1. **Wrong basis for exemption.** The identification exemption under 97.215(a) is based on the *type of operation* (telecommand of model craft with a label on the transmitter) — NOT on power level. The 0.1-watt threshold cited in the explanation doesn't appear ANYWHERE in Part 97.

2. **Wrong power figure.** The model craft power limit is 1 watt per 97.215(c), not 0.1 watt. The "0.1 watt" figure is fabricated — it exists in neither 97.215 nor any other Part 97 section.

3. **Directs students toward the trap answer.** Answer C ("below 0.1 watt") is a deliberate distractor. Both the narrative and the explanation emphasize "below 0.1 watt" as the reason for the exemption — which is *exactly what answer C says*. A student who learns the reasoning rather than memorizing the letter will pick C and get it WRONG.

**The correct answer D is marked correctly** (✅), so pure memorization would survive. But any student who reads the explanation and tries to understand *why* will be primed to select the wrong answer.

**Severity: CRITICAL — Could directly cause a wrong answer on the exam.**

---

## 4. MINOR ISSUES

### 🟡 ISSUE #2: T1B11/Narrative — Imprecise scope of 200W HF limit

**Narrative says:**
> "Technicians are limited to 200 watts peak envelope power on their HF band segments, which is the 10 meter band."

**Problem:** The 200W PEP limit applies to ALL Technician HF segments — not just 10 meters. Technicians also have CW/data privileges on 80m (3.525–3.600), 40m (7.025–7.125), and 15m (21.025–21.200), all subject to the same 200W limit. The phrasing "which is the 10 meter band" implies 10 meters is the only HF band with this limit.

**Exam impact:** Low. Question T1B11 asks about "their HF band segments" generally, and 200W is correct. The student won't get it wrong, but the narrative creates a false impression that Technicians only have 10-meter HF access.

**Severity: LOW — Misleading context but won't cause a wrong answer.**

### 🟡 ISSUE #3: Narrative — Technician HF CW privileges underexplained

The narrative mentions "The segments below 28.300 are for CW and data modes" (referring only to 10 meters) and never explicitly states that Technicians have CW privileges on 80, 40, and 15 meters. The T1B06 *explanation* does mention this ("They have CW privileges on 80, 40, 15, and 10 meters"), but the narrative alone would leave a student unaware.

**Exam impact:** Low for T1 specifically (no T1 question tests CW privileges on 80/40/15 directly), but creates a knowledge gap.

**Severity: LOW — No direct exam question affected, but incomplete picture.**

### 🟢 ISSUE #4: T1D05 — Explanation adds detail not in the answer choice

The T1D05 explanation says: *"The equipment must be amateur radio related and must be personal property of the licensee, control operator, or their close relatives."*

The correct answer (D) only says: *"When selling amateur radio equipment and not on a regular basis."*

The "personal property" detail is from 97.113(a)(3)(ii) and is accurate, but answer choice B is a trap using similar language ("not the personal property of either the station licensee, or the control operator, or their close relatives"). The explanation's mention of this detail could theoretically confuse a student into thinking B is also relevant, but the overall explanation is clear enough that D is correct.

**Severity: NEGLIGIBLE — Extra context, unlikely to mislead.**

---

## 5. FACTUAL ACCURACY AUDIT

Cross-referencing every major claim against Part 97:

| Claim | Rule | Correct? |
|-------|------|----------|
| Purpose: advancing skills in technical/communication phases | 97.1 | ✅ |
| FCC is sole regulatory agency | 97.1 | ✅ |
| Phonetic alphabet: encouraged, not required | 97.119(b)(2) | ✅ |
| License notification by email from FCC | 97.23 | ✅ |
| License official when in ULS database | 97.7 | ✅ |
| HF beacons: 28.200–28.300 MHz | 97.203(d) | ✅ |
| Space station: >50 km above Earth | 97.3(a)(41) | ✅ |
| Volunteer Frequency Coordinators | 97.3(a)(22) | ✅ |
| RACES: civil defense enrollment required | 97.407(a) | ✅ |
| Willful interference prohibited | 97.101(d) | ✅ |
| Tech phone: 28.300–28.500 MHz | 97.301(e) | ✅ |
| ISS contact: Technician and above | 97.301, 97.207(c) | ✅ |
| 6m band: 50–54 MHz | 97.301(a) | ✅ |
| 2m band: 144–148 MHz | 97.301(a) | ✅ |
| CW-only: 50.0–50.1, 144.0–144.1 MHz | 97.305(a),(c) | ✅ |
| Secondary allocation: yield to primary | 97.303 | ✅ |
| Band edge: all three reasons | 97.101(a) | ✅ |
| SSB allowed in all bands above 50 MHz | 97.305(c) | ✅ |
| 200W PEP on HF segments | 97.313 | ✅ |
| 1500W PEP above 30 MHz | 97.313(b) | ✅ |
| Three license classes issued | 97.9(a), 97.17(a) | ✅ |
| Vanity: any licensed amateur | 97.19 | ✅ |
| International comms: personal character | 97.117 | ✅ |
| Email required or face revocation/suspension | 97.23 | ✅ |
| 2x3 call sign format for Technician | FCC call sign groups | ✅ |
| Vessel operation: US-documented, master's permission | 97.5(a)(2), 97.11(a) | ✅ |
| Renewal: 90 days before expiration | 97.21, 1.949 | ✅ |
| License term: 10 years | 97.25 | ✅ |
| Grace period: 2 years, no transmitting | 97.21 | ✅ |
| Transmit when license in FCC database | 97.5a | ✅ |
| ITU objection blocks communications | 97.111(a)(1) | ✅ |
| Broadcasting prohibited (one-way) | 97.113(b) | ✅ |
| Encoding OK for space stations/model craft | 97.211(b), 97.215(b) | ✅ |
| Music exception: manned spacecraft retransmission | 97.113(c) | ✅ |
| Equipment sale: occasional, amateur equipment | 97.113(a)(3)(ii) | ✅ |
| Indecent/obscene language: blanket prohibition | 97.113(a)(4) | ✅ |
| Auxiliary station: remote receiver to repeater link | 97.201(e) | ✅ |
| Compensation: classroom instruction | 97.113(a)(3)(iii) | ✅ |
| Broadcasting support: only for safety of life/property | 97.113(5)(b) | ✅ |
| Broadcasting definition: reception by general public | 97.3(a)(10) | ✅ |
| Model craft ID exemption | 97.215 | ⚠️ See Issue #1 |
| Test transmissions: must identify | 97.119(a) | ✅ |
| Control operator: always required | 97.7(a) | ✅ |
| Satellite control: any amateur on uplink freq | 97.301, 97.207(c) | ✅ |
| Licensee designates control operator | 97.103(b) | ✅ |
| Control op license determines privileges | 97.103(b) | ✅ |
| Control point definition | 97.3(a)(14) | ✅ |
| Tech can't operate Extra segments | 97.301 | ✅ |
| Both control op and licensee responsible | 97.103(a) | ✅ |
| Repeater = automatic control example | 97.3(a)(6), 97.205(d) | ✅ |
| Any station may be remote controlled | 97.109(c) | ✅ |
| Internet operation = remote control | 97.3(a)(39) | ✅ |
| Control operator definition | 97.3(a)(13) | ✅ |
| FCC inspection: any time upon request | 97.103(c) | ✅ |
| ID every 10 min + end of communication | 97.119(a) | ✅ |
| Tactical calls don't replace legal ID | 97.119(a) | ✅ |
| ID must be in English (phone) | 97.119(b)(2) | ✅ |
| CW or phone acceptable for ID | 97.119(b)(2) | ✅ |
| Stroke/slant/slash all acceptable | 97.119(c) | ✅ |
| Third-party: foreign country agreement required | 97.115(a)(2) | ✅ |
| Third-party definition | 97.3(a)(47) | ✅ |
| Repeater: simultaneous retransmission, different channel | 97.3(a)(40) | ✅ |
| Repeater violation: originating station accountable | 97.205(g) | ✅ |
| Club station: at least 4 members | 97.5(b)(2) | ✅ |

**Score: 67/68 claims verified accurate. 1 claim factually wrong (T1D11 / 0.1W).**

---

## 6. INTERNAL CONTRADICTIONS

**None found.** The narrative and questions file are internally consistent. The one factual error (0.1W claim) appears in BOTH files, so they agree with each other — they're just both wrong against the actual FCC rule.

---

## 7. EXPLANATION QUALITY

Overall: **Excellent.** The explanations are clear, conversational, and effective at distinguishing correct answers from distractors. They consistently explain WHY wrong answers are wrong, which is good study technique.

The one dangerous exception is T1D11 (documented above), where the explanation actively reinforces the trap answer's logic.

---

## 8. OVERALL GRADE

### **B+**

**Breakdown:**
- Answer key accuracy: **A+** (68/68 correct letters)
- Coverage completeness: **A+** (68/68 questions covered)
- Factual accuracy: **A-** (67/68 claims correct; 1 critical error)
- Explanation quality: **B+** (excellent except T1D11 which is actively harmful)
- Narrative completeness: **A-** (minor gaps on CW HF privileges)
- Internal consistency: **A+** (no contradictions)

**The single critical issue (T1D11) prevents an A grade.** The explanation doesn't just omit something — it actively teaches incorrect reasoning that points students toward a trap answer. On a 68-question pool where 6 are sampled, the probability of encountering T1D11 on the exam is ~8.8%, and a student who learned the reasoning rather than memorizing the letter could miss it.

**Everything else is exam-ready.** A student studying only these two files would pass every other T1 question.

---

## 9. REQUIRED FIXES

### Must Fix (Critical)
1. **T1D11 narrative** — Replace "when the transmitted power level is below 0.1 watt, such as when controlling model craft" with "when transmitting signals to control model craft per Part 97.215, provided a label with the call sign is on the transmitter. The power limit for model craft telecommand is 1 watt."
2. **T1D11 explanation** — Rewrite to explain that the exemption is based on the TYPE of operation (model craft telecommand per 97.215), not a power threshold. Explicitly warn that answer C ("below 0.1 watt") is a trap — the 0.1-watt figure doesn't appear in Part 97.

### Should Fix (Minor)
3. **Narrative, Power section** — Clarify that the 200W PEP limit applies to ALL Technician HF segments (80m CW, 40m CW, 15m CW, 10m all modes), not just 10 meters.
4. **Narrative, Frequency Privileges section** — Add a brief mention that Technicians have CW/data privileges on 80, 40, and 15 meters in addition to 10-meter phone.
