#!/usr/bin/env python3
"""
Quiz Server - Flask application for serving academic quizzes.
Deploy to: /var/www/quizzes/server.py
"""

import json
import os
from datetime import datetime
from pathlib import Path

from flask import Flask, jsonify, render_template, request, abort

app = Flask(__name__)

# Configuration
DATA_DIR = Path(__file__).parent / "data"
RESULTS_DIR = Path(__file__).parent / "results"

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
RESULTS_DIR.mkdir(exist_ok=True)


def load_quiz(quiz_id: str) -> dict | None:
    """Load a quiz by ID."""
    quiz_file = DATA_DIR / f"{quiz_id}.json"
    if quiz_file.exists():
        with open(quiz_file) as f:
            return json.load(f)
    return None


def list_quizzes() -> list[dict]:
    """List all available quizzes."""
    quizzes = []
    for quiz_file in DATA_DIR.glob("*.json"):
        try:
            with open(quiz_file) as f:
                quiz = json.load(f)
                quizzes.append({
                    "id": quiz.get("id", quiz_file.stem),
                    "lecture": quiz.get("lecture", "Unknown"),
                    "topic": quiz.get("topic", "Unknown"),
                    "num_questions": len(quiz.get("questions", [])),
                    "created": quiz.get("created", "Unknown")
                })
        except (json.JSONDecodeError, KeyError):
            continue
    # Sort by creation date, newest first
    quizzes.sort(key=lambda x: x.get("created", ""), reverse=True)
    return quizzes


def extract_course(lecture: str) -> str:
    """Extract course code from lecture string (e.g., 'pcv5' -> 'PCV')."""
    import re
    match = re.match(r'^([a-zA-Z]+)', lecture)
    return match.group(1).upper() if match else "OTHER"


def group_quizzes_by_course_and_lecture(quizzes: list[dict], completed: set[str]) -> dict:
    """
    Group quizzes hierarchically by course and lecture.
    Returns: {
        'PCV': {
            'lectures': {
                'pcv5': {'name': 'pcv5', 'quizzes': [...], 'completed': 2, 'total': 3},
                ...
            },
            'completed': 5,
            'total': 10
        },
        ...
    }
    """
    courses = {}

    for quiz in quizzes:
        quiz["completed"] = quiz["id"] in completed
        course = extract_course(quiz["lecture"])
        lecture = quiz["lecture"]

        if course not in courses:
            courses[course] = {"lectures": {}, "completed": 0, "total": 0}

        if lecture not in courses[course]["lectures"]:
            courses[course]["lectures"][lecture] = {
                "name": lecture,
                "quizzes": [],
                "completed": 0,
                "total": 0
            }

        courses[course]["lectures"][lecture]["quizzes"].append(quiz)
        courses[course]["lectures"][lecture]["total"] += 1
        courses[course]["total"] += 1

        if quiz["completed"]:
            courses[course]["lectures"][lecture]["completed"] += 1
            courses[course]["completed"] += 1

    # Sort lectures within each course by lecture number
    for course in courses.values():
        course["lectures"] = dict(
            sorted(course["lectures"].items(),
                   key=lambda x: (x[0], x[1]["quizzes"][0]["created"] if x[1]["quizzes"] else ""))
        )

    # Sort courses alphabetically
    return dict(sorted(courses.items()))


def get_completed_quizzes() -> set[str]:
    """Get set of quiz IDs that have been completed."""
    completed = set()
    for result_file in RESULTS_DIR.glob("*_result.json"):
        # Extract quiz_id from filename (e.g., "pcv5_dlt_result.json" -> "pcv5_dlt")
        quiz_id = result_file.stem.replace("_result", "")
        completed.add(quiz_id)
    return completed


@app.route("/")
def index():
    """List all available quizzes grouped by course and lecture."""
    quizzes = list_quizzes()
    completed = get_completed_quizzes()
    courses = group_quizzes_by_course_and_lecture(quizzes, completed)
    return render_template("index.html", courses=courses)


@app.route("/quiz/<quiz_id>")
def take_quiz(quiz_id: str):
    """Render the quiz-taking interface."""
    quiz = load_quiz(quiz_id)
    if not quiz:
        abort(404, description="Quiz not found")

    # Remove correct answers from questions sent to client
    client_quiz = {
        "id": quiz["id"],
        "lecture": quiz.get("lecture", ""),
        "topic": quiz.get("topic", ""),
        "questions": []
    }
    for q in quiz.get("questions", []):
        client_q = {
            "id": q["id"],
            "type": q["type"],
            "question": q["question"],
            "topic": q.get("topic", ""),
        }
        if q["type"] == "multiple_choice":
            client_q["options"] = q["options"]
        client_quiz["questions"].append(client_q)

    return render_template("quiz.html", quiz=client_quiz)


@app.route("/quiz/<quiz_id>/submit", methods=["POST"])
def submit_quiz(quiz_id: str):
    """Submit quiz answers and save results."""
    quiz = load_quiz(quiz_id)
    if not quiz:
        abort(404, description="Quiz not found")

    data = request.get_json()
    if not data or "answers" not in data:
        abort(400, description="Invalid submission")

    # Build result with scoring
    result = {
        "quiz_id": quiz_id,
        "completed": datetime.utcnow().isoformat() + "Z",
        "answers": [],
        "score": 0,
        "total": len(quiz["questions"])
    }

    # Create answer lookup
    answers_by_id = {a["question_id"]: a for a in data["answers"]}

    for q in quiz["questions"]:
        answer_data = answers_by_id.get(q["id"], {})
        answer_record = {
            "question_id": q["id"],
            "topic": q.get("topic", ""),
            "slide_ref": q.get("slide_ref", ""),
            "type": q["type"],
        }

        if q["type"] == "multiple_choice":
            selected = answer_data.get("selected")
            answer_record["selected"] = selected
            answer_record["correct_index"] = q["correct"]
            answer_record["is_correct"] = selected == q["correct"]
            if answer_record["is_correct"]:
                result["score"] += 1

        elif q["type"] == "true_false":
            selected = answer_data.get("selected")
            answer_record["selected"] = selected
            answer_record["correct_value"] = q["correct"]
            answer_record["is_correct"] = selected == q["correct"]
            if answer_record["is_correct"]:
                result["score"] += 1

        elif q["type"] == "short_answer":
            text = answer_data.get("text", "")
            answer_record["text"] = text
            # Check for expected keywords (case-insensitive)
            keywords = q.get("expected_keywords", [])
            found = sum(1 for kw in keywords if kw.lower() in text.lower())
            answer_record["keywords_found"] = found
            answer_record["keywords_expected"] = len(keywords)
            # Partial credit for short answers
            if keywords and found >= len(keywords) // 2:
                result["score"] += 1
                answer_record["is_correct"] = found == len(keywords)
            else:
                answer_record["is_correct"] = False

        answer_record["time_spent_sec"] = answer_data.get("time_spent_sec", 0)
        result["answers"].append(answer_record)

    result["total_time_sec"] = data.get("total_time_sec", 0)
    result["percentage"] = round(result["score"] / result["total"] * 100) if result["total"] > 0 else 0

    # Save result
    result_file = RESULTS_DIR / f"{quiz_id}_result.json"
    with open(result_file, "w") as f:
        json.dump(result, f, indent=2)

    return jsonify({
        "success": True,
        "score": result["score"],
        "total": result["total"],
        "percentage": result["percentage"]
    })


@app.route("/api/quizzes")
def api_list_quizzes():
    """API endpoint to list quizzes."""
    return jsonify(list_quizzes())


@app.route("/api/quiz/<quiz_id>")
def api_get_quiz(quiz_id: str):
    """API endpoint to get quiz details (without answers)."""
    quiz = load_quiz(quiz_id)
    if not quiz:
        abort(404)
    # Strip correct answers
    for q in quiz.get("questions", []):
        q.pop("correct", None)
        q.pop("expected_keywords", None)
    return jsonify(quiz)


if __name__ == "__main__":
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5050
    app.run(host="0.0.0.0", port=port, debug=True)
