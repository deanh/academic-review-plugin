# Quiz Corrections

Overall: 197/240 (82%) across 11 quizzes. 8 answers were scored wrong due to a
server bug (correct answers marked incorrect). Actual score: 205/240 (85%).

---

## Epipolar Geometry -- 21/30 (70%)

**epipole_null_space**: The epipole e' in the second image satisfies e'^T F = 0
(left null space of F), equivalently F^T e' = 0. The epipole e in the first
image satisfies Fe = 0 (right null space). Both can be extracted from one SVD
of F: e = last column of V, e' = last column of U.

**8point_minimum**: The 8-point algorithm ignores det(F)=0, treating F as having
8 DOF (9 elements - 1 scale). Each correspondence gives 1 equation, so 8
correspondences needed. The 7-point algorithm uses det(F)=0, needing only 7.

**7point_solutions**: 7 correspondences give a 2D null space: F_t = tU + (1-t)V.
Applying det(F_t)=0 gives a cubic polynomial in t. A cubic has 1 or 3 real
roots, so 1 or 3 solutions.

**planar_degeneracy** (skipped): When all points lie on a plane, correspondences
are described by a homography H. F becomes ambiguous (2-parameter family of
solutions). F and H are related through F = [e']_x H.

**f_from_projection**: F can be computed directly from P=[I|0] and P'=[M|m] as
F = [m]_x M. No point correspondences needed.

**sampson_error**: Sampson error is a first-order approximation to the geometric
(reprojection) error. It normalizes algebraic error by the epipolar line
lengths, giving a result in approximately squared pixel units.

**ransac_error_metric**: RANSAC needs a geometrically meaningful threshold.
Use symmetric epipolar distance (point-to-line distance in both images) or
Sampson error, not algebraic error (which has no geometric meaning).

**e_from_f_same_k** (skipped): E = K^T F K when both cameras share calibration
K. Derivation: substitute x_hat = K^{-1}x into x'^T F x = 0 and compare with
x_hat'^T E x_hat = 0.

**point_line_distance**: Distance from point to epipolar line l=(a,b,c):
d = |ax + by + c| / sqrt(a^2 + b^2). The denominator uses only the first two
components of l, not the full norm.

---

## Homogeneous 2D -- 18/25 (72%)

*3 answers were scored wrong due to server bug (h2d_019, h2d_022, and one
other). Actual score likely ~21/25.*

**line_at_infinity**: Points at infinity have the form (x,y,0)^T. They form the
line at infinity l_inf = (0,0,1)^T. Not a conic, not a plane -- a line.

**conic_dof**: A conic C is a 3x3 symmetric matrix: 6 independent elements
minus 1 for scale = 5 DOF. Therefore 5 points determine a conic.

**degenerate_conic**: When det(C)=0, the conic degenerates into two lines
(possibly coincident). Not a hyperbola -- degeneracy means the conic splits.

**line_at_infinity_coords**: l_inf = (0,0,1)^T in homogeneous coordinates. A
point x = (x,y,w)^T lies on l_inf when l_inf^T x = w = 0, which is exactly
the condition for a point at infinity.

**pole_polar**: For a point x outside conic C, the polar line l = Cx passes
through the two tangent points from x to the conic. The pole-polar relationship
is fundamental: if l is the polar of x, then x is the pole of l.

---

## Transformations -- 22/25 (88%)

*1 answer scored wrong due to server bug (trans_006). Actual score ~23/25.*

**denormalization**: After estimating H_tilde with normalized points
(x_hat = Tx, x_hat' = T'x'), recover H for original coordinates:
H = T'^{-1} H_tilde T. Same pattern as F denormalization.

**affine_decomposition**: To decompose an affine transformation's linear part A
into rotation, scale, and shear, use SVD: A = U S V^T. This gives rotation
(U, V^T), scale/shear (S). Not eigendecomposition -- A may not be symmetric.

---

## Homogeneous 3D -- 17/20 (85%)

*2 answers scored wrong due to server bug (h3d_005, h3d_015). Actual ~19/20.*

**quadric_dof**: A quadric Q is a 4x4 symmetric matrix: 10 independent elements
minus 1 for scale = 9 DOF.

---

## Triangulation -- 16/20 (80%)

**linear_triangulation_equations**: Each image point gives 2 independent
equations from x cross PX = 0 (the cross product eliminates the projective
scale factor, yielding 2 independent equations from the 3 cross product rows).

**disparity_depth** (skipped): In rectified stereo: Z = f*B/d where f is focal
length, B is baseline, d is disparity. Depth is inversely proportional to
disparity -- precision degrades with distance.

**dlt_triangulation_invariance**: DLT triangulation minimizes algebraic error,
which is NOT invariant to coordinate system choice. The gold standard
(minimizing geometric/reprojection error) is invariant.

**multiview_triangulation**: Overdetermined linear triangulation via SVD
minimizes the sum of squared algebraic errors (||Ax||^2 subject to ||x||=1),
not reprojection errors. Reprojection error minimization requires nonlinear
optimization.

---

## Trifocal Tensor -- 13/20 (65%)

*2 answers scored wrong due to server bug (tri3_001, tri3_016). Actual ~15/20.*

**trifocal_from_cameras** (skipped): Each tensor element relates to determinants
of 2x2 submatrices of P2 and P3 (with P1=[I|0] fixed). The tensor encodes how
the two non-canonical cameras relate through the canonical one.

**ppp_constraints** (skipped): A point-point-point correspondence across 3 views
provides 4 independent scalar constraints (from the 3x3 matrix equation
[x']_x (sum_i x_i T^i) [x'']_x = 0, which is rank-deficient).

**trifocal_minimum_points**: 7 point correspondences minimum for linear
estimation (ignoring internal constraints). 7 points x 4 equations = 28 >= 27
elements (up to scale).

**trifocal_from_fundamental** (skipped): The tensor can be expressed in terms
of F12, F13, and the epipoles. This means pairwise F matrices are embedded
within the tensor.

**tensor_contraction**: Contracting the tensor sum_i x_i T^i produces a 3x3
matrix (not a new tensor). This matrix depends on the point x in view 1 and
encodes the point transfer between views 2 and 3.

---

## Bundle Adjustment -- 17/20 (85%)

**normal_equations**: J^T J is the Hessian approximation (also called the normal
matrix). In Gauss-Newton, J^T J approximates the Hessian of the cost function.
Not the correlation or covariance matrix.

**schur_complement**: The Schur complement eliminates point unknowns, leaving a
reduced system involving only camera parameters. Points are eliminated first
because the point-point block V is block-diagonal (trivially invertible).

**rotation_parameterization**: Angle-axis (Rodrigues) is preferred for BA: 3
parameters (minimal), no gimbal lock, smooth derivatives. Euler angles have
gimbal lock. Quaternions work but have 4 params + unit constraint.

---

## Calibration -- 18/20 (90%)

**daq_projection**: The dual absolute quadric Q*_inf projects as
omega* = P Q*_inf P^T. Note: P on the left, P^T on the right (dual/adjoint
projection).

**kruppa_constraints**: Kruppa equations provide 2 independent constraints per
image pair (not 1). Derived from the relationship between the IAC and F.

---

## Robust Estimation -- 18/20 (90%)

**ransac_iterations** (skipped): k = log(1-p) / log(1-w^n). With w=0.5, n=8,
p=0.99: k = log(0.01)/log(1-1/256) ~ 1177 iterations.

**ransac_guarantee**: RANSAC is probabilistic -- never guaranteed to find the
optimal solution. It achieves high probability of success, but there's always a
(small) chance of failure. This is fundamental to its design.

---

## Distortion -- 14/15 (93%)

**distortion_distribution**: Radial distortion increases with distance from the
image center, not decreases. Maximum distortion is at the image edges.

---

## Camera Model -- 23/25 (92%)

*1 answer scored wrong due to server bug (cam_007). Actual ~24/25.*

**plane_at_infinity**: The image of the plane at infinity (vanishing points and
lines) depends only on camera rotation R and calibration K, not on translation.
This is because the plane at infinity has no finite 3D position.

---

## Server Bug Note

A scoring bug in the server-side option shuffle caused 8 correct answers to be
marked wrong. The bug was in strip_answers(): it shuffled option display order
and updated the correct index, but didn't update the stored options, creating a
mismatch in the scoring file. Fixed 2026-02-04.
