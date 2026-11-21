#!/usr/bin/env python3
"""Generate and score a random Technician class practice exam.

Simulates the real exam: one random question from each of the 35 question
groups. Drill mode instead draws 35 questions at random from the whole pool.

Usage:
    python3 practice-test.py                       # Interactive exam (current pool)
    python3 practice-test.py --drill               # Drill: 35 random questions, ignoring groups
    python3 practice-test.py --pool 2026-2030      # Force a specific pool
    python3 practice-test.py --quick               # Show answers immediately
    python3 practice-test.py --stats               # Just show pool stats
"""

import json
import random
import re
import sys
from pathlib import Path

POOLS_DIR = Path(__file__).parent.parent / "pools"
CURRENT_POOL = "2026-2030"

# Questions per subelement on the real exam
EXAM_DISTRIBUTION = {
    "T1": 6, "T2": 3, "T3": 3, "T4": 2, "T5": 4,
    "T6": 4, "T7": 4, "T8": 4, "T9": 2, "T0": 3,
}

EXAM_TOTAL = 35
PASS_MARK = 26

FIGURE_RE = re.compile(r"figure (T-[123])", re.IGNORECASE)


def figure_for(question):
    """Return the figure file a question refers to (e.g. 'T-1.png'), or None."""
    match = FIGURE_RE.search(question["question"])
    return f"{match.group(1).upper()}.png" if match else None


def resolve_pool(pool_arg: str | None) -> tuple[str, Path]:
    """Return (pool_name, pool_path): the --pool value if given, else the current pool."""
    if pool_arg is not None:
        valid = {p.name for p in POOLS_DIR.iterdir() if (p / "questions.json").exists()}
        if pool_arg not in valid:
            print(f"Error: --pool must be one of: {', '.join(sorted(valid))}", file=sys.stderr)
            sys.exit(1)
        name = pool_arg
    else:
        name = CURRENT_POOL

    return name, POOLS_DIR / name / "questions.json"


def load_pool(pool_path: Path):
    with open(pool_path) as f:
        data = json.load(f)
    return data["questions"], data["subelements"]


def generate_exam(questions):
    """Select one question per group, matching real exam structure."""
    by_group = {}
    for q in questions:
        by_group.setdefault(q["group"], []).append(q)

    exam = []
    for group in sorted(by_group.keys()):
        exam.append(random.choice(by_group[group]))

    random.shuffle(exam)
    return exam


def generate_drill(questions):
    """Draw EXAM_TOTAL questions at random from the whole pool, ignoring groups."""
    return random.sample(questions, EXAM_TOTAL)


def run_interactive(exam):
    """Run an interactive practice exam."""
    correct = 0
    total = len(exam)
    wrong = []

    print(f"\n{'='*60}")
    print(f"  TECHNICIAN CLASS PRACTICE EXAM")
    print(f"  {total} questions — need {PASS_MARK} to pass")
    print(f"{'='*60}\n")

    for i, q in enumerate(exam, 1):
        print(f"Q{i}. [{q['id']}] {q['question']}")
        # Show figure reference for schematic questions
        fig = figure_for(q)
        if fig:
            print(f"    📎 See figures/{fig}")
        letters = sorted(q["answers"].keys())
        for letter in letters:
            print(f"    {letter}) {q['answers'][letter]}")

        while True:
            try:
                answer = input(f"\n  Your answer (A/B/C/D or Q to quit): ").strip().upper()
            except EOFError:
                answer = "Q"
            if answer == "Q":
                print(f"\nQuitting. {correct}/{i-1} correct so far.")
                return correct, i - 1, wrong
            if answer in ["A", "B", "C", "D"]:
                break
            print("  Enter A, B, C, or D")

        if answer == q["correct"]:
            correct += 1
            print(f"  ✅ Correct!\n")
        else:
            wrong.append(q)
            print(f"  ❌ Wrong — correct answer is {q['correct']}) {q['answers'][q['correct']]}\n")

    return correct, total, wrong


def run_quick(exam):
    """Show all questions with answers revealed."""
    print(f"\n{'='*60}")
    print(f"  PRACTICE EXAM — ANSWER KEY")
    print(f"{'='*60}\n")

    for i, q in enumerate(exam, 1):
        print(f"Q{i}. [{q['id']}] {q['question']}")
        fig = figure_for(q)
        if fig:
            print(f"    📎 See figures/{fig}")
        letters = sorted(q["answers"].keys())
        for letter in letters:
            mark = " ✅" if letter == q["correct"] else ""
            print(f"    {letter}) {q['answers'][letter]}{mark}")
        print()


def show_stats(questions, subelements):
    """Show pool statistics."""
    print(f"\n{'='*60}")
    print(f"  QUESTION POOL STATISTICS")
    print(f"{'='*60}\n")

    by_sub = {}
    for q in questions:
        by_sub.setdefault(q["subelement"], []).append(q)

    print(f"  {'Sub':<5} {'Topic':<35} {'Pool':>5} {'Exam':>5}")
    print(f"  {'-'*55}")
    for sub in sorted(EXAM_DISTRIBUTION.keys()):
        name = subelements.get(sub, {}).get("name", "Unknown")
        pool_count = len(by_sub.get(sub, []))
        exam_count = EXAM_DISTRIBUTION[sub]
        print(f"  {sub:<5} {name:<35} {pool_count:>5} {exam_count:>5}")

    total_pool = sum(len(v) for v in by_sub.values())
    total_exam = sum(EXAM_DISTRIBUTION.values())
    print(f"  {'-'*55}")
    print(f"  {'Total':<41} {total_pool:>5} {total_exam:>5}")
    print(f"\n  Passing score: {PASS_MARK}/{EXAM_TOTAL} (74%)\n")


def print_results(correct, total, wrong):
    """Print exam results with subelement breakdown."""
    pct = (correct / total * 100) if total > 0 else 0
    passed = correct >= PASS_MARK

    print(f"\n{'='*60}")
    print(f"  RESULTS: {correct}/{total} ({pct:.0f}%)")
    print(f"  {'✅ PASSED!' if passed else '❌ Not yet — keep studying'}")
    print(f"{'='*60}")

    if wrong:
        # Group wrong answers by subelement
        by_sub = {}
        for q in wrong:
            by_sub.setdefault(q["subelement"], []).append(q)

        print(f"\n  Areas to review:")
        for sub in sorted(by_sub.keys()):
            count = len(by_sub[sub])
            print(f"    {sub}: {count} wrong")

    print()


def parse_args() -> tuple[bool, bool, bool, str | None]:
    """Parse CLI arguments. Returns (quick, stats, drill, pool_name)."""
    args = sys.argv[1:]
    quick = "--quick" in args
    stats = "--stats" in args
    drill = "--drill" in args
    pool_name = None
    if "--pool" in args:
        idx = args.index("--pool")
        if idx + 1 >= len(args):
            print("Error: --pool requires a value (e.g. 2026-2030)", file=sys.stderr)
            sys.exit(1)
        pool_name = args[idx + 1]
    return quick, stats, drill, pool_name


def main():
    quick, stats, drill, pool_arg = parse_args()

    pool_name, pool_path = resolve_pool(pool_arg)
    source = "current pool" if pool_arg is None else "specified via --pool"
    print(f"📡 Question pool: {pool_name} ({source})")

    questions, subelements = load_pool(pool_path)

    if stats:
        show_stats(questions, subelements)
        return

    exam = generate_drill(questions) if drill else generate_exam(questions)
    if drill:
        print("🎲 Drill mode: 35 random questions from the whole pool (not real exam layout)")

    if quick:
        run_quick(exam)
        return

    correct, total, wrong = run_interactive(exam)
    if total > 0:
        print_results(correct, total, wrong)


if __name__ == "__main__":
    main()
