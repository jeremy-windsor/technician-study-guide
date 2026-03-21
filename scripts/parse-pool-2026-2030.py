#!/usr/bin/env python3
"""
Parse the 2026-2030 NCVEC Technician question pool PDF → questions.json
Format: TXXX## (LETTER) [refs]\nQuestion\nA. ...\nB. ...\nC. ...\nD. ...\n~~
"""
import re
import json
import os
from pdfminer.high_level import extract_text

PDF = "pool-2026-2030.pdf"  # place the NCVEC PDF here
OUT = "../pools/2026-2030/questions.json"

SUBELEMENT_NAMES = {
    "T1": {"name": "Commission's Rules", "exam_questions": 6},
    "T2": {"name": "Operating Procedures", "exam_questions": 3},
    "T3": {"name": "Radio Wave Characteristics", "exam_questions": 3},
    "T4": {"name": "Amateur Radio Practices", "exam_questions": 2},
    "T5": {"name": "Electrical Principles", "exam_questions": 4},
    "T6": {"name": "Electronic Components", "exam_questions": 4},
    "T7": {"name": "Practical Circuits", "exam_questions": 4},
    "T8": {"name": "Signals and Emissions", "exam_questions": 4},
    "T9": {"name": "Antennas and Feed Lines", "exam_questions": 2},
    "T0": {"name": "Electrical and RF Safety", "exam_questions": 3},
}

def clean_text(text):
    """Remove form feeds and normalize whitespace while preserving line structure."""
    # Replace form feed (page breaks) with space
    text = text.replace('\x0c', ' ')
    # Collapse multiple blank lines to one
    text = re.sub(r'\n[ \t]*\n[ \t]*\n+', '\n\n', text)
    return text

def extract_pool_text(pdf_path):
    text = extract_text(pdf_path)
    text = clean_text(text)
    # Find the start of the actual question pool (first T1A01 in pool format)
    # The errata section has "T1C01 –" format, pool has "T1A01 (C)"
    idx = text.find('T1A01 (')
    if idx == -1:
        raise ValueError("Could not find T1A01 in PDF")
    return text[idx:]

def parse_questions(raw):
    """
    Parse all questions from raw pool text.
    Strategy: find each question header, then extract to next question header or ~~.
    """
    questions = []

    # Pattern to find question ID lines: TXXX## (LETTER) [optional_refs]
    # Use finditer to locate all question starts
    qid_re = re.compile(
        r'(T[0-9][A-F]\d{2})\s+\(([A-D])\)([^\n]*)\n',
    )

    # Find all question positions
    q_starts = [(m.start(), m.group(1), m.group(2), m.group(3).strip()) 
                for m in qid_re.finditer(raw)]

    print(f"Found {len(q_starts)} question headers")

    for i, (start, qid, correct, extra) in enumerate(q_starts):
        # Get text for this question (until next question or end)
        end = q_starts[i+1][0] if i+1 < len(q_starts) else len(raw)
        block = raw[start:end].strip()

        # Extract refs
        refs_match = re.match(r'^\[([^\]]+)\]', extra)
        refs = refs_match.group(1) if refs_match else None

        # Remove the ID line from block
        # block starts with "T1A01 (C) [97.1] \n..."
        block_lines = block.split('\n')
        content_lines = block_lines[1:]  # skip the ID line

        # Strip trailing ~~ and blank lines
        cleaned_lines = []
        for line in content_lines:
            stripped = line.strip()
            if stripped == '~~':
                break
            cleaned_lines.append(stripped)

        # Remove leading/trailing blank entries
        while cleaned_lines and not cleaned_lines[0]:
            cleaned_lines.pop(0)
        while cleaned_lines and not cleaned_lines[-1]:
            cleaned_lines.pop()

        # Find answer start (line beginning with "A. ")
        answer_start_idx = None
        for j, line in enumerate(cleaned_lines):
            if re.match(r'^A\.\s', line):
                answer_start_idx = j
                break

        if answer_start_idx is None:
            print(f"WARNING: No answers found for {qid}, lines: {cleaned_lines[:5]}")
            continue

        # Question text = everything before A.
        question_lines = [l for l in cleaned_lines[:answer_start_idx] if l]
        question = ' '.join(question_lines).strip()

        # Parse answers: collect lines, split by "A.", "B.", "C.", "D." markers
        answer_lines = cleaned_lines[answer_start_idx:]
        answers = {}
        current_letter = None
        current_text = []

        for line in answer_lines:
            if not line:
                continue
            m = re.match(r'^([A-D])\.\s+(.*)', line)
            if m:
                if current_letter:
                    answers[current_letter] = ' '.join(current_text).strip()
                current_letter = m.group(1)
                current_text = [m.group(2).strip()] if m.group(2).strip() else []
            else:
                if current_letter:
                    # continuation of current answer
                    current_text.append(line)

        if current_letter:
            answers[current_letter] = ' '.join(current_text).strip()

        if len(answers) != 4:
            print(f"WARNING: {qid} has {len(answers)} answers: {list(answers.keys())}")
            if len(answers) < 2:
                print(f"  Block snippet: {cleaned_lines[:10]}")
            continue

        subelement = qid[:2]
        group = qid[:3]

        questions.append({
            "id": qid,
            "subelement": subelement,
            "group": group,
            "question": f"[{refs}] {question}" if refs else question,
            "correct": correct,
            "answers": answers,
        })

    return questions


def main():
    print("Extracting text from PDF...")
    raw = extract_pool_text(PDF)
    print(f"Raw text length: {len(raw)} chars")

    print("Parsing questions...")
    questions = parse_questions(raw)
    print(f"\nParsed {len(questions)} questions")

    # Verify counts
    by_se = {}
    for q in questions:
        se = q["subelement"]
        by_se[se] = by_se.get(se, 0) + 1

    print("\nPer-subelement counts:")
    expected = {"T1":68,"T2":37,"T3":35,"T4":23,"T5":50,"T6":46,"T7":44,"T8":47,"T9":23,"T0":36}
    for se in sorted(by_se):
        got = by_se.get(se, 0)
        exp = expected.get(se, "?")
        status = "✓" if got == exp else f"MISMATCH (expected {exp})"
        print(f"  {se}: {got} {status}")

    # Build subelements metadata
    subelements = {}
    for se, info in SUBELEMENT_NAMES.items():
        count = by_se.get(se, 0)
        subelements[se] = {
            "name": info["name"],
            "exam_questions": info["exam_questions"],
            "pool_size": count,
        }

    output = {
        "pool": "2026-2030",
        "effective": "2026-07-01",
        "expires": "2030-06-30",
        "total": len(questions),
        "subelements": subelements,
        "questions": questions,
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)

    with open(OUT, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\nWrote {len(questions)} questions to {OUT}")

    # Spot-check errata questions
    print("\nErrata spot checks:")
    checks = {
        "T1C01": ("D", "For which classes of amateur radio licenses does the FCC currently issue new licenses?"),
        "T5A05": ("A", "A difference in which of the following causes electron flow?"),
        "T7A09": ("B", "What is the function of the switch which selects either SSB or CW-FM"),
        "T0A10": ("A", "What hazard exists when rapidly charging or discharging an unprotected battery?"),
    }
    for qid, (exp_correct, exp_q_fragment) in checks.items():
        q = next((x for x in questions if x["id"] == qid), None)
        if q:
            q_match = exp_q_fragment.lower() in q["question"].lower()
            c_match = q["correct"] == exp_correct
            print(f"  {qid}: correct={q['correct']} {'✓' if c_match else f'WRONG (expected {exp_correct})'}, question {'✓' if q_match else 'MISMATCH'}")
        else:
            print(f"  {qid}: NOT FOUND ✗")


if __name__ == "__main__":
    main()
