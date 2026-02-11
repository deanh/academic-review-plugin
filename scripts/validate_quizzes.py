#!/usr/bin/env python3
"""
Quiz Validation Script
Validates question pool JSON files and checks for answer position bias.

Usage: python scripts/validate_quizzes.py
"""

import json
import sys
from pathlib import Path

# ANSI colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

REQUIRED_QUESTION_FIELDS = {"id", "type", "question"}
VALID_QUESTION_TYPES = {"multiple_choice", "true_false"}

BIAS_THRESHOLD = 0.40  # Warn if any position has > 40% of correct answers


def validate_question(q: dict, file_name: str, q_idx: int):
    """Validate a single question. Returns list of error messages."""
    errors = []
    prefix = f"{file_name}, Q{q_idx + 1} ({q.get('id', '?')})"

    for field in REQUIRED_QUESTION_FIELDS:
        if field not in q:
            errors.append(f"{prefix}: Missing required field '{field}'")

    if "type" not in q:
        return errors

    q_type = q["type"]

    if q_type not in VALID_QUESTION_TYPES:
        errors.append(f"{prefix}: Invalid type '{q_type}'. Must be one of {VALID_QUESTION_TYPES}")
        return errors

    if q_type == "multiple_choice":
        if "options" not in q:
            errors.append(f"{prefix}: Missing 'options' array")
        elif not isinstance(q["options"], list):
            errors.append(f"{prefix}: 'options' must be an array")
        elif len(q["options"]) < 2:
            errors.append(f"{prefix}: Needs at least 2 options, has {len(q['options'])}")
        elif len(q["options"]) > 6:
            errors.append(f"{prefix}: Has {len(q['options'])} options (max 6)")

        if "correct" not in q:
            errors.append(f"{prefix}: Missing 'correct' index")
        elif not isinstance(q["correct"], int):
            errors.append(f"{prefix}: 'correct' must be int, got {type(q['correct']).__name__}")
        elif "options" in q and isinstance(q["options"], list):
            if q["correct"] < 0 or q["correct"] >= len(q["options"]):
                errors.append(f"{prefix}: 'correct' index {q['correct']} out of range for {len(q['options'])} options")

    elif q_type == "true_false":
        if "correct" not in q:
            errors.append(f"{prefix}: Missing 'correct' value")
        elif not isinstance(q["correct"], bool):
            errors.append(f"{prefix}: 'correct' must be boolean, got {type(q['correct']).__name__}")

    if "question" in q and (not q["question"] or not q["question"].strip()):
        errors.append(f"{prefix}: Question text is empty")

    return errors


def check_position_bias(position_counts: dict, total_mc: int):
    """Check for answer position bias. Returns list of warnings."""
    warnings = []
    if total_mc < 10:
        return warnings

    for pos, count in sorted(position_counts.items()):
        ratio = count / total_mc
        if ratio > BIAS_THRESHOLD:
            warnings.append(
                f"Position {pos} has {count}/{total_mc} correct answers "
                f"({ratio:.0%}) - exceeds {BIAS_THRESHOLD:.0%} threshold"
            )

    return warnings


def main():
    questions_dir = Path(__file__).parent.parent / "server" / "data" / "questions"

    if not questions_dir.exists():
        print(f"{RED}Error: Questions directory not found: {questions_dir}{RESET}")
        sys.exit(1)

    # Find all question pool files across all courses
    pool_files = sorted(questions_dir.glob("**/*.json"))

    if not pool_files:
        print(f"{YELLOW}No question files found in {questions_dir}{RESET}")
        sys.exit(0)

    print(f"{BOLD}Question Pool Validation Report{RESET}")
    print("=" * 50)
    print()

    total_files = 0
    valid_files = 0
    total_questions = 0
    total_mc = 0
    total_tf = 0
    all_errors = []
    all_ids = set()
    duplicate_ids = []

    # Global position bias tracking
    position_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    # Per-file position tracking
    per_file_positions = {}

    for filepath in pool_files:
        total_files += 1
        file_name = f"{filepath.parent.name}/{filepath.name}"
        file_errors = []
        file_positions = {0: 0, 1: 0, 2: 0, 3: 0}
        file_mc = 0

        try:
            with open(filepath) as f:
                questions = json.load(f)
        except json.JSONDecodeError as e:
            all_errors.append(f"{file_name}: Invalid JSON: {e}")
            continue

        if not isinstance(questions, list):
            all_errors.append(f"{file_name}: Must be a JSON array of questions")
            continue

        if len(questions) == 0:
            all_errors.append(f"{file_name}: Empty question array")
            continue

        for idx, q in enumerate(questions):
            q_errors = validate_question(q, file_name, idx)
            file_errors.extend(q_errors)

            # Track IDs for global duplicate check
            q_id = q.get("id")
            if q_id:
                if q_id in all_ids:
                    duplicate_ids.append(f"{file_name}: Duplicate ID '{q_id}'")
                all_ids.add(q_id)

            q_type = q.get("type", "")
            if q_type == "multiple_choice":
                total_mc += 1
                file_mc += 1
                correct = q.get("correct", 0)
                if isinstance(correct, int) and 0 <= correct <= 3:
                    position_counts[correct] += 1
                    file_positions[correct] += 1
            elif q_type == "true_false":
                total_tf += 1

        total_questions += len(questions)

        if file_errors:
            all_errors.extend(file_errors)
        else:
            valid_files += 1

        if file_mc > 0:
            per_file_positions[file_name] = (file_positions, file_mc)

    # Print results
    if valid_files == total_files and not duplicate_ids:
        print(f"{GREEN}All {total_files} question files are valid!{RESET}")
    else:
        print(f"{RED}{total_files - valid_files}/{total_files} files have errors{RESET}")

    print()
    print(f"{BOLD}Statistics:{RESET}")
    print(f"  Question files:    {total_files}")
    print(f"  Total questions:   {total_questions}")
    if total_questions:
        print(f"  Multiple choice:   {total_mc} ({total_mc/total_questions*100:.1f}%)")
        print(f"  True/False:        {total_tf} ({total_tf/total_questions*100:.1f}%)")

    # Position bias check
    print()
    print(f"{BOLD}Answer Position Distribution:{RESET}")
    if total_mc > 0:
        for pos in sorted(position_counts):
            count = position_counts[pos]
            ratio = count / total_mc
            bar = "#" * int(ratio * 40)
            indicator = f" {YELLOW}<--{RESET}" if ratio > BIAS_THRESHOLD else ""
            print(f"  Position {pos}: {count:3d} ({ratio:5.1%}) {bar}{indicator}")

        bias_warnings = check_position_bias(position_counts, total_mc)
        if bias_warnings:
            print()
            print(f"{BOLD}{YELLOW}Answer Position Bias Detected:{RESET}")
            for w in bias_warnings:
                print(f"  {YELLOW}!{RESET} {w}")
            print(f"  {YELLOW}!{RESET} Run: python scripts/fix_bias.py to shuffle answers")
            print(f"  {YELLOW}!{RESET} Server shuffles at serving time, but source files should be fixed")

    if duplicate_ids:
        print()
        print(f"{BOLD}{RED}Duplicate IDs:{RESET}")
        for d in duplicate_ids[:10]:
            print(f"  {RED}*{RESET} {d}")

    if all_errors:
        print()
        print(f"{BOLD}{RED}Errors:{RESET}")
        for error in all_errors[:20]:
            print(f"  {RED}*{RESET} {error}")
        if len(all_errors) > 20:
            print(f"  ... and {len(all_errors) - 20} more errors")

    print()

    has_errors = valid_files < total_files or duplicate_ids
    has_bias = bool(check_position_bias(position_counts, total_mc))
    sys.exit(2 if has_bias else (1 if has_errors else 0))


if __name__ == "__main__":
    main()
