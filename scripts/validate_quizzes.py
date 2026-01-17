#!/usr/bin/env python3
"""
Quiz Validation Script
Validates all quiz JSON files against the expected format for the web app.
"""

import json
import sys
from pathlib import Path
from typing import List, Tuple

# ANSI colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

REQUIRED_QUIZ_FIELDS = {"id", "lecture", "topic", "questions"}
OPTIONAL_QUIZ_FIELDS = {"source_pdf", "created"}

REQUIRED_QUESTION_FIELDS = {"id", "type", "question"}
OPTIONAL_QUESTION_FIELDS = {"topic", "slide_ref"}

VALID_QUESTION_TYPES = {"multiple_choice", "true_false", "short_answer"}


def validate_question(q: dict, quiz_id: str, q_idx: int) -> List[str]:
    """Validate a single question. Returns list of error messages."""
    errors = []
    prefix = f"Quiz '{quiz_id}', Question {q_idx + 1}"

    # Check required fields
    for field in REQUIRED_QUESTION_FIELDS:
        if field not in q:
            errors.append(f"{prefix}: Missing required field '{field}'")

    if "type" not in q:
        return errors  # Can't validate further without type

    q_type = q["type"]

    # Check valid question type
    if q_type not in VALID_QUESTION_TYPES:
        errors.append(f"{prefix}: Invalid question type '{q_type}'. Must be one of {VALID_QUESTION_TYPES}")
        return errors

    # Type-specific validation
    if q_type == "multiple_choice":
        if "options" not in q:
            errors.append(f"{prefix}: Multiple choice question missing 'options' array")
        elif not isinstance(q["options"], list):
            errors.append(f"{prefix}: 'options' must be an array")
        elif len(q["options"]) < 2:
            errors.append(f"{prefix}: Multiple choice needs at least 2 options, has {len(q['options'])}")
        elif len(q["options"]) > 6:
            errors.append(f"{prefix}: Multiple choice has {len(q['options'])} options (recommend 4)")

        if "correct" not in q:
            errors.append(f"{prefix}: Multiple choice question missing 'correct' index")
        elif not isinstance(q["correct"], int):
            errors.append(f"{prefix}: 'correct' must be an integer index, got {type(q['correct']).__name__}")
        elif "options" in q and isinstance(q["options"], list):
            if q["correct"] < 0 or q["correct"] >= len(q["options"]):
                errors.append(f"{prefix}: 'correct' index {q['correct']} out of range for {len(q['options'])} options")

    elif q_type == "true_false":
        if "correct" not in q:
            errors.append(f"{prefix}: True/false question missing 'correct' value")
        elif not isinstance(q["correct"], bool):
            errors.append(f"{prefix}: True/false 'correct' must be boolean, got {type(q['correct']).__name__}")

    elif q_type == "short_answer":
        if "expected_keywords" not in q:
            errors.append(f"{prefix}: Short answer question missing 'expected_keywords' array")
        elif not isinstance(q["expected_keywords"], list):
            errors.append(f"{prefix}: 'expected_keywords' must be an array")
        elif len(q["expected_keywords"]) == 0:
            errors.append(f"{prefix}: 'expected_keywords' is empty")

    # Check question text is non-empty
    if "question" in q and (not q["question"] or not q["question"].strip()):
        errors.append(f"{prefix}: Question text is empty")

    return errors


def validate_quiz(filepath: Path) -> Tuple[bool, List[str], dict]:
    """
    Validate a quiz file.
    Returns: (is_valid, error_messages, stats_dict)
    """
    errors = []
    stats = {"questions": 0, "mc": 0, "tf": 0, "sa": 0}

    try:
        with open(filepath) as f:
            quiz = json.load(f)
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON: {e}"], stats

    quiz_id = filepath.stem

    # Check required fields
    for field in REQUIRED_QUIZ_FIELDS:
        if field not in quiz:
            errors.append(f"Quiz '{quiz_id}': Missing required field '{field}'")

    # Validate quiz ID matches filename
    if "id" in quiz and quiz["id"] != quiz_id:
        errors.append(f"Quiz '{quiz_id}': ID in file ('{quiz['id']}') doesn't match filename")

    # Validate lecture format (should be like 'pcv5', 'pcv15', etc.)
    if "lecture" in quiz:
        lecture = quiz["lecture"]
        if not lecture or not lecture[0].isalpha():
            errors.append(f"Quiz '{quiz_id}': Invalid lecture format '{lecture}'")

    # Validate questions
    if "questions" not in quiz:
        return len(errors) == 0, errors, stats

    questions = quiz["questions"]
    if not isinstance(questions, list):
        errors.append(f"Quiz '{quiz_id}': 'questions' must be an array")
        return False, errors, stats

    stats["questions"] = len(questions)

    if len(questions) == 0:
        errors.append(f"Quiz '{quiz_id}': No questions in quiz")
    elif len(questions) < 5:
        errors.append(f"Quiz '{quiz_id}': Only {len(questions)} questions (recommend 10+)")

    # Check for duplicate question IDs
    q_ids = [q.get("id") for q in questions if "id" in q]
    if len(q_ids) != len(set(q_ids)):
        errors.append(f"Quiz '{quiz_id}': Duplicate question IDs detected")

    # Validate each question
    for idx, q in enumerate(questions):
        q_errors = validate_question(q, quiz_id, idx)
        errors.extend(q_errors)

        # Count question types
        q_type = q.get("type", "")
        if q_type == "multiple_choice":
            stats["mc"] += 1
        elif q_type == "true_false":
            stats["tf"] += 1
        elif q_type == "short_answer":
            stats["sa"] += 1

    return len(errors) == 0, errors, stats


def main():
    data_dir = Path(__file__).parent.parent / "server" / "data"

    if not data_dir.exists():
        print(f"{RED}Error: Data directory not found: {data_dir}{RESET}")
        sys.exit(1)

    quiz_files = sorted(data_dir.glob("*.json"))

    if not quiz_files:
        print(f"{YELLOW}No quiz files found in {data_dir}{RESET}")
        sys.exit(0)

    print(f"{BOLD}Quiz Validation Report{RESET}")
    print("=" * 50)
    print()

    total_quizzes = 0
    valid_quizzes = 0
    total_questions = 0
    total_mc = 0
    total_tf = 0
    total_sa = 0
    all_errors = []

    for filepath in quiz_files:
        is_valid, errors, stats = validate_quiz(filepath)
        total_quizzes += 1
        total_questions += stats["questions"]
        total_mc += stats["mc"]
        total_tf += stats["tf"]
        total_sa += stats["sa"]

        if is_valid:
            valid_quizzes += 1
        else:
            all_errors.extend(errors)

    # Summary
    if valid_quizzes == total_quizzes:
        print(f"{GREEN}✓ All {total_quizzes} quizzes are valid!{RESET}")
    else:
        print(f"{RED}✗ {total_quizzes - valid_quizzes}/{total_quizzes} quizzes have errors{RESET}")

    print()
    print(f"{BOLD}Statistics:{RESET}")
    print(f"  Total quizzes:     {total_quizzes}")
    print(f"  Valid quizzes:     {valid_quizzes}")
    print(f"  Total questions:   {total_questions}")
    print(f"  Multiple choice:   {total_mc} ({total_mc/total_questions*100:.1f}%)" if total_questions else "")
    print(f"  True/False:        {total_tf} ({total_tf/total_questions*100:.1f}%)" if total_questions else "")
    print(f"  Short answer:      {total_sa} ({total_sa/total_questions*100:.1f}%)" if total_questions else "")

    if all_errors:
        print()
        print(f"{BOLD}{RED}Errors:{RESET}")
        for error in all_errors[:20]:  # Show first 20 errors
            print(f"  {RED}•{RESET} {error}")
        if len(all_errors) > 20:
            print(f"  ... and {len(all_errors) - 20} more errors")

    print()

    # Exit with error code if validation failed
    sys.exit(0 if valid_quizzes == total_quizzes else 1)


if __name__ == "__main__":
    main()
