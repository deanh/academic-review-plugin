---
name: academic-review
description: Interactive review sessions with academic PDFs (lectures, research papers, book chapters). Extract concepts, run Q&A sessions, generate quizzes with scoring. Preserves mathematical formulas in LaTeX format. Privacy-preserving local processing - PDFs never uploaded. Use when studying academic materials, reviewing research, or preparing for exams.
allowed-tools: Read, Glob, Bash(python:*)
---

# Academic Review Skill

## Overview

This skill enables interactive review sessions with **academic PDFs** while **preserving your privacy**. All PDF processing happens locally on your machine using the Marker library - PDFs are never sent to Anthropic servers. Only extracted text (with LaTeX formulas) is used in our conversation.

**Supported Document Types:**
- **Lecture Slides**: Review presentations, generate quizzes, Q&A on concepts
- **Research Papers**: Analyze methodology, results, and discussion sections
- **Book Chapters**: Study concepts, work through examples and exercises

**Key Features:**
- **Privacy-preserving**: PDFs processed locally, never uploaded
- **Math-aware**: Formulas preserved in LaTeX format (e.g., `$E = mc^2$`, `$$\int_a^b f(x)dx$$`)
- **Cached extraction**: First extraction is slow, subsequent access is instant
- **Two review modes**: Q&A (free-form questions) and Quiz (auto-generated questions with scoring)
- **Visual fallback**: Can extract specific pages as images for complex diagrams

## Document Type Detection

When starting a review session, **identify the document type** from context:

**Lectures** - Indicators:
- File names with "lecture", "slides", "presentation"
- Bullet-point heavy content
- Sequential slide numbers
- Course/semester codes (e.g., "CS229_Lecture05.pdf")

**Research Papers** - Indicators:
- File names with "paper", author names, conference/journal codes
- Standard sections: Abstract, Introduction, Methods, Results, Discussion, References
- Citations and bibliography
- Two-column format common

**Book Chapters** - Indicators:
- File names with "chapter", book titles
- Sections and subsections with numbered headings
- End-of-chapter exercises or problems
- Dense paragraph-based text

**Default approach**: If unclear, start with Q&A mode and adapt based on the content structure.

## Quick Start

### Starting a Review Session

When the user requests a review session:

1. **Find PDFs** using Glob: `**/*.pdf` or more specific patterns
2. **Identify document type** (lecture/paper/chapter) from filename and request
3. **Extract content** using the extraction script
4. **Ask mode preference**: "Would you like Q&A mode or Quiz mode?"
5. **Begin the selected mode** with document-type-appropriate approach

### Example Flow

```
User: "Review the SLAM paper by Smith et al."

Your actions:
1. Use Glob to find PDFs matching "smith" or "slam"
2. Identify as research paper
3. Run: python scripts/extract_pdf.py <pdf_path>
4. Read the cached markdown file
5. Ask: "Q&A mode or Quiz mode?"
6. Begin selected mode (adapt to paper structure)
```

## Review Modes

### Q&A Mode (Free-Form Questions)

**Purpose**: Answer user's specific questions about content with detailed explanations.

**How to conduct Q&A mode:**

1. **Load and parse content**:
   ```bash
   # Extract PDF (or use cached version)
   python scripts/extract_pdf.py /path/to/document.pdf
   ```
   Then read the output markdown file using the Read tool.

2. **Present overview** (adapt to document type):

   **For Lectures**:
   - List main topics covered
   - Highlight key formulas (show in LaTeX)
   - Mention important definitions or concepts

   Example:
   ```
   📚 Lecture Overview: Epipolar Geometry

   This lecture covers 45 slides on:
   - Epipolar constraint: $x'^T F x = 0$
   - Fundamental matrix $F$ (3x3, rank 2)
   - Essential matrix $E = K'^T F K$
   - Applications: stereo vision, 3D reconstruction

   Ask me anything about these topics, or say "quiz" to switch to quiz mode.
   ```

   **For Research Papers**:
   - Summarize the research question/contribution
   - Key methodology and approach
   - Main results and conclusions
   - Important formulas or algorithms

   Example:
   ```
   📄 Paper Overview: "ORB-SLAM2: Real-Time SLAM for Monocular, Stereo and RGB-D Cameras"

   **Research Question**: How to build a complete SLAM system that works across multiple camera types?

   **Key Contributions**:
   - Unified SLAM system for monocular, stereo, and RGB-D cameras
   - Place recognition and loop closing
   - Real-time performance on standard CPUs

   **Methods**: ORB features, bag-of-words place recognition, pose graph optimization

   **Results**: Evaluated on KITTI and TUM datasets, outperforms previous methods

   Ask me about methodology, results, or implementation details.
   ```

   **For Book Chapters**:
   - Main concepts introduced
   - Theorems or key results
   - Important formulas
   - Example problems covered

   Example:
   ```
   📖 Chapter Overview: "Matrix Decompositions" (Chapter 7)

   **Topics Covered**:
   - Singular Value Decomposition (SVD): $A = U\Sigma V^T$
   - Eigenvalue decomposition: $A = Q\Lambda Q^T$
   - QR decomposition and applications
   - Least squares via matrix decompositions

   **Key Theorems**: Spectral theorem, SVD existence

   **Exercises**: 15 problems on computing decompositions and applications

   Ask me about concepts, work through examples, or get help with exercises.
   ```

3. **Answer questions**:
   - Reference specific page/section numbers
   - Show formulas in LaTeX format
   - Explain concepts with examples
   - Connect related topics
   - If user asks about a diagram, offer to extract that page as an image

4. **Track progress**:
   - Note which topics user asks about
   - Identify apparent knowledge gaps
   - Suggest related concepts proactively

**Document-specific guidance:**

**Lectures**: Focus on concept understanding, derivations, applications
**Papers**: Focus on methodology critique, results interpretation, reproducibility
**Chapters**: Focus on theorem understanding, example walkthrough, exercise solving

### Quiz Mode (Auto-Generated Questions)

**Purpose**: Test user's knowledge with auto-generated questions, provide scoring and feedback.

**How to conduct Quiz mode:**

1. **Load and analyze content**:
   ```bash
   # Extract PDF (or use cached version)
   python scripts/extract_pdf.py /path/to/document.pdf
   ```
   Read the markdown and analyze:
   - Key concepts and definitions
   - Important formulas (in LaTeX)
   - Learning objectives
   - Example problems

2. **Generate questions** (default: 10, but ask user for preference):

   **For Lectures**:
   - **Multiple choice**: Test understanding of concepts
   - **True/False**: Quick concept checks
   - **Short answer**: Define terms or explain relationships
   - **Formula problems**: Apply equations to scenarios

   **For Research Papers**:
   - **Multiple choice**: Methodology choices, experimental design
   - **True/False**: Claims about results or methods
   - **Short answer**: Explain key contributions, limitations
   - **Analysis questions**: Critique methods or interpret results

   **For Book Chapters**:
   - **Multiple choice**: Theorem conditions, concept understanding
   - **True/False**: Mathematical statements
   - **Short answer**: Prove simple results, explain concepts
   - **Problems**: Similar to end-of-chapter exercises

   Mix question types and topics proportionally. Order by difficulty (easier first).

3. **Present questions one at a time**:
   ```
   Quiz Mode - 10 Questions
   Score: 0/0

   Question 1 of 10 [Multiple Choice]
   What is the rank of the Fundamental matrix $F$?

   a) 1
   b) 2
   c) 3
   d) 4

   Your answer:
   ```

4. **Evaluate and provide feedback**:
   ```
   ✓ Correct! [+1 point]

   The Fundamental matrix $F$ has rank 2, which means det($F$) = 0. This constraint
   arises from the fact that $F$ maps points to epipolar lines, and the mapping has
   a one-dimensional null space.

   Score: 1/1 (100%)

   Question 2 of 10...
   ```

   For incorrect answers:
   ```
   ✗ Incorrect [+0 points]
   Your answer: a) 1
   Correct answer: b) 2

   The Fundamental matrix has rank 2, not 1. The rank-2 constraint (det($F$) = 0)
   is one of the key properties used in estimating $F$ from point correspondences.

   Score: 1/2 (50%)

   Question 3 of 10...
   ```

5. **End with summary**:
   ```
   📊 Quiz Complete!

   Final Score: 8/10 (80%) - B

   ✓ Topics Mastered:
   - Epipolar constraint
   - Essential matrix properties
   - Stereo reconstruction basics

   ⚠️ Topics to Review:
   - Fundamental matrix estimation (8-point algorithm)
   - RANSAC for outlier rejection

   Would you like to:
   1. Review the topics you missed in Q&A mode?
   2. Take another quiz on the same material?
   3. Move to a different document?
   ```

**Scoring Guidelines:**
- Multiple choice: 1 point for correct answer
- True/False: 1 point for correct answer
- Short answer: 1 point if answer captures key concept (be flexible)
- Formula problems: 1 point for correct answer, 0.5 for correct approach but calculation error

### Quiz Logging

**IMPORTANT**: At the end of every quiz, **automatically create a log file** without prompting.

**File location**: `.cache/quiz-logs/YYYY-MM-DD_pcv{N}_{topic}.md`

Example: `.cache/quiz-logs/2026-01-13_pcv05_DLT.md`

**During the quiz, track**:
- Which slide/page each question sources from (use `_page_N_` markers in extracted content)
- Student's reasoning when provided
- Specific knowledge gaps revealed by incorrect answers

**Log file structure**:

1. **YAML frontmatter**: date, lecture number, topic, source PDF path, cache hash, score, percentage
2. **Performance summary table**: score, grade, date
3. **Mastered topics table**: topic, question numbers, slide references, notes on understanding
4. **Topics needing review table**: topic, question numbers, slide references, specific knowledge gap
5. **Question-by-question detail**: Full detail for each question, especially reasoning and gaps for incorrect answers
6. **Study recommendations**: Prioritized list for next session
7. **Machine-readable metadata block**: YAML block with topics_covered, weak_topics, strong_topics arrays

**Slide reference format**:
- Extract page number from `_page_N_` markers in the cached markdown
- Reference as "Slide N" or "Slides N-M" for ranges
- Include content description (e.g., "Slide 3, transformation DOF table")

**Example log file**:

```markdown
---
date: 2026-01-13
lecture: pcv05
topic: Direct Linear Transformation (DLT)
source_pdf: lectures/PCV/pcv05_WS2526_DLT.pdf
cache_hash: c57edf3d7baf5f7d
score: 9/10
percentage: 90
grade: A
---

# Quiz Log: PCV Lecture 5 - DLT

## Performance Summary
| Metric | Value |
|--------|-------|
| Score | 9/10 (90%) |
| Grade | A |
| Date | 2026-01-13 |

## Topics Assessed

### Mastered Topics
| Topic | Questions | Slide References | Notes |
|-------|-----------|------------------|-------|
| Degrees of freedom | Q1 | Slide 3 (transformation table) | Understood 8 DOF = 9 elements - 1 scale |
| Point requirements | Q2 | Slides 16-17 | 4 points for 2D homography |

### Topics Needing Review
| Topic | Questions | Slide References | Specific Gap |
|-------|-----------|------------------|--------------|
| Conic transformation | Q8 | Slide 7 | Formula: C' = H^{-T}CH^{-1} |

## Question-by-Question Detail

### Q1: Degrees of Freedom [CORRECT]
- **Topic**: 2D transformation properties
- **Slide**: 3
- **Answer**: c) 8
- **Student reasoning**: "3x3 minus one for scaling"
- **Assessment**: Full understanding demonstrated

### Q8: Conic Transformation [INCORRECT]
- **Topic**: Transformation of geometric primitives
- **Slide**: 7
- **Correct answer**: C' = H^{-T}CH^{-1}
- **Student response**: "I'm not sure how conics are transformed"
- **Recommended review**: Review derivation from point incidence x^T C x = 0

## Study Recommendations for Next Session
1. **Priority**: Conic transformation formula and derivation
2. **Related topics to reinforce**: Dual conics (C*' = HC*H^T)

## Metadata for Future Processing
```yaml
session_type: quiz
question_count: 10
correct_count: 9
topics_covered:
  - degrees_of_freedom
  - point_requirements
  - conic_transformation
weak_topics:
  - conic_transformation
strong_topics:
  - degrees_of_freedom
  - point_requirements
```
```

**Purpose**: These logs enable future Claude instances to:
- Identify persistent weak areas across multiple sessions
- Recommend focused review before exams
- Track learning velocity and mastery progression
- Generate personalized study plans based on history

## Web Quiz System

The web quiz system allows pre-generating quizzes that can be taken on mobile devices (iPhone via Safari), with results synced back for Claude-assisted review.

### Architecture Overview

```
LOCAL                          SERVER                    MOBILE
─────────────────────────────────────────────────────────────────
Claude generates    rsync      Flask serves     Safari
quiz JSON files ──────────▶   quizzes      ◀─────────── iPhone
                                   │
.cache/web-quizzes/                │
                                   ▼
Claude reads       rsync      Results saved
results for    ◀──────────   as JSON files
review
.cache/quiz-results/
```

### Generating Web Quizzes

When user requests web quizzes, generate JSON files in `.cache/web-quizzes/`.

**File naming**: `{lecture}_{topic}_{date}.json`
Example: `pcv05_dlt_2026-01-14.json`

**Important**: Use zero-padded lecture numbers for single digits (pcv01-pcv09, not pcv1-pcv9). This ensures correct alphabetical sorting in file listings and the web UI.

**Quiz JSON Format** (IMPORTANT - use this exact structure):

```json
{
  "id": "pcv05_dlt_2026-01-14",
  "lecture": "pcv05",
  "topic": "Direct Linear Transformation",
  "source_pdf": "lectures/PCV/pcv05_WS2526_DLT.pdf",
  "cache_hash": "c57edf3d7baf5f7d",
  "created": "2026-01-14T10:30:00Z",
  "questions": [
    {
      "id": "q1",
      "type": "multiple_choice",
      "question": "How many DOF does a 2D projectivity have?",
      "options": ["4", "6", "8", "9"],
      "correct": 2,
      "slide_ref": "Slide 3",
      "topic": "degrees_of_freedom"
    },
    {
      "id": "q2",
      "type": "true_false",
      "question": "The DLT algorithm requires iterative optimization.",
      "correct": false,
      "slide_ref": "Slide 14",
      "topic": "dlt_properties"
    },
    {
      "id": "q3",
      "type": "short_answer",
      "question": "How are lines transformed under a homography H?",
      "expected_keywords": ["H^{-T}", "inverse transpose", "H^-T"],
      "slide_ref": "Slide 7",
      "topic": "line_transformation"
    }
  ]
}
```

**Question types**:
- `multiple_choice`: Include `options` array and `correct` (0-indexed)
- `true_false`: Include `correct` as boolean
- `short_answer`: Include `expected_keywords` array for partial matching

**Guidelines for generating questions**:
- Include 10-15 questions per quiz
- Mix question types (60% MC, 20% T/F, 20% short answer)
- Reference specific slides using `slide_ref`
- Tag each question with a `topic` for tracking
- **IMPORTANT**: Randomize correct answer positions (see utility below)
- Use ASCII for formulas in questions (e.g., "H^{-T}" not LaTeX)

### Answer Randomization Utility

To prevent answer position bias, use `scripts/quiz_utils.py` when generating multiple choice questions:

```python
from scripts.quiz_utils import shuffle_options, create_mc_question

# Method 1: Shuffle existing options
options = ["4", "6", "8", "9"]  # correct answer is "8" at index 2
shuffled, new_correct_idx = shuffle_options(options, correct_index=2)

# Method 2: Create question with automatic shuffling
question = create_mc_question(
    question="How many DOF does a 2D homography have?",
    correct="8",
    distractors=["4", "6", "9"],
    id="q1",
    topic="degrees_of_freedom",
    slide_ref="Slide 3"
)
# Returns dict with shuffled options and correct index
```

**Always use one of these methods** - never manually place correct answers, as this leads to positional bias (e.g., correct answer always in position B).

### Reading Quiz Results

After user takes quizzes and syncs results, read from `.cache/quiz-results/`.

**Result JSON Format** (server generates this):

```json
{
  "quiz_id": "pcv05_dlt_2026-01-14",
  "completed": "2026-01-14T14:22:00Z",
  "score": 8,
  "total": 10,
  "percentage": 80,
  "total_time_sec": 180,
  "answers": [
    {
      "question_id": "q1",
      "topic": "degrees_of_freedom",
      "slide_ref": "Slide 3",
      "type": "multiple_choice",
      "selected": 2,
      "correct_index": 2,
      "is_correct": true,
      "time_spent_sec": 15
    },
    {
      "question_id": "q2",
      "topic": "dlt_properties",
      "slide_ref": "Slide 14",
      "type": "true_false",
      "selected": true,
      "correct_value": false,
      "is_correct": false,
      "time_spent_sec": 8
    },
    {
      "question_id": "q3",
      "topic": "line_transformation",
      "slide_ref": "Slide 7",
      "type": "short_answer",
      "text": "l' = H^-T @ l",
      "keywords_found": 2,
      "keywords_expected": 3,
      "is_correct": true,
      "time_spent_sec": 25
    }
  ]
}
```

### Reviewing Web Quiz Results

When user asks to review web quiz results:

1. Read result files from `.cache/quiz-results/`
2. Cross-reference with original quiz JSON to get full question text
3. Analyze patterns:
   - Which topics had incorrect answers?
   - How much time spent on each question?
   - Compare with previous quiz logs for recurring weak areas
4. Generate study recommendations based on missed questions
5. Offer focused review on weak topics

**Example review workflow**:
```
User: "Review my web quiz results"

Claude:
1. Glob .cache/quiz-results/*.json
2. Read each result file
3. Load corresponding quiz from .cache/web-quizzes/
4. Summarize performance
5. Identify weak topics across multiple quizzes
6. Suggest focused review or generate follow-up quiz
```

### Sync Commands

**Push quizzes to server**:
```bash
./scripts/sync_quizzes.sh
```

**Pull results from server**:
```bash
./scripts/sync_results.sh
```

Note: User must configure server credentials in these scripts.

### Quiz Validation

Before deploying quizzes to the web server, validate them with:

```bash
./scripts/validate_quizzes.py
```

This validates all quiz JSON files in `server/data/` against the expected format:

**Quiz-level validation:**
- Required fields: `id`, `lecture`, `topic`, `questions`
- ID matches filename
- Valid lecture format

**Question-level validation:**
- Required fields: `id`, `type`, `question`
- Valid question types: `multiple_choice`, `true_false`, `short_answer`
- Type-specific requirements:
  - Multiple choice: `options` array (2-6 items), `correct` index in range
  - True/false: `correct` as boolean
  - Short answer: `expected_keywords` array (non-empty)
- No duplicate question IDs

**Example output:**
```
Quiz Validation Report
==================================================

✓ All 96 quizzes are valid!

Statistics:
  Total quizzes:     96
  Valid quizzes:     96
  Total questions:   960
  Multiple choice:   633 (65.9%)
  True/False:        231 (24.1%)
  Short answer:      96 (10.0%)
```

Run this after generating or modifying quizzes to catch formatting errors before they cause server issues.

### Quiz Status

Check which lectures have quizzes and how many:

```bash
./scripts/quiz_status.sh
```

Shows quiz coverage per lecture with counts and identifies lectures missing quizzes.

## Finding PDFs

**General patterns:**

```bash
# All PDFs in current directory and subdirectories
glob pattern: "**/*.pdf"

# Find specific document by name
glob pattern: "**/*smith*.pdf"

# Course-specific (if organized in directories)
glob pattern: "CS229/**/*.pdf"
```

**When user's request is ambiguous:**
1. Use Glob to find matching PDFs
2. Present options if multiple matches
3. Let user select which PDF to review

## Extraction and Caching

### Checking the Cache First

**IMPORTANT**: Before running the extraction script, always check if the PDF is already cached:

```bash
# List all cached metadata files to find source PDFs
for f in .cache/extracted/*.json; do cat "$f" | head -5; done
```

Or search for a specific PDF:
```bash
grep -l "pcv10" .cache/extracted/*.json
```

Each `.json` file contains the source PDF path and hash. If found, read the corresponding `.md` file directly:
```bash
# If pcv10 has hash f2c4d6104b10076b:
Read .cache/extracted/f2c4d6104b10076b.md
```

This avoids unnecessary extraction and speeds up sessions.

### First-Time Extraction

When extracting a PDF for the first time (not in cache):

```bash
# Run extraction script (uses venv python)
source .venv/bin/activate && python scripts/extract_pdf.py /path/to/document.pdf
```

This will:
- Convert PDF to markdown using Marker
- Preserve formulas as LaTeX
- Cache result in `.cache/extracted/<hash>.md`
- Save metadata in `.cache/extracted/<hash>.json`
- Take 30-60 seconds depending on PDF size

The script prints the path to the cached markdown file - use Read to load it.

### Using Cached Extraction

If the PDF was previously extracted:
- Script immediately returns cached file path
- Read the markdown file using Read tool
- Instant access (no re-processing)

### Extracting Page Images (Fallback)

If user asks about a specific diagram or visual element:

```bash
# Extract page 23 as an image
source .venv/bin/activate && python scripts/extract_page_image.py /path/to/document.pdf 23
```

Then use Read to view the image and analyze it visually.

## Working with LaTeX Formulas

**Extracted formulas are in LaTeX format:**

Inline: `$E = mc^2$`
Display: `$$\int_a^b f(x)dx$$`

**When explaining formulas:**
- Show the LaTeX notation
- Explain each variable
- Provide context from the document
- Give examples if helpful

**Example:**
```
The epipolar constraint is expressed as:

$$x'^T F x = 0$$

Where:
- $x$ and $x'$ are corresponding points in homogeneous coordinates
- $F$ is the 3×3 Fundamental matrix
- The equation states that $x'$ lies on the epipolar line $Fx$ in the second image
```

## Tips for Best Results

**General Guidelines:**
1. **Always extract first**: Run the extraction script before answering questions
2. **Use caching**: Check if extraction already exists (script handles this)
3. **Reference pages**: Include page numbers when answering
4. **Show formulas**: Display LaTeX formulas when explaining math concepts
5. **Be interactive**: Ask follow-up questions, offer deeper explanations
6. **Adapt to document type**: Use appropriate review style (lectures vs papers vs chapters)

**For Math-Heavy Content:**
- Formulas are preserved in LaTeX - use them!
- Explain notation and variables clearly
- Show step-by-step derivations when helpful
- Offer to extract page images for complex diagrams

**For Research Papers:**
- Focus on understanding methodology and contributions
- Help interpret results and figures
- Discuss limitations and future work
- Compare with related work when relevant

**For Book Chapters:**
- Work through examples step-by-step
- Help with end-of-chapter exercises
- Connect concepts across chapters
- Prove theorems when requested

**For Multi-PDF Sessions:**
- Can review multiple documents in one session
- Cross-reference concepts between documents
- Build connections across topics

**Mode Switching:**
- User can switch from Q&A to Quiz (or vice versa) anytime
- Just ask and switch modes
- Keep the extracted content loaded

## Session Examples

### Lecture Review Session

```
User: "Quiz me on the SLAM lecture"

Your actions:
1. glob pattern: "**/*slam*.pdf"
2. Find matching PDF (e.g., "Lecture_12_SLAM.pdf")
3. Identify as lecture (filename, slide structure)
4. source .venv/bin/activate && python scripts/extract_pdf.py Lecture_12_SLAM.pdf
5. Read cached markdown
6. Generate 10 questions covering SLAM topics
7. Start quiz mode
```

### Research Paper Review Session

```
User: "Help me understand the ORB-SLAM2 paper"

Your actions:
1. glob pattern: "**/*orb*slam*.pdf"
2. Find matching PDF
3. Identify as research paper (structure, citations)
4. source .venv/bin/activate && python scripts/extract_pdf.py orb_slam2.pdf
5. Read cached markdown
6. Present paper overview (research question, methods, results)
7. Enter Q&A mode - focus on methodology and results interpretation
```

### Book Chapter Review Session

```
User: "Review chapter 7 on matrix decompositions"

Your actions:
1. glob pattern: "**/*chapter*7*.pdf" or "**/*matrix*.pdf"
2. Find matching PDF
3. Identify as book chapter (numbered sections, exercises)
4. source .venv/bin/activate && python scripts/extract_pdf.py chapter_07_decompositions.pdf
5. Read cached markdown
6. Present chapter overview (concepts, theorems, exercises)
7. Ask: "Q&A mode or Quiz mode?"
8. If Q&A: Help with concepts and exercises
9. If Quiz: Generate problems similar to exercises
```

### Switching Modes Mid-Session

```
[In Q&A mode]
User: "Actually, can you quiz me instead?"

Your response:
"Sure! I'll generate a quiz based on this content. How many questions would you like? (default: 10)"

User: "10 is fine"

Your response:
[Generate 10 questions and start quiz mode]
```

### Using Page Images

```
User: "I don't understand the diagram on page 15"

Your actions:
1. source .venv/bin/activate && python scripts/extract_page_image.py /path/to/document.pdf 15
2. Read the image file
3. Analyze the diagram visually
4. Explain what it shows, referencing specific elements

Your response:
"Let me extract that diagram for you..."
[After reading image]
"This diagram shows the epipolar geometry configuration. I can see two cameras (left and right) viewing a 3D point P. The key elements are:
- Point P in 3D space
- Its projections p and p' in the two images
- The baseline connecting camera centers C and C'
- The epipolar plane (gray triangle)
- Epipolar lines l and l' in each image

Would you like me to explain how these elements relate to the Fundamental matrix?"
```

## Error Handling

**If extraction fails:**
1. Check if PDF file exists
2. Ensure dependencies are installed (`pip list | grep marker`)
3. Check file permissions
4. Report error to user with helpful message

**If formula extraction is unclear:**
1. Show what was extracted
2. Offer to extract the page as an image
3. Analyze the formula visually from the image

**If no PDFs found:**
1. Double-check the glob pattern
2. Ask user for the PDF file path
3. Clarify which document they want to review

## Privacy Reminder

Always remember: **PDFs are processed locally**. Only extracted markdown text (with LaTeX formulas) is sent to Claude. The original PDFs never leave the user's machine. This ensures privacy for proprietary or sensitive academic materials.

---

For detailed documentation, see [reference.md](reference.md).
For usage examples, see [examples.md](examples.md).
