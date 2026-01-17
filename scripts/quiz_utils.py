#!/usr/bin/env python3
"""
Quiz generation utilities.
Usage: Import and use in quiz generation, or run directly to test.
"""

import random


def shuffle_options(options: list[str], correct_index: int) -> tuple[list[str], int]:
    """
    Shuffle multiple choice options and return new correct index.

    Args:
        options: List of answer options (e.g., ["4", "6", "8", "9"])
        correct_index: Index of correct answer in original list

    Returns:
        Tuple of (shuffled_options, new_correct_index)

    Example:
        >>> options = ["Wrong A", "Wrong B", "Correct", "Wrong C"]
        >>> shuffled, new_idx = shuffle_options(options, correct_index=2)
        >>> shuffled[new_idx]
        'Correct'
    """
    correct_answer = options[correct_index]
    shuffled = options.copy()
    random.shuffle(shuffled)
    new_index = shuffled.index(correct_answer)
    return shuffled, new_index


def create_mc_question(
    question: str,
    correct: str,
    distractors: list[str],
    **kwargs
) -> dict:
    """
    Create a multiple choice question with randomized option order.

    Args:
        question: The question text
        correct: The correct answer
        distractors: List of incorrect answers (typically 3)
        **kwargs: Additional fields (id, topic, slide_ref, etc.)

    Returns:
        Question dict with shuffled options and correct index

    Example:
        >>> q = create_mc_question(
        ...     question="How many DOF does a 2D homography have?",
        ...     correct="8",
        ...     distractors=["4", "6", "9"],
        ...     id="q1",
        ...     topic="degrees_of_freedom",
        ...     slide_ref="Slide 3"
        ... )
        >>> q["options"][q["correct"]]
        '8'
    """
    all_options = [correct] + distractors
    shuffled, correct_idx = shuffle_options(all_options, 0)

    return {
        "type": "multiple_choice",
        "question": question,
        "options": shuffled,
        "correct": correct_idx,
        **kwargs
    }


if __name__ == "__main__":
    # Test the utilities
    print("Testing shuffle_options:")
    options = ["A (wrong)", "B (wrong)", "C (correct)", "D (wrong)"]
    for i in range(5):
        shuffled, idx = shuffle_options(options, correct_index=2)
        print(f"  Run {i+1}: correct at index {idx} -> {shuffled}")

    print("\nTesting create_mc_question:")
    q = create_mc_question(
        question="How many DOF does a 2D homography have?",
        correct="8",
        distractors=["4", "6", "9"],
        id="q1",
        topic="degrees_of_freedom"
    )
    print(f"  Options: {q['options']}")
    print(f"  Correct index: {q['correct']}")
    print(f"  Correct answer: {q['options'][q['correct']]}")
