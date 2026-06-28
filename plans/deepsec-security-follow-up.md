# DeepSec Security Follow-up Plan

Date: 2026-06-28

## #1 Review Study App DOM injection candidates

DeepSec fast scan found security candidates in `apps/study-app/app.js`: 25 hits total. These are **not AI-confirmed vulnerabilities yet**; they are matcher hits that need human/AI triage.

Candidate clusters:

1. `dangerous-html` / `xss` — many `innerHTML` and template literal render paths. Verify all inserted values come from trusted static question-pool data, or switch dynamic user/imported values to `textContent` / DOM node construction.
2. `non-atomic-read-delete` — review local persistence/import/export/delete flows for race-prone behavior.
3. `insecure-crypto` — likely `Math.random()` / shuffle usage; confirm it is only study randomization and not security-token generation.

Repair checklist:

1. Identify every `innerHTML` sink in `apps/study-app/app.js`.
2. Classify data source for each sink: static bundled content, user input, imported JSON, URL/hash params, localStorage.
3. Replace any non-static/untrusted insertion with safe DOM APIs.
4. Add regression tests or a small sanitizer helper if imported study data can ever be user-controlled.
5. Run full DeepSec AI processing when gateway auth is restored; current result is matcher-only.
