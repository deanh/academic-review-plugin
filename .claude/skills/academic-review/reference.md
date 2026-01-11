# Academic Review Skill - Technical Reference

## Table of Contents

1. [PDF Extraction Process](#pdf-extraction-process)
2. [LaTeX Formula Handling](#latex-formula-handling)
3. [Question Types](#question-types)
4. [Scoring Rubrics](#scoring-rubrics)
5. [Caching System](#caching-system)
6. [Page Image Fallback](#page-image-fallback)
7. [Advanced Features](#advanced-features)
8. [Troubleshooting](#troubleshooting)

## PDF Extraction Process

### Marker-Based Extraction

The skill uses [Marker](https://github.com/VikParuchuri/marker), a powerful PDF-to-Markdown converter that preserves mathematical formulas in LaTeX format.

**How it works:**

1. **PDF Analysis**: Marker analyzes the PDF structure, identifying text blocks, formulas, tables, and figures
2. **Text Extraction**: Extracts text while preserving formatting (headings, lists, paragraphs)
3. **Formula Recognition**: Identifies mathematical expressions and converts them to LaTeX
4. **Markdown Generation**: Outputs clean markdown with LaTeX formulas embedded

**What gets preserved:**
- Headings and subheadings
- Bullet points and numbered lists
- Tables (converted to markdown format)
- **Formulas in LaTeX** (inline and display)
- Structure and hierarchy

**What doesn't extract well:**
- Complex multi-column layouts (may be linearized)
- Diagrams and figures (referenced but not rendered)
- Handwritten annotations
- Some specialized symbols (fallback to Unicode or description)

### Extraction Command

```bash
source .venv/bin/activate && python scripts/extract_pdf.py <pdf_path>
```

**Output:**
- **Markdown file**: `.cache/extracted/<hash>.md` - The extracted content
- **Metadata JSON**: `.cache/extracted/<hash>.json` - Info about the PDF

**Metadata format:**
```json
{
  "pdf_path": "/absolute/path/to/lecture.pdf",
  "pdf_name": "lecture.pdf",
  "page_count": 45,
  "hash": "a1b2c3d4e5f67890"
}
```

**Performance:**
- First extraction: 30-60 seconds (depends on PDF size and complexity)
- Cached access: Instant (<1 second)
- Memory usage: ~500MB-1GB during extraction
- Disk usage: ~10-50KB per cached markdown file

## LaTeX Formula Handling

### Formula Types

**Inline formulas** (within text):
```markdown
The epipolar constraint is $x'^T F x = 0$ for corresponding points.
```

**Display formulas** (standalone):
```markdown
The fundamental matrix satisfies:

$$x'^T F x = 0$$
```

### Common Formula Patterns

**Photogrammetry/Computer Vision:**
- Camera projection: $x = PX$ where $P = K[R|t]$
- Fundamental matrix: $F = K'^{-T} [t]_× R K^{-1}$
- Homography: $x' = Hx$
- Essential matrix: $E = [t]_× R$

**Adjustment Theory:**
- Error propagation: $\Sigma_{xx} = J \Sigma_{ll} J^T$
- Least squares: $\hat{x} = (A^T P A)^{-1} A^T P l$
- Weight matrix: $P = \Sigma^{-1}$
- Chi-square test: $\chi^2 = v^T P v$

**Geodesy:**
- GPS positioning: $\rho = \sqrt{(X-X_s)^2 + (Y-Y_s)^2 + (Z-Z_s)^2}$
- Coordinate transformations: $X = R X' + t$
- Height systems: $H = h - N$ where $N$ is geoid undulation

**GIS/Databases:**
- Distance metrics: $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$
- Spatial queries: Set notation and SQL

**Machine Learning/AI:**
- Loss functions: $L(\theta) = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2$
- Gradient descent: $\theta_{t+1} = \theta_t - \alpha \nabla L(\theta_t)$
- Backpropagation: $\frac{\partial L}{\partial w} = \frac{\partial L}{\partial y} \frac{\partial y}{\partial w}$
- Softmax: $\text{softmax}(x_i) = \frac{e^{x_i}}{\sum_j e^{x_j}}$
- Cross-entropy: $H(p,q) = -\sum_x p(x) \log q(x)$

**Statistics/Probability:**
- Normal distribution: $f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-(x-\mu)^2/(2\sigma^2)}$
- Bayes' theorem: $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$
- Confidence intervals: $\bar{x} \pm t_{\alpha/2} \frac{s}{\sqrt{n}}$
- Hypothesis testing: $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$
- Maximum likelihood: $\hat{\theta} = \arg\max_\theta \prod_i p(x_i | \theta)$

**Physics:**
- Energy-momentum: $E^2 = (pc)^2 + (mc^2)^2$
- Wave equation: $\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u$
- Schrodinger equation: $i\hbar\frac{\partial}{\partial t}|\psi\rangle = \hat{H}|\psi\rangle$
- Maxwell's equations: $\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$

**Linear Algebra:**
- Matrix decomposition: $A = U\Sigma V^T$ (SVD)
- Eigenvalues: $A\mathbf{v} = \lambda \mathbf{v}$
- Matrix inverse: $(AB)^{-1} = B^{-1}A^{-1}$
- Trace: $\text{tr}(AB) = \text{tr}(BA)$
- Determinant: $\det(AB) = \det(A)\det(B)$

**Calculus:**
- Chain rule: $\frac{df}{dx} = \frac{df}{du}\frac{du}{dx}$
- Integration by parts: $\int u \, dv = uv - \int v \, du$
- Taylor series: $f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(x-a)^n$
- Gradient: $\nabla f = \left(\frac{\partial f}{\partial x_1}, \ldots, \frac{\partial f}{\partial x_n}\right)$

### Explaining Formulas

**Best practices:**

1. **Show the formula**:
   ```
   The covariance matrix is:
   $$\Sigma_{xx} = (A^T P A)^{-1}$$
   ```

2. **Define all variables**:
   ```
   Where:
   - $\Sigma_{xx}$ is the covariance matrix of unknowns
   - $A$ is the design matrix
   - $P$ is the weight matrix
   ```

3. **Explain the meaning**:
   ```
   This formula tells us how uncertain our adjusted parameters are. Larger values in
   $\Sigma_{xx}$ mean more uncertainty, while smaller values mean higher precision.
   ```

4. **Give context**:
   ```
   This appears in Lecture 3, page 15, in the section on least squares adjustment.
   ```

## Question Types

### 1. Multiple Choice

**Purpose**: Test conceptual understanding, common misconceptions

**Format:**
```
Question X of N [Multiple Choice]
What is the rank of the Fundamental matrix F?

a) 1
b) 2
c) 3
d) 4

Your answer:
```

**Design guidelines:**
- 4 options total
- 1 correct answer
- 3 plausible distractors (common mistakes)
- Keep options concise
- Vary position of correct answer

**Example distractors:**
- Off-by-one errors (rank 1 or 3 instead of 2)
- Confusion with related concepts (dimension vs rank)
- Common misconceptions from the material

### 2. True/False

**Purpose**: Quick concept checks, test binary understanding

**Format:**
```
Question X of N [True/False]
True or False: The Essential matrix can be computed from uncalibrated cameras.

Your answer:
```

**Design guidelines:**
- Clear, unambiguous statements
- Test single concepts
- Avoid "always" and "never" (usually false)
- Balance true/false distribution

### 3. Short Answer

**Purpose**: Test ability to define concepts, explain relationships

**Format:**
```
Question X of N [Short Answer]
In 1-2 sentences, explain the difference between the Fundamental matrix and the Essential matrix.

Your answer:
```

**Evaluation:**
- Accept various phrasings
- Look for key concepts in answer
- Award full credit if main idea is present
- Provide model answer in feedback

**Key concepts to check:**
- Main distinction mentioned
- Correct terminology used
- Relationship understood (if asked)

### 4. Formula Problems

**Purpose**: Test ability to apply formulas to scenarios

**Format:**
```
Question X of N [Formula Problem]
Given two cameras with intrinsic matrices K and K', and Fundamental matrix F,
write the formula to compute the Essential matrix E.

Your answer:
```

**Evaluation:**
- Full credit: Correct formula
- Partial credit (0.5 pts): Correct approach but minor errors
- Examples of partial credit:
  - Transpose in wrong place: $E = K'^T F K$ instead of $E = K'^T F K^{-1}$
  - Forgot inverse: $E = K'^T F K$ instead of $E = K'^T F K^{-1}$

## Scoring Rubrics

### Overall Scoring

| Score | Grade | Interpretation |
|-------|-------|----------------|
| 90-100% | A | Excellent understanding |
| 80-89% | B | Good understanding, minor gaps |
| 70-79% | C | Adequate understanding, some gaps |
| 60-69% | D | Passing, significant gaps |
| 0-59% | F | Major gaps, needs review |

### Per-Question Scoring

| Question Type | Points | Partial Credit |
|---------------|--------|----------------|
| Multiple Choice | 1.0 | None (all or nothing) |
| True/False | 1.0 | None (all or nothing) |
| Short Answer | 1.0 | 0.5 if partially correct |
| Formula Problem | 1.0 | 0.5 if approach correct but error |

### Partial Credit Guidelines

**Short Answer (0.5 points):**
- Mentioned one key concept but missed another
- Right idea but imprecise terminology
- Incomplete but not incorrect

**Formula Problems (0.5 points):**
- Correct structure but wrong symbol
- Forgot transpose or inverse
- Right approach but calculation error

**No Credit:**
- Completely wrong answer
- Shows fundamental misunderstanding
- No relevant content

## Caching System

### How Caching Works

**Hash-based identification:**
- Each PDF gets a SHA256 hash (first 16 characters)
- Hash is based on file content, not name
- Same file = same hash, even if renamed
- Modified file = different hash, new extraction

**Cache structure:**
```
.cache/
├── extracted/
│   ├── a1b2c3d4e5f67890.md      # Markdown content
│   ├── a1b2c3d4e5f67890.json    # Metadata
│   ├── f9e8d7c6b5a43210.md
│   └── f9e8d7c6b5a43210.json
└── images/
    ├── a1b2c3d4e5f67890_page_15.png
    ├── a1b2c3d4e5f67890_page_23.png
    └── f9e8d7c6b5a43210_page_8.png
```

**Cache benefits:**
- **Speed**: Instant access after first extraction
- **Consistency**: Same extraction every time
- **Privacy**: Process once locally, use many times
- **Disk efficient**: Markdown much smaller than PDF

**Cache invalidation:**
- If PDF is modified, hash changes → new extraction
- Old cache entries remain (manual cleanup needed)
- No automatic expiration

**Manual cache management:**
```bash
# Clear all cached extractions
rm .cache/extracted/*

# Clear specific PDF's cache
rm .cache/extracted/a1b2c3d4e5f67890.*

# Clear all page images
rm .cache/images/*

# Check cache size
du -sh .cache/
```

## Page Image Fallback

### When to Use

Use page image extraction when:
1. User asks about a specific diagram or figure
2. Formula extraction is unclear or garbled
3. Complex visual elements (graphs, charts, photos)
4. Multi-panel figures with annotations

### Extraction Command

```bash
source .venv/bin/activate && python scripts/extract_page_image.py <pdf_path> <page_number>
```

**Parameters:**
- `pdf_path`: Path to PDF file
- `page_number`: Page to extract (1-indexed, not 0-indexed)

**Output:**
- PNG image at 200 DPI
- Saved to `.cache/images/<hash>_page_<num>.png`
- High resolution for formula and diagram clarity

### Using Extracted Images

After extracting:
```bash
# Read the image file
Read .cache/images/a1b2c3d4e5f67890_page_15.png
```

Claude can then:
- Analyze the diagram visually
- Read formulas from the image
- Describe visual elements
- Explain relationships shown in the diagram

### Example Workflow

```
User: "I don't understand the diagram on slide 23"

Steps:
1. Extract: python scripts/extract_page_image.py lecture.pdf 23
2. Read: Read .cache/images/<hash>_page_23.png
3. Analyze image and explain to user
4. Reference markdown text for additional context
```

## Advanced Features

### Multi-PDF Sessions

**Reviewing multiple lectures:**
1. Extract all relevant PDFs
2. Load all markdown files into context
3. Cross-reference concepts between lectures
4. Generate comprehensive quizzes spanning multiple topics

**Example:**
```
User: "Quiz me on all space geodesy lectures"

Steps:
1. glob: "space-odesy/**/*.pdf"
2. Extract all 15 PDFs (use cached if available)
3. Read all markdown files
4. Generate 20 questions covering all lectures
5. Note which lecture each question comes from
```

### Adaptive Difficulty

In quiz mode, adjust difficulty based on performance:

- **High performance (>80%)**: Ask deeper questions, test edge cases
- **Medium performance (60-80%)**: Mix of basic and advanced
- **Low performance (<60%)**: Focus on fundamentals, offer hints

### Cross-Lecture Connections

When answering questions, make connections:
- "This relates to the concept of X we saw in Lecture 2..."
- "Compare this to the alternative approach in Lecture 5..."
- "This is a special case of the general formula from Lecture 1..."

### Study Guide Generation

Can generate structured study guides:
```
# Lecture X: Topic Name

## Key Concepts
- Concept 1: Brief definition
- Concept 2: Brief definition

## Important Formulas
- $formula_1$: What it computes
- $formula_2$: When to use it

## Practice Problems
1. Question about concept 1
2. Question applying formula 1

## Connections
- Related to Lecture Y: Concept Z
- Builds on Lecture W: Foundation
```

## Troubleshooting

### Extraction Issues

**Problem**: Script fails with "marker-pdf not installed"

**Solution:**
```bash
source .venv/bin/activate
pip install marker-pdf pdf2image
```

---

**Problem**: Extraction is very slow (>2 minutes)

**Possible causes:**
- Very large PDF (>100 pages)
- High-resolution images in PDF
- Complex formulas or tables

**Solutions:**
- Be patient on first extraction (cached after)
- Consider splitting large PDFs
- Verify sufficient memory available

---

**Problem**: Formulas extracted incorrectly

**Symptoms:**
- Garbled LaTeX
- Missing symbols
- Wrong operators

**Solutions:**
1. Check the original PDF (sometimes formula is an image)
2. Use page image fallback for that specific page
3. Manually show the correct formula from the visual image

---

**Problem**: "No such file or directory" error

**Checks:**
- Verify PDF path is correct
- Use absolute path if relative path fails
- Check file permissions
- Ensure you're in the correct working directory

### Caching Issues

**Problem**: Cache not being used (re-extracting every time)

**Possible causes:**
- PDF file was modified (different hash)
- Cache directory doesn't exist
- Permissions issue

**Solution:**
```bash
# Verify cache exists
ls .cache/extracted/

# Check if hash matches
python -c "import hashlib; print(hashlib.sha256(open('path/to/pdf', 'rb').read()).hexdigest()[:16])"
```

---

**Problem**: Running out of disk space

**Check cache size:**
```bash
du -sh .cache/
```

**Clean up if needed:**
```bash
# Remove old/unused caches
rm .cache/extracted/*.md
rm .cache/images/*.png
```

### Quiz Issues

**Problem**: Questions too easy/hard

**Solution:**
- Adjust question generation based on lecture complexity
- Mix difficulty levels
- Ask user preference at start

---

**Problem**: Short answer evaluation too strict

**Solution:**
- Be flexible with phrasing
- Accept synonyms and paraphrasing
- Award partial credit generously
- Explain what was missing

### Performance Issues

**Problem**: Running out of memory during extraction

**Symptoms:**
- Process killed
- "MemoryError" exception

**Solutions:**
- Close other applications
- Process smaller PDFs first
- Consider extracting in batches

---

**Problem**: Slow response during quiz

**Possible causes:**
- Too much content loaded
- Multiple large PDFs in context

**Solutions:**
- Focus on one lecture at a time
- Clear context between sessions
- Use caching effectively

## Dependencies

**Python Packages:**
- `marker-pdf>=1.10.1` - PDF to Markdown with LaTeX
- `pdf2image>=1.17.0` - PDF page to image conversion
- `Pillow>=10.1.0` - Image processing (dependency)

**System Requirements:**
- Python 3.9+
- poppler (system package for pdf2image)
- 2GB+ RAM for extraction
- 100MB+ disk space for caches

**Installation:**
```bash
# Python packages (in venv)
pip install marker-pdf pdf2image

# System package (macOS)
brew install poppler

# System package (Linux)
sudo apt-get install poppler-utils
```

## Performance Characteristics

**Extraction Speed:**
- Small PDF (20 pages): ~15-30 seconds
- Medium PDF (50 pages): ~30-60 seconds
- Large PDF (100+ pages): ~60-120 seconds

**Memory Usage:**
- Extraction: 500MB-1GB
- Cached read: <100MB

**Disk Usage:**
- Markdown cache: ~10-50KB per PDF
- Page images: ~200-500KB per page (200 DPI)

**Accuracy:**
- Formula extraction: ~95% for standard LaTeX
- Text extraction: ~99% for digital PDFs
- Table extraction: ~85% (depends on complexity)
