# Academic Review Skill - Usage Examples

This document shows complete examples of using the academic review skill for different document types and scenarios.

## Table of Contents

1. [Lecture Examples](#lecture-examples)
   - [Q&A Mode: Reviewing a Lecture](#qa-mode-reviewing-a-lecture)
   - [Quiz Mode: Testing Lecture Knowledge](#quiz-mode-testing-lecture-knowledge)
2. [Research Paper Examples](#research-paper-examples)
   - [Q&A Mode: Understanding a Research Paper](#qa-mode-understanding-a-research-paper)
   - [Quiz Mode: Testing Paper Comprehension](#quiz-mode-testing-paper-comprehension)
3. [Book Chapter Examples](#book-chapter-examples)
   - [Q&A Mode: Learning from a Textbook Chapter](#qa-mode-learning-from-a-textbook-chapter)
4. [Advanced Examples](#advanced-examples)
   - [Mode Switching](#mode-switching)
   - [Page Image Fallback](#page-image-fallback)
   - [Multi-Document Review](#multi-document-review)

---

## Lecture Examples

### Q&A Mode: Reviewing a Lecture

**Scenario**: Reviewing Epipolar Geometry lecture

**User**: "Review the lecture on epipolar geometry"

**Claude**:
Finding PDFs...

```bash
glob pattern: "**/*epipolar*.pdf"
```

Found: `lectures/Lecture_05_Epipolar_Geometry.pdf`

Extracting content...

```bash
source .venv/bin/activate && python scripts/extract_pdf.py lectures/Lecture_05_Epipolar_Geometry.pdf
```

```
# Extracting Lecture_05_Epipolar_Geometry.pdf... This may take a minute.
# Extraction complete
.cache/extracted/a1b2c3d4e5f67890.md
```

Reading extracted content...

---

📚 **Lecture Overview: Epipolar Geometry**

This lecture covers 45 pages on stereo vision geometry:

**Main Topics:**
- Epipolar constraint and geometry
- Fundamental matrix $F$ (3×3, rank 2)
- Essential matrix $E = K'^T F K$
- 8-point algorithm for estimating $F$
- Stereo reconstruction workflow
- RANSAC for outlier rejection

**Key Formulas:**
- Epipolar constraint: $x'^T F x = 0$
- Essential matrix from rotation and translation: $E = [t]_× R$
- Triangulation: Solve $AX = 0$ from projections

**Would you like Q&A mode or Quiz mode?**

---

**User**: "Q&A mode"

**Claude**:
Q&A Mode Active! Ask me anything about epipolar geometry, or type "quiz" to switch modes.

---

**User**: "What's the difference between the Fundamental and Essential matrices?"

**Claude**:
Great question! These two matrices are closely related but serve different purposes.

**Fundamental Matrix $F$** (pages 12-18):
- Works in **pixel coordinates** (image space)
- 3×3 matrix with rank 2, so det($F$) = 0
- Encodes the epipolar constraint: $x'^T F x = 0$
- Works with **any cameras** (even uncalibrated)
- Has 7 degrees of freedom (9 entries - scale - rank constraint)
- Accounts for both intrinsic and extrinsic parameters

**Essential Matrix $E$** (pages 25-30):
- Works in **normalized coordinates** (calibrated space)
- Related to $F$ by: $E = K'^T F K$ where $K$ are intrinsic matrices
- Only encodes the **relative pose** (rotation $R$ and translation $t$)
- Structure: $E = [t]_× R$ where $[t]_×$ is the skew-symmetric matrix
- Has 5 degrees of freedom (3 for rotation + 2 for translation direction)
- Requires **calibrated cameras** (known $K$)

**Key Difference:**
Think of $F$ as the complete stereo relationship including camera parameters, while $E$ is the "pure geometry" after removing the camera intrinsics. If you have calibrated cameras, you can extract $E$ from $F$ using the formula above.

Would you like me to explain how to extract $E$ from $F$, or see the derivation?

---

### Quiz Mode: Testing Lecture Knowledge

**User**: "Quiz me on SLAM"

**Claude**:
Finding PDFs...

```bash
glob pattern: "**/*slam*.pdf"
```

Found: `lectures/Lecture_12_SLAM.pdf`

Extracting and analyzing content...

```
# Using cached extraction from Lecture_12_SLAM.pdf
.cache/extracted/b2c3d4e5f67890a1.md
```

---

Quiz Mode - 10 Questions
I'll test your understanding of SLAM concepts, algorithms, and applications.

Score: 0/0

---

**Question 1 of 10** [Multiple Choice]
What does SLAM stand for?

a) Structured Localization and Mapping
b) Simultaneous Localization and Mapping
c) Sequential Location and Measurement
d) Spatial Landmark Acquisition Method

**User**: "b"

**Claude**:
✓ **Correct!** [+1 point]

SLAM stands for Simultaneous Localization and Mapping. It's the problem of building a map of an unknown environment while simultaneously tracking the robot's location within that map. This circular dependency (need map to localize, need pose to map) is what makes SLAM challenging.

Score: 1/1 (100%)

---

**Question 2 of 10** [True/False]
Loop closure is optional in SLAM systems and doesn't significantly affect map quality.

**User**: "false"

**Claude**:
✓ **Correct!** [+1 point]

Loop closure is crucial for SLAM accuracy. When the robot revisits a previously mapped area, recognizing this "loop closure" allows the system to correct accumulated drift and improve the entire map's consistency. Without loop closure, errors accumulate unboundedly, leading to increasingly poor maps over time.

Score: 2/2 (100%)

---

[... continues through 10 questions ...]

---

📊 **Quiz Complete!**

Final Score: 8/10 (80%) - B

✓ **Topics Mastered:**
- SLAM fundamentals and definitions
- Bundle adjustment and optimization
- Loop closure detection

⚠️ **Topics to Review:**
- EKF-SLAM vs Graph-SLAM tradeoffs (pages 15-20)
- Place recognition techniques (pages 28-32)

**Would you like to:**
1. Review the topics you missed in Q&A mode?
2. Take another quiz on the same material?
3. Move to a different lecture?

---

## Research Paper Examples

### Q&A Mode: Understanding a Research Paper

**Scenario**: Understanding a SLAM research paper

**User**: "Help me understand the ORB-SLAM2 paper"

**Claude**:
Finding PDFs...

```bash
glob pattern: "**/*orb*slam*.pdf"
```

Found: `papers/orb_slam2_tro2017.pdf`

Extracting content...

```bash
source .venv/bin/activate && python scripts/extract_pdf.py papers/orb_slam2_tro2017.pdf
```

```
# Extracting orb_slam2_tro2017.pdf... This may take a minute.
# Extraction complete
.cache/extracted/c3d4e5f67890a1b2.md
```

Reading extracted content...

---

📄 **Paper Overview: "ORB-SLAM2: Real-Time SLAM for Monocular, Stereo and RGB-D Cameras"**

**Authors**: Raúl Mur-Artal, Juan D. Tardós
**Published**: IEEE Transactions on Robotics, 2017
**Citations**: 3000+ (highly influential)

**Research Question**:
How to build a complete, real-time SLAM system that works across multiple camera types (monocular, stereo, RGB-D) with the same codebase?

**Key Contributions**:
1. Unified SLAM system for three camera types
2. Place recognition and loop closing module
3. Full 3D reconstruction with scale (even for monocular)
4. Relocalization after tracking failure
5. Real-time performance on standard CPUs

**Methodology**:
- Uses ORB features (fast, rotation-invariant)
- Bag-of-words (DBoW2) for place recognition
- Three-thread architecture: Tracking, Local Mapping, Loop Closing
- Bundle adjustment for optimization: $\min \sum_{i,j} \rho(\|x_j - \pi(T_i X_j)\|^2)$
- Pose graph optimization for loop closure

**Key Results** (Table II, page 8):
- Outperforms LSD-SLAM and PTAM on KITTI dataset
- Monocular: 1.15cm median error
- Stereo: 0.88cm median error
- Real-time: 25-30 FPS on Intel i7

**Limitations** (Section VII):
- Requires textured environments (ORB features)
- No semantic understanding
- Pure geometric SLAM (no learning)

**Would you like Q&A mode or Quiz mode?**

---

**User**: "Q&A mode. How does the three-thread architecture work?"

**Claude**:
Great question! The three-thread architecture is one of ORB-SLAM2's key innovations (Section III, pages 3-5).

**Thread 1: Tracking** (runs every frame)
- Receives new image frames
- Estimates camera pose by matching ORB features to existing map points
- Decides if current frame is a "keyframe" (selected for mapping)
- Most critical for real-time performance
- Formula: Minimizes reprojection error $\sum_i \|x_i - \pi(T X_i)\|^2$

**Thread 2: Local Mapping** (processes keyframes)
- Runs when new keyframes arrive from Tracking
- Creates new map points from keyframe observations
- Performs local bundle adjustment to refine recent map
- Culls redundant keyframes and outlier points
- Goal: Keep map compact and accurate

**Thread 3: Loop Closing** (runs in background)
- Continuously searches for loop closures using DBoW2
- When loop detected: computes similarity transform
- Performs pose graph optimization to distribute error
- Triggers full bundle adjustment to refine entire map

**Why this design?**
- **Parallelism**: All three run concurrently for speed
- **Separation of concerns**: Tracking stays fast, mapping ensures quality
- **Robustness**: If tracking fails, reloc localization can recover

The key insight is that tracking needs to be fast (every frame), but mapping and loop closing can be slower since they work on selected keyframes only.

Would you like me to explain any specific thread in more detail, or discuss how loop closure detection works?

---

### Quiz Mode: Testing Paper Comprehension

**User**: "Quiz me on the ORB-SLAM2 paper"

**Claude**:
Quiz Mode - 10 Questions
I'll test your understanding of the methodology, results, and contributions.

Score: 0/0

---

**Question 1 of 10** [Multiple Choice]
Which feature detector does ORB-SLAM2 use?

a) SIFT
b) SURF
c) ORB (Oriented FAST and Rotated BRIEF)
d) Harris corners

**User**: "c"

**Claude**:
✓ **Correct!** [+1 point]

ORB-SLAM2 uses ORB features (Oriented FAST and Rotated BRIEF), which are rotation-invariant, fast to compute, and free from patents. The paper specifically chose ORB because it provides good performance with low computational cost, enabling real-time operation (Section II-A, page 2).

Score: 1/1 (100%)

---

**Question 2 of 10** [Short Answer]
What is the main advantage of the three-thread architecture over single-threaded SLAM?

**User**: "It allows tracking to stay fast while mapping and loop closing run in parallel"

**Claude**:
✓ **Correct!** [+1 point]

Exactly! The parallel architecture separates time-critical tracking (which must run every frame) from less time-sensitive mapping and loop closing. This allows ORB-SLAM2 to achieve real-time performance while still performing expensive operations like bundle adjustment in the background.

Score: 2/2 (100%)

---

**Question 3 of 10** [Analysis]
The paper reports 1.15cm median error for monocular SLAM on KITTI. Why might monocular SLAM be less accurate than stereo (0.88cm)?

**User**: "Monocular doesn't have depth information directly, has to triangulate"

**Claude**:
✓ **Correct!** [+1 point]

Great reasoning! Monocular SLAM must estimate depth through triangulation from multiple views, which accumulates more uncertainty than stereo cameras that measure depth directly from disparity. Additionally, monocular SLAM has scale ambiguity - the absolute scale must be recovered from motion, while stereo has known baseline.

The paper addresses this in Section IV-C (page 6), noting that monocular initialization is more complex and requires sufficient parallax for reliable triangulation.

Score: 3/3 (100%)

---

[... continues ...]

---

## Book Chapter Examples

### Q&A Mode: Learning from a Textbook Chapter

**Scenario**: Studying matrix decompositions from a linear algebra textbook

**User**: "Help me study chapter 7 on matrix decompositions"

**Claude**:
Finding PDFs...

```bash
glob pattern: "**/*chapter*7*.pdf"
```

Found: `textbooks/linear_algebra_chapter_07.pdf`

Extracting content...

```bash
source .venv/bin/activate && python scripts/extract_pdf.py textbooks/linear_algebra_chapter_07.pdf
```

```
# Extracting linear_algebra_chapter_07.pdf... This may take a minute.
# Extraction complete
.cache/extracted/d4e5f67890a1b2c3.md
```

Reading extracted content...

---

📖 **Chapter Overview: "Matrix Decompositions" (Chapter 7)**

**Topics Covered:**
1. **Singular Value Decomposition (SVD)** (pages 215-228)
   - Definition: $A = U\Sigma V^T$
   - Geometric interpretation
   - Applications: data compression, pseudoinverse

2. **Eigenvalue Decomposition** (pages 229-240)
   - Eigenvectors and eigenvalues: $A\mathbf{v} = \lambda \mathbf{v}$
   - Diagonalization: $A = Q\Lambda Q^{-1}$
   - Spectral theorem for symmetric matrices

3. **QR Decomposition** (pages 241-250)
   - Gram-Schmidt orthogonalization
   - Applications: solving least squares
   - QR algorithm for computing eigenvalues

4. **Cholesky Decomposition** (pages 251-255)
   - For positive definite matrices: $A = LL^T$
   - Efficient for solving linear systems

**Key Theorems:**
- **Theorem 7.1**: Every matrix has an SVD
- **Theorem 7.3**: Symmetric matrices have real eigenvalues
- **Spectral Theorem**: Symmetric matrices are orthogonally diagonalizable

**Exercises**: 28 problems (pages 256-260)
- Computational: Calculate decompositions
- Theoretical: Prove properties
- Applied: Use decompositions to solve problems

**Would you like Q&A mode or Quiz mode?**

---

**User**: "Q&A mode. Can you explain the geometric meaning of SVD?"

**Claude**:
Excellent question! The SVD has a beautiful geometric interpretation (pages 218-220).

**The SVD Formula:**
$$A = U\Sigma V^T$$

**Geometric Interpretation:**
Think of multiplying by $A$ as a **three-step transformation**:

1. **$V^T$**: Rotate/reflect (orthogonal transformation)
2. **$\Sigma$**: Scale along coordinate axes (diagonal matrix)
3. **$U$**: Rotate/reflect again (orthogonal transformation)

**Visualizing with a 2×2 example:**

Suppose $A$ maps the unit circle to an ellipse.

- $V^T$ rotates the circle to align with $A$'s "action directions"
- $\Sigma$ stretches by singular values $\sigma_1, \sigma_2$ (the ellipse's axes)
- $U$ rotates the ellipse to its final orientation

**The singular values** $\sigma_1, \sigma_2, \ldots$ tell you **how much $A$ stretches** in each direction. The columns of $V$ (right singular vectors) are the **input directions**, and columns of $U$ (left singular vectors) are the **output directions**.

**Example from page 220:**
$$A = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}$$

has singular values $\sigma_1 = 4, \sigma_2 = 2$, meaning $A$ stretches most (by factor 4) in one direction and less (by factor 2) in the perpendicular direction.

**Why this matters:**
- **Data compression**: Small singular values = less important directions
- **Pseudoinverse**: $A^+ = V\Sigma^{-1}U^T$ reverses the transformation
- **Low-rank approximation**: Keep only largest singular values

Would you like to see how to compute an SVD, or work through an example problem?

---

**User**: "Let's work through example 7.5"

**Claude**:
Great! Example 7.5 (page 223) asks us to find the SVD of:

$$A = \begin{bmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{bmatrix}$$

Let's solve this step-by-step.

**Step 1: Compute $A^T A$**

$$A^T A = \begin{bmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$

**Step 2: Find eigenvalues of $A^T A$**

$$\det(A^T A - \lambda I) = \det\begin{bmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{bmatrix} = (2-\lambda)^2 - 1 = 0$$

$$(2-\lambda)^2 = 1 \implies 2-\lambda = \pm 1$$

So $\lambda_1 = 3$, $\lambda_2 = 1$

**Step 3: Singular values**

$\sigma_1 = \sqrt{3}$, $\sigma_2 = 1$

**Step 4: Find eigenvectors of $A^T A$ (these become $V$)**

For $\lambda_1 = 3$:
$$\begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}\mathbf{v}_1 = 0 \implies \mathbf{v}_1 = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 \\ 1 \end{bmatrix}$$

For $\lambda_2 = 1$:
$$\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}\mathbf{v}_2 = 0 \implies \mathbf{v}_2 = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 \\ -1 \end{bmatrix}$$

So: $V = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$

**Step 5: Compute $U$ from $U = AV\Sigma^{-1}$**

[I can continue with the full calculation if you'd like, or move to the next step. Would you like to see the rest, or do you want to try computing $U$ yourself?]

---

## Advanced Examples

### Mode Switching

**User**: [In Q&A mode] "Actually, can you quiz me on this instead?"

**Claude**:
Sure! I'll generate a quiz based on this chapter. How many questions would you like? (default: 10)

**User**: "5 questions"

**Claude**:
Quiz Mode - 5 Questions

I'll test your understanding of matrix decompositions.

Score: 0/0

[Quiz begins...]

---

### Page Image Fallback

**User**: "I don't understand the diagram on page 15"

**Claude**:
Let me extract that diagram for you...

```bash
source .venv/bin/activate && python scripts/extract_page_image.py document.pdf 15
```

[After reading image]

This diagram shows the geometric interpretation of SVD in 2D. I can see:

1. **Input space (left)**: Unit circle in blue
2. **After $V^T$** (middle): Circle rotated to align with transformation axes
3. **After $\Sigma$** (middle-right): Ellipse with axes $\sigma_1$ and $\sigma_2$
4. **After $U$** (right): Final rotated ellipse

The arrows show:
- Red arrow: direction of maximum stretch ($\sigma_1 = 2.5$)
- Blue arrow: direction of minimum stretch ($\sigma_2 = 1.2$)

The key insight is that ANY linear transformation is just rotation + scaling + rotation.

Would you like me to explain any specific part in more detail?

---

### Multi-Document Review

**User**: "Compare the ORB-SLAM2 paper with the LSD-SLAM paper"

**Claude**:
Great comparative analysis question! Let me extract both papers...

```bash
source .venv/bin/activate && python scripts/extract_pdf.py papers/orb_slam2_tro2017.pdf
# Using cached extraction: .cache/extracted/c3d4e5f67890a1b2.md

source .venv/bin/activate && python scripts/extract_pdf.py papers/lsd_slam_eccv2014.pdf
# Extracting lsd_slam_eccv2014.pdf...
# Extraction complete: .cache/extracted/e5f67890a1b2c3d4.md
```

Reading both papers...

---

📄 **Comparative Analysis: ORB-SLAM2 vs LSD-SLAM**

**Approach:**
- **ORB-SLAM2**: Feature-based (ORB keypoints)
- **LSD-SLAM**: Direct method (photometric error)

**Map Representation:**
- **ORB-SLAM2**: Sparse map of 3D points
- **LSD-SLAM**: Semi-dense depth maps

**Key Differences:**

| Aspect | ORB-SLAM2 | LSD-SLAM |
|--------|-----------|----------|
| Features | ORB keypoints (~1000/frame) | All high-gradient pixels |
| Optimization | Bundle adjustment on keypoints | Direct image alignment |
| Loop Closure | DBoW2 bag-of-words | Direct image matching |
| Accuracy | Higher (1.15cm on KITTI) | Lower (3-4cm on KITTI) |
| Robustness | Better in textured scenes | Works in low-texture |
| Computation | Faster (30 FPS) | Slower (20 FPS) |

**Mathematical Foundation:**

*ORB-SLAM2* minimizes geometric error:
$$\min \sum_{i,j} \rho(\|x_j - \pi(T_i X_j)\|^2)$$

*LSD-SLAM* minimizes photometric error:
$$\min \sum_{\mathbf{p}} \|I_2(\mathbf{p}') - I_1(\mathbf{p})\|^2$$

**When to use each:**
- **ORB-SLAM2**: Textured environments, need high accuracy, have good features
- **LSD-SLAM**: Low-texture scenes, need dense reconstruction, indoors

Would you like me to dive deeper into any specific aspect of the comparison?

---

**End of Examples Document**

For more information, see [SKILL.md](SKILL.md) for usage instructions and [reference.md](reference.md) for technical details.
