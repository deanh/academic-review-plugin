#!/bin/bash
# Show quiz generation and completion status
# Usage: ./scripts/quiz_status.sh

# Find project root
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

EXTRACTED_DIR="$PROJECT_ROOT/.cache/extracted"
QUIZ_DIR="$PROJECT_ROOT/server/data"
RESULTS_DIR="$PROJECT_ROOT/server/results"

# Colors
BOLD='\033[1m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
DIM='\033[2m'
RESET='\033[0m'

# Build list of lectures from JSON metadata
get_all_lectures() {
    if [ -d "$EXTRACTED_DIR" ]; then
        for json_file in "$EXTRACTED_DIR"/*.json; do
            [ -f "$json_file" ] || continue
            pdf_name=$(grep '"pdf_name"' "$json_file" | sed 's/.*: *"\([^"]*\)".*/\1/')
            # Extract lecture ID (e.g., pcv6 from pcv6_WS2526_homography.pdf)
            echo "$pdf_name" | sed 's/_.*//; s/\.pdf//'
        done | sort -u
    fi
}

# Get unique courses from lectures
get_courses() {
    get_all_lectures | sed 's/[0-9].*//' | sort -u
}

# Get lectures for a course
get_lectures_for_course() {
    local course=$1
    get_all_lectures | grep "^${course}[0-9]" | sort -V
}

# Normalize lecture ID to zero-padded format (pcv1 -> pcv01)
normalize_lecture() {
    local lecture=$1
    echo "$lecture" | sed 's/^\([a-z]*\)\([0-9]\)$/\10\2/'
}

# Count quizzes for a lecture
count_quizzes() {
    local lecture=$1
    local normalized=$(normalize_lecture "$lecture")
    if [ -d "$QUIZ_DIR" ]; then
        # Try both original and normalized names (avoid double-counting)
        count1=$(ls "$QUIZ_DIR" 2>/dev/null | grep "^${lecture}_" | wc -l | tr -d ' ')
        if [ "$normalized" != "$lecture" ]; then
            count2=$(ls "$QUIZ_DIR" 2>/dev/null | grep "^${normalized}_" | wc -l | tr -d ' ')
        else
            count2=0
        fi
        echo $((count1 + count2))
    else
        echo "0"
    fi
}

# Count completed quizzes for a lecture
count_completed() {
    local lecture=$1
    local normalized=$(normalize_lecture "$lecture")
    if [ -d "$RESULTS_DIR" ]; then
        # Try both original and normalized names (avoid double-counting)
        count1=$(ls "$RESULTS_DIR" 2>/dev/null | grep "^${lecture}_" | wc -l | tr -d ' ')
        if [ "$normalized" != "$lecture" ]; then
            count2=$(ls "$RESULTS_DIR" 2>/dev/null | grep "^${normalized}_" | wc -l | tr -d ' ')
        else
            count2=0
        fi
        echo $((count1 + count2))
    else
        echo "0"
    fi
}

# Main
echo ""
echo -e "${BOLD}Quiz Status${RESET}"
echo "==========="
echo ""

all_lectures=$(get_all_lectures)
if [ -z "$all_lectures" ]; then
    echo "No extracted lectures found in $EXTRACTED_DIR"
    exit 0
fi

courses=$(get_courses)
total_lectures=0
total_with_quizzes=0
total_quizzes=0
total_completed=0

for course in $courses; do
    course_upper=$(echo "$course" | tr '[:lower:]' '[:upper:]')
    lectures=$(get_lectures_for_course "$course")
    lecture_count=$(echo "$lectures" | wc -w | tr -d ' ')

    course_with_quizzes=0
    course_quizzes=0
    course_completed=0

    for lecture in $lectures; do
        qcount=$(count_quizzes "$lecture")
        ccount=$(count_completed "$lecture")
        if [ "$qcount" -gt 0 ]; then
            course_with_quizzes=$((course_with_quizzes + 1))
            course_quizzes=$((course_quizzes + qcount))
            course_completed=$((course_completed + ccount))
        fi
    done

    total_lectures=$((total_lectures + lecture_count))
    total_with_quizzes=$((total_with_quizzes + course_with_quizzes))
    total_quizzes=$((total_quizzes + course_quizzes))
    total_completed=$((total_completed + course_completed))

    echo -e "${BOLD}${course_upper}${RESET} - ${lecture_count} lectures, ${course_with_quizzes} with quizzes"

    # Show details for lectures with quizzes
    for lecture in $lectures; do
        qcount=$(count_quizzes "$lecture")
        ccount=$(count_completed "$lecture")
        if [ "$qcount" -gt 0 ]; then
            if [ "$ccount" -eq "$qcount" ]; then
                echo -e "  ${GREEN}${lecture}${RESET}: ${qcount} quizzes (${GREEN}all done${RESET})"
            elif [ "$ccount" -gt 0 ]; then
                echo -e "  ${YELLOW}${lecture}${RESET}: ${qcount} quizzes (${ccount} done)"
            else
                echo -e "  ${lecture}: ${qcount} quizzes"
            fi
        fi
    done

    # Show lectures without quizzes (collapsed)
    no_quiz_lectures=""
    for lecture in $lectures; do
        qcount=$(count_quizzes "$lecture")
        if [ "$qcount" -eq 0 ]; then
            if [ -z "$no_quiz_lectures" ]; then
                no_quiz_lectures="$lecture"
            else
                no_quiz_lectures="$no_quiz_lectures, $lecture"
            fi
        fi
    done

    if [ -n "$no_quiz_lectures" ]; then
        echo -e "  ${DIM}No quizzes: ${no_quiz_lectures}${RESET}"
    fi

    echo ""
done

# Summary
echo "==========="
echo -e "${BOLD}Summary${RESET}"
echo "  Lectures: ${total_with_quizzes}/${total_lectures} have quizzes"
echo "  Quizzes: ${total_quizzes} total, ${total_completed} completed"
echo ""
