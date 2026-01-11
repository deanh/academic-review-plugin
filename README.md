# Academic Review Plugin for Claude Code

An AI-powered skill for Claude Code that provides privacy-preserving review sessions with academic PDFs. Extract concepts from lectures, research papers, and book chapters, run Q&A sessions, and generate quizzes with scoring. Mathematical formulas are preserved in LaTeX format.

## Features

- **Multi-Document Support**: Works with lectures, research papers, and book chapters
- **Privacy-Preserving**: All PDF processing happens locally using Marker AI - PDFs never uploaded
- **Math-Aware**: Preserves mathematical formulas in LaTeX format (e.g., `$E = mc^2$`, `$$\int_a^b f(x)dx$$`)
- **Cached Extraction**: First extraction takes 30-60 seconds, subsequent access is instant
- **Two Review Modes**:
  - **Q&A Mode**: Free-form questions with detailed explanations
  - **Quiz Mode**: Auto-generated questions with scoring and feedback
- **Visual Fallback**: Extract specific pages as images for complex diagrams
- **Document Type Detection**: Automatically adapts review style based on document type

## Privacy & Security

This plugin processes PDFs **locally on your machine**. The Marker AI models (~2.7GB) are downloaded once and cached permanently. PDFs are converted to markdown with LaTeX formulas, and only the extracted text is used in conversations with Claude. **Your PDFs never leave your machine.**

## Installation

### Prerequisites

- Python 3.8 or later
- ~3GB disk space for Marker AI models (one-time download)
- Virtual environment (recommended)

### Install the Plugin

```bash
# Method 1: Install directly from GitHub
/plugin install academic-review@github.com/YOUR-USERNAME/academic-review-plugin

# Method 2: Add to marketplace first
/plugin marketplace add YOUR-USERNAME/academic-review-plugin
/plugin install academic-review
```

### Install Python Dependencies

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install marker-pdf
pip install marker-pdf
```

On first use, Marker AI will download ~2.7GB of models (one-time only). These are cached in `~/Library/Caches/datalab/models/` (macOS) or equivalent on other systems.

## Quick Start

### Review a Lecture

```
User: "Review the lecture on epipolar geometry"

Claude will:
1. Find matching PDFs
2. Extract content (cached after first time)
3. Ask: "Q&A mode or Quiz mode?"
4. Begin interactive review session
```

### Understand a Research Paper

```
User: "Help me understand the ORB-SLAM2 paper"

Claude will:
1. Find and extract the paper
2. Present overview: research question, methods, results
3. Enter Q&A mode for methodology and results interpretation
```

### Study a Book Chapter

```
User: "Review chapter 7 on matrix decompositions"

Claude will:
1. Find and extract the chapter
2. Present concepts, theorems, and exercises
3. Help with problem-solving and concept understanding
```

## Usage

### Q&A Mode

Ask free-form questions about the content. Claude provides:
- Detailed explanations with page/section references
- LaTeX formulas with variable definitions
- Examples and derivations
- Connections between related concepts

**Example:**
```
User: What's the difference between F and E matrices?
Claude: [Detailed explanation with formulas from pages 12-18 and 25-30]
```

### Quiz Mode

Test your knowledge with auto-generated questions. Features:
- Multiple choice, true/false, short answer, and problem questions
- Immediate feedback with explanations
- Running score tracking
- Final summary with topics mastered and topics to review

**Example:**
```
User: Quiz me on SLAM
Claude: [Generates 10 questions covering SLAM concepts]
Score: 8/10 (80%) - B

✓ Topics Mastered: SLAM fundamentals, bundle adjustment
⚠️ Topics to Review: EKF-SLAM vs Graph-SLAM tradeoffs
```

### Document Type Detection

The skill automatically detects document type from context:

- **Lectures**: File names with "lecture", "slides", bullet-point heavy content
- **Research Papers**: Standard sections (Abstract, Methods, Results), citations
- **Book Chapters**: Numbered sections, end-of-chapter exercises

Review approach adapts automatically:
- Lectures: Concept understanding, derivations, applications
- Papers: Methodology critique, results interpretation, reproducibility
- Chapters: Theorem understanding, example walkthroughs, exercise solving

## How It Works

### First-Time Extraction

When you review a PDF for the first time:

```bash
python scripts/extract_pdf.py /path/to/document.pdf
```

This:
1. Converts PDF to markdown using Marker AI
2. Preserves formulas as LaTeX
3. Caches result in `.cache/extracted/<hash>.md`
4. Saves metadata in `.cache/extracted/<hash>.json`
5. Takes 30-60 seconds depending on PDF size

### Cached Access

Subsequent access to the same PDF:
- Instantly returns cached markdown file
- No re-processing needed
- Identified by SHA256 hash of PDF content

### Page Image Fallback

For complex diagrams:

```bash
python scripts/extract_page_image.py /path/to/document.pdf 23
```

Extracts page 23 as an image for visual analysis.

## Examples

See [examples.md](.claude/skills/academic-review/examples.md) for detailed usage examples including:
- Lecture Q&A and Quiz modes
- Research paper review
- Book chapter problem-solving
- Mode switching
- Multi-document comparison

## Requirements

- **Python**: 3.8+
- **Disk Space**: ~3GB for Marker AI models (one-time download)
- **Memory**: ~500MB-1GB during PDF extraction
- **Dependencies**: `marker-pdf>=0.2.0`

## Troubleshooting

### Extraction Fails

```bash
# Check if PDF exists
ls -la /path/to/document.pdf

# Ensure marker-pdf is installed
pip list | grep marker

# Check file permissions
ls -l /path/to/document.pdf
```

### Formulas Not Extracted Correctly

- Try extracting the specific page as an image for visual analysis
- Some PDFs use non-standard encoding for formulas

### Models Not Downloading

- Check internet connection
- Ensure sufficient disk space (~3GB)
- Models download automatically on first use

### Virtual Environment Issues

```bash
# Recreate virtual environment
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install marker-pdf
```

## File Structure

```
academic-review-plugin/
├── .claude-plugin/
│   └── plugin.json           # Plugin metadata
├── .claude/
│   └── skills/
│       └── academic-review/
│           ├── SKILL.md       # Main skill definition
│           ├── reference.md   # Technical reference
│           ├── examples.md    # Usage examples
│           └── scripts/
│               ├── extract_pdf.py
│               └── extract_page_image.py
├── .cache/
│   └── extracted/             # Cached PDF extractions
├── README.md                  # This file
├── LICENSE                    # MIT License
├── requirements.txt           # Python dependencies
└── .gitignore                 # Git ignore rules
```

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

See `docs/CONTRIBUTING.md` for detailed guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

- Built with [Marker AI](https://github.com/VikParuchuri/marker) for PDF extraction
- Powered by Claude Code skills system
- Inspired by the need for privacy-preserving academic tools

## Support

- **Issues**: [GitHub Issues](https://github.com/YOUR-USERNAME/academic-review-plugin/issues)
- **Discussions**: [GitHub Discussions](https://github.com/YOUR-USERNAME/academic-review-plugin/discussions)
- **Claude Code Docs**: [code.claude.com/docs](https://code.claude.com/docs)

---

**Note**: Replace `YOUR-USERNAME` with your GitHub username before publishing.
