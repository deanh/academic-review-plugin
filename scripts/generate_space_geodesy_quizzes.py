#!/usr/bin/env python3
"""Generate Space Geodesy (Introduction to Space Geodesy) quiz questions."""

import json
from pathlib import Path
from quiz_utils import create_mc_question

OUTPUT_DIR = Path(__file__).parent.parent / "server" / "data" / "questions" / "space_geodesy"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def tf(id, question, correct, topic):
    return {"id": id, "type": "true_false", "question": question, "correct": correct, "topic": topic}


def write_topic(filename, questions):
    path = OUTPUT_DIR / f"{filename}.json"
    path.write_text(json.dumps(questions, indent=2))
    print(f"  {filename}: {len(questions)} questions")


# ============================================================
# TOPIC: reference_systems (L02) — 26 questions
# ============================================================
reference_systems = [
    create_mc_question(
        id="ref_001", topic="terminology",
        question="In space geodesy, three related concepts are distinguished: coordinate system, reference system, and reference frame. A coordinate system is the most abstract — it defines mathematical base functions in a metric space. A reference system adds physical context. What is a reference frame?",
        correct="The realization of a reference system through measured coordinates of physical points (e.g., station positions derived from observations)",
        distractors=[
            "An alternative name for a coordinate system used in navigation",
            "A set of mathematical equations relating two coordinate systems",
            "The hardware used to define the origin of a coordinate system"
        ]
    ),
    create_mc_question(
        id="ref_002", topic="conversion_vs_transformation",
        question="What is the difference between a coordinate conversion and a coordinate transformation?",
        correct="A conversion changes from one coordinate system to another (e.g., Cartesian to spherical) without changing the reference; a transformation changes the underlying physical observer or reference system",
        distractors=[
            "A conversion changes the reference system; a transformation changes the coordinate system",
            "They are the same operation — the terms are interchangeable",
            "A conversion is approximate; a transformation is exact"
        ]
    ),
    create_mc_question(
        id="ref_003", topic="coordinate_systems",
        question="In spherical coordinates $\\mathbf{u} = \\mathbf{u}(\\varphi, \\lambda, r)$, the Cartesian components are given by $u_1 = r\\cos\\lambda\\cos\\varphi$, $u_2 = r\\sin\\lambda\\cos\\varphi$, $u_3 = r\\sin\\varphi$. What does the metric tensor for this coordinate system look like?",
        correct="It is diagonal (orthogonal) but not the identity matrix — $g_{11} = r^2$, $g_{22} = r^2\\cos^2\\varphi$, $g_{33} = 1$",
        distractors=[
            "It is the $3 \\times 3$ identity matrix, just like Cartesian coordinates",
            "It is a full $3 \\times 3$ matrix with all non-zero entries",
            "It is diagonal with all entries equal to $r^2$"
        ]
    ),
    create_mc_question(
        id="ref_004", topic="metric_tensor",
        question="The metric tensor $G$ for an orthonormal Cartesian coordinate system is the identity matrix $I$. The Euclidean line element is then $ds^2 = dx^2 + dy^2 + dz^2$. What is the physical significance of the metric tensor in general?",
        correct="It defines how coordinate changes translate to actual distances and angles — it encodes the scaling factors of the coordinate space",
        distractors=[
            "It stores the coordinates of all reference points in the frame",
            "It determines the handedness (left vs. right) of the coordinate system",
            "It specifies the number of dimensions of the coordinate space"
        ]
    ),
    create_mc_question(
        id="ref_005", topic="meridian_convergence",
        question="In the spherical metric tensor, the entry $g_{22} = r^2\\cos^2\\varphi$ contains a factor $\\cos\\varphi$. This factor is called meridian convergence. What does it express physically?",
        correct="An angular change in longitude produces a larger change in distance at the equator ($\\cos\\varphi = 1$) and approaches zero at the poles ($\\cos\\varphi = 0$)",
        distractors=[
            "Meridians are longer at the poles than at the equator",
            "The radius of curvature is constant regardless of latitude",
            "Longitude is undefined at the equator"
        ]
    ),
    create_mc_question(
        id="ref_006", topic="handedness",
        question="A right-handed coordinate system satisfies $\\mathbf{e}_1 \\times \\mathbf{e}_2 = \\mathbf{e}_3$. To convert from a right-handed to a left-handed system, which operation is required?",
        correct="A reflection (mirror) matrix that reverses the sign of one axis",
        distractors=[
            "A rotation of 90° around any axis",
            "A scaling by a factor of $-1$ on all three axes",
            "A translation of the origin"
        ]
    ),
    create_mc_question(
        id="ref_007", topic="ellipsoidal_coordinates",
        question="Geodetic (ellipsoidal) coordinates use latitude $B$, longitude $L$, and height $h$. How does geodetic latitude $B$ differ from spherical latitude $\\varphi$?",
        correct="Geodetic latitude is the angle between the normal to the ellipsoid surface and the equatorial plane — this normal does not generally pass through the Earth's center",
        distractors=[
            "Geodetic latitude is measured from the North Pole rather than from the equator",
            "There is no difference; they are identical for any reference surface",
            "Geodetic latitude is always larger than spherical latitude"
        ]
    ),
    create_mc_question(
        id="ref_008", topic="ellipsoidal_coordinates",
        question="Converting from Cartesian $(x, y, z)$ to ellipsoidal coordinates $(B, L, h)$ is more complicated than the reverse. Why?",
        correct="Latitude $B$ depends on height $h$, and $h$ depends on $B$ (via the radius of curvature $N$), creating a circular dependency that requires iterative methods",
        distractors=[
            "The ellipsoid has no closed-form equation",
            "Cartesian coordinates are undefined near the poles",
            "The conversion requires knowledge of the geoid, which is not available analytically"
        ]
    ),
    create_mc_question(
        id="ref_009", topic="icrs",
        question="The International Celestial Reference System (ICRS) is based on extragalactic objects (quasars) rather than stars within our galaxy. Why?",
        correct="Quasars have quasi-zero proper motion due to their immense distance, providing effectively fixed reference points — unlike galactic stars which have noticeable proper motion",
        distractors=[
            "Quasars emit radio waves while stars emit only visible light",
            "There are more quasars than stars visible from Earth",
            "Quasars are located at the Solar System Barycenter"
        ]
    ),
    create_mc_question(
        id="ref_010", topic="icrs",
        question="The ICRS has its origin at the Solar System Barycenter (SSB). Its coordinate time is TCB (Barycentric Coordinate Time). Why can't TT (Terrestrial Time) be used as the time scale of the ICRS?",
        correct="TT is defined for an Earth-centered frame (GCRS) — due to General Relativity, time flows at different rates in different gravitational potentials, so using TT would inject Earth-specific relativistic effects into the barycentric description",
        distractors=[
            "TT is less accurate than TCB",
            "TT cannot measure intervals longer than 24 hours",
            "TT is only defined for ground-based clocks, not space-based systems"
        ]
    ),
    create_mc_question(
        id="ref_011", topic="itrs",
        question="The International Terrestrial Reference System (ITRS) is centered at the Geocenter. How is the Geocenter precisely determined?",
        correct="Through satellite observations — orbiting masses naturally reference the center of the gravity field, and the lowest-order spherical harmonic coefficients ($C_{10}$, $S_{11}$, $C_{11}$) are set to zero to force the center of mass to coincide with the coordinate origin",
        distractors=[
            "By measuring the geometric center of the Earth's solid surface",
            "By averaging the positions of all GNSS ground stations",
            "By locating the point of minimum gravitational acceleration"
        ]
    ),
    create_mc_question(
        id="ref_012", topic="itrs",
        question="The ITRS first axis ($\\mathbf{e}_1$) is defined by the intersection of the mean equator with the prime meridian through Greenwich. Why is this choice considered a political convention?",
        correct="The Greenwich meridian has no physical significance — it was chosen by international agreement, not dictated by any physical feature of the Earth",
        distractors=[
            "The Greenwich meridian coincides with a magnetic anomaly",
            "The prime meridian naturally aligns with the Earth's rotation axis",
            "All other observatories are equidistant from Greenwich"
        ]
    ),
    create_mc_question(
        id="ref_013", topic="reference_systems_overview",
        question="Four fundamental reference systems are used in space geodesy: ICRS, GCRS, ITRS, and a Local Horizon System. Which pair shares the same origin (Geocenter) but differs only in rotation?",
        correct="GCRS and ITRS — both are geocentric, but GCRS is non-rotating (fixed to space) while ITRS rotates with the Earth",
        distractors=[
            "ICRS and GCRS — both are celestial systems",
            "ITRS and Local Horizon — both are terrestrial systems",
            "ICRS and ITRS — one is celestial, one is terrestrial"
        ]
    ),
    create_mc_question(
        id="ref_014", topic="ecef_eci",
        question="ECEF (Earth-Centered Earth-Fixed) and ECI (Earth-Centered Inertial) are alternative terminologies used in navigation and aerospace. What do they correspond to in geodetic terminology?",
        correct="ECEF corresponds to the ITRS; ECI corresponds to the GCRS",
        distractors=[
            "ECEF corresponds to the GCRS; ECI corresponds to the ICRS",
            "Both ECEF and ECI correspond to the ITRS",
            "ECEF corresponds to the Local Horizon System; ECI corresponds to the ITRS"
        ]
    ),
    create_mc_question(
        id="ref_015", topic="transformations",
        question="The transformation from ICRS (barycentric) to GCRS (geocentric) accounts for the Earth's orbit around the Sun. What type of transformation is this?",
        correct="A relativistic spacetime transformation — it accounts for the change in dynamic state (metric) between the SSB and the Geocenter",
        distractors=[
            "A simple rotation matrix",
            "A Helmert similarity transformation with 7 parameters",
            "A coordinate conversion from spherical to Cartesian"
        ]
    ),
    create_mc_question(
        id="ref_016", topic="transformations",
        question="The transformation from GCRS to ITRS involves no translation (same origin). What does it involve?",
        correct="A series of time-dependent rotation matrices accounting for precession, nutation, Earth rotation angle (ERA), and polar motion",
        distractors=[
            "A single constant rotation matrix fixed at epoch J2000.0",
            "A scaling transformation to account for relativistic effects",
            "A reflection matrix to change handedness"
        ]
    ),
    create_mc_question(
        id="ref_017", topic="rotations",
        question="Rotation matrices $R_1(\\alpha)$, $R_2(\\beta)$, $R_3(\\gamma)$ define rotations around the three coordinate axes. A general 3D rotation can be decomposed into a sequence of basic rotations. What constraint applies?",
        correct="No two consecutive rotations may be around the same axis — e.g., $R_1 R_2 R_3$ is valid but $R_1 R_1 R_3$ is not",
        distractors=[
            "The rotations must always be applied in the order $R_1$, $R_2$, $R_3$",
            "Only two rotations are needed for any 3D rotation",
            "The angles must sum to 360°"
        ]
    ),
    tf(
        id="ref_018", topic="rotations",
        question="3D rotations are commutative — the order in which rotation matrices are applied does not matter.",
        correct=False
    ),
    create_mc_question(
        id="ref_019", topic="wgs84",
        question="WGS84 (World Geodetic System 1984) extends the ITRS by adding definitions of the Earth's size and shape. Which parameters define the WGS84 reference ellipsoid?",
        correct="Semi-major axis $a = 6378.137$ km and flattening $f = 1/298.257223563$",
        distractors=[
            "Only the Earth's mass and gravitational constant",
            "The geoid height at the equator and the polar radius",
            "The Earth's rotation rate and the speed of light"
        ]
    ),
    create_mc_question(
        id="ref_020", topic="local_horizon",
        question="The Local Horizon System is a topocentric coordinate system. Its vertical axis is defined by the local plumb line (gravity vector). Why is transforming from ITRS to a Local Horizon System challenging?",
        correct="The vertical direction is defined by a physical, non-geometric quantity (the local gravity vector), and its exact direction is typically approximated using the ellipsoid normal",
        distractors=[
            "The Local Horizon System uses a different time scale than ITRS",
            "The transformation requires knowledge of satellite positions",
            "The Local Horizon System is always right-handed while ITRS is left-handed"
        ]
    ),
    create_mc_question(
        id="ref_021", topic="local_horizon",
        question="In the Local Horizon System, the transformation from global to local coordinates involves rotation matrices and a reflection matrix $M_1$. Why is the reflection needed?",
        correct="To ensure the correct handedness of the local system — the Local Horizon System is a left-handed system (North-East-Zenith), requiring a reflection from the right-handed ITRS",
        distractors=[
            "To account for the Coriolis effect",
            "To invert the direction of gravity",
            "To convert from geocentric to heliocentric coordinates"
        ]
    ),
    create_mc_question(
        id="ref_022", topic="inertial_systems",
        question="The ICRS is described as 'quasi-inertial' rather than truly inertial. What is the distinction?",
        correct="A truly inertial system requires verifying zero net force ($\\sum F = 0$); the ICRS is only kinematically non-rotating (constrained by mathematical conditions on quasar positions), without verification of forces",
        distractors=[
            "The ICRS rotates slowly due to precession",
            "The ICRS is centered at the Geocenter rather than the SSB",
            "The ICRS uses optical observations instead of radio observations"
        ]
    ),
    create_mc_question(
        id="ref_023", topic="orientational_system",
        question="An orientational coordinate system is a degenerate spherical system where the radial distance $r$ is neglected or set to 1 (unit sphere). The celestial coordinate system uses two angles: right ascension $\\alpha$ and declination $\\delta$. What does this system describe?",
        correct="Only the direction to an object, not its distance — all objects are projected onto the celestial sphere",
        distractors=[
            "The full 3D position of celestial objects",
            "The velocity of objects along the line of sight",
            "The gravitational potential at each point on the sphere"
        ]
    ),
    tf(
        id="ref_024", topic="coordinate_systems",
        question="The Kronecker delta $\\delta_{ij}$ elegantly summarizes orthonormality: $\\mathbf{e}_i \\cdot \\mathbf{e}_j = \\delta_{ij}$, which equals 1 when $i = j$ (normality) and 0 when $i \\neq j$ (orthogonality).",
        correct=True
    ),
    create_mc_question(
        id="ref_025", topic="three_pillars",
        question="Space geodesy rests on three pillars. Which are they?",
        correct="Geometry (relative geometry of a body), gravity field (body as ensemble of mass particles), and Earth rotation",
        distractors=[
            "GNSS, SLR, and VLBI",
            "Coordinate systems, reference systems, and reference frames",
            "Precession, nutation, and polar motion"
        ]
    ),
    create_mc_question(
        id="ref_026", topic="helmert",
        question="The Helmert (similarity) transformation between two terrestrial reference frames uses 7 parameters. What are they?",
        correct="3 translations (origin shift), 3 rotations (orientation), and 1 scale factor",
        distractors=[
            "3 translations and 4 quaternion components",
            "6 rotation angles and 1 reflection parameter",
            "3 translations, 3 rotations, and 1 time parameter"
        ]
    ),
]

# ============================================================
# TOPIC: earth_orientation (L03) — 14 questions
# ============================================================
earth_orientation = [
    create_mc_question(
        id="eo_001", topic="earth_orientation_definition",
        question="Earth orientation describes the transformation between GCRS (non-rotating, space-fixed) and ITRS (rotating with Earth). This transformation is expressed as $\\mathbf{x}^* = W(t)\\,R(t)\\,Q(t)\\,\\mathbf{x}$. What do the three matrices represent?",
        correct="$Q(t)$: precession and nutation; $R(t)$: Earth rotation angle (ERA); $W(t)$: polar motion",
        distractors=[
            "$Q(t)$: polar motion; $R(t)$: precession; $W(t)$: nutation",
            "$Q(t)$: scaling; $R(t)$: translation; $W(t)$: rotation",
            "$Q(t)$: reflection; $R(t)$: ERA; $W(t)$: Helmert transformation"
        ]
    ),
    create_mc_question(
        id="eo_002", topic="precession",
        question="Precession is the slow circular motion of the Earth's rotation axis around the pole of the ecliptic, with a period of approximately:",
        correct="25,000 to 26,000 years",
        distractors=[
            "433 days (the Chandler period)",
            "18.6 years",
            "365.25 days"
        ]
    ),
    create_mc_question(
        id="eo_003", topic="precession_nutation",
        question="Both precession and nutation are caused by the same physical mechanism. What is it?",
        correct="Gravitational torques exerted by the Sun and Moon on the non-spherical (oblate) Earth, causing the rotating Earth to behave like a gyroscope",
        distractors=[
            "The centrifugal force due to Earth's rotation",
            "Magnetic interactions between the Earth's core and the Sun",
            "Tidal friction between the Earth and Moon"
        ]
    ),
    create_mc_question(
        id="eo_004", topic="nutation",
        question="Nutation represents periodic variations superimposed on the steady precession. What causes these periodic variations?",
        correct="The constantly changing geometry of the Sun-Moon-Earth system — the gravitational torques vary as the relative positions change",
        distractors=[
            "Irregularities in the Earth's internal mass distribution",
            "Variations in solar radiation pressure",
            "Changes in ocean currents"
        ]
    ),
    create_mc_question(
        id="eo_005", topic="polar_motion",
        question="Polar motion refers to the movement of the Celestial Intermediate Pole (CIP) relative to the ITRS pole (fixed to Earth's crust). What physical processes drive polar motion?",
        correct="Intrinsic processes within the Earth system — mass redistribution in the atmosphere, oceans, hydrosphere, and Earth's interior",
        distractors=[
            "Gravitational torques from the Sun and Moon (the same as precession)",
            "The Doppler effect of radio signals from quasars",
            "Solar wind pressure on the magnetosphere"
        ]
    ),
    create_mc_question(
        id="eo_006", topic="frequency_separation",
        question="In the Earth orientation equation $\\mathbf{x}^* = W(t)R(t)Q(t)\\mathbf{x}$, the effects are separated by frequency. How are polar motion and precession-nutation distinguished?",
        correct="Polar motion captures high-frequency effects (in the ITRS spectrum); precession-nutation captures low-frequency effects (in the GCRS spectrum), separated by a frequency shift of $-1$ cpsd (cycle per sidereal day)",
        distractors=[
            "Polar motion is constant; precession-nutation is time-varying",
            "They are separated by amplitude, not frequency",
            "Polar motion is secular; precession-nutation is periodic"
        ]
    ),
    create_mc_question(
        id="eo_007", topic="eop",
        question="Five Earth Orientation Parameters (EOP) are defined. Which set correctly lists all five?",
        correct="$dX$, $dY$ (celestial pole offsets), ERA/UT1 (Earth rotation angle), $x_p$, $y_p$ (polar motion coordinates)",
        distractors=[
            "Precession rate, nutation amplitude, ERA, LOD, polar wander",
            "Latitude, longitude, height, rotation rate, axial tilt",
            "Three Euler angles and two translation components"
        ]
    ),
    create_mc_question(
        id="eo_008", topic="eop_observation",
        question="Which space geodetic technique is the only one that can directly observe all five Earth Orientation Parameters?",
        correct="VLBI — because it directly observes quasars (objects in the GCRS), realizing the celestial reference frame",
        distractors=[
            "GNSS — because it has the most satellites",
            "SLR — because it has the highest ranging accuracy",
            "DORIS — because it uses the Doppler effect"
        ]
    ),
    create_mc_question(
        id="eo_009", topic="tidal_friction",
        question="Tidal friction causes the Earth's rotation to decelerate. Due to conservation of angular momentum in the Earth-Moon system, what is the observable consequence?",
        correct="The Earth-Moon distance increases by about 3.82 cm/year, measurable by Lunar Laser Ranging (LLR)",
        distractors=[
            "The Moon's rotation rate increases",
            "The Earth's orbit around the Sun expands",
            "The axial tilt of the Earth decreases"
        ]
    ),
    create_mc_question(
        id="eo_010", topic="tidal_friction",
        question="Paleontological evidence from fossil coral growth rings confirms that Earth's rotation has slowed over geological time. What does this evidence show?",
        correct="Hundreds of millions of years ago, a year contained significantly more solar days than it does today",
        distractors=[
            "The Earth used to rotate in the opposite direction",
            "The length of a year has decreased over time",
            "The Moon was much farther from Earth in the past"
        ]
    ),
    tf(
        id="eo_011", topic="eop_predictability",
        question="Earth Orientation Parameters (EOP) are precisely predictable far into the future, so they do not need to be continuously observed.",
        correct=False  # EOP are only predictable for about 7 days; they must be observed
    ),
    create_mc_question(
        id="eo_012", topic="rotation_matrices",
        question="In the kinematic definition of Earth orientation, the Celestial Intermediate Pole (CIP) is defined as a pole that is constant for 24 hours. What purpose does this serve?",
        correct="It creates a stable intermediate reference system that allows the large Earth rotation $R(t)$ to be treated separately and consistently over short time periods",
        distractors=[
            "It eliminates the need for precession corrections entirely",
            "It defines a pole that never changes position in the GCRS",
            "It allows polar motion to be ignored in the transformation"
        ]
    ),
    create_mc_question(
        id="eo_013", topic="satellite_eop",
        question="Satellite techniques (GNSS, SLR, DORIS) cannot determine the full set of EOP as well as VLBI. What is the fundamental limitation?",
        correct="The satellite orbits are perturbed by non-gravitational forces that are difficult to model, so they can only approximate a stable celestial system for short periods — this creates correlations between EOP and orbital parameters",
        distractors=[
            "Satellites cannot observe objects outside the solar system",
            "The satellite signals are too weak for precise measurements",
            "Satellite techniques use only one frequency"
        ]
    ),
    create_mc_question(
        id="eo_014", topic="ring_laser",
        question="Ring laser gyroscopes (such as ROMY near Munich) can monitor Earth rotation in real time. How do they work?",
        correct="They establish an inertial plane of laser beams and measure rotations with respect to this plane — measuring absolute rotation without reference to satellites or celestial objects",
        distractors=[
            "They reflect laser beams off satellites and measure the Doppler shift",
            "They use GPS signals to determine the rotation rate",
            "They measure changes in the Earth's magnetic field"
        ]
    ),
]

# ============================================================
# TOPIC: gnss_fundamentals (L04) — 18 questions
# ============================================================
gnss_fundamentals = [
    create_mc_question(
        id="gnss1_001", topic="gnss_constellations",
        question="GNSS is an umbrella term for multiple satellite navigation constellations. Which of the following is NOT a GNSS constellation?",
        correct="DORIS — it is a tracking system using the Doppler effect, not a navigation constellation",
        distractors=[
            "GPS (United States)",
            "GLONASS (Russia)",
            "Galileo (European Union)"
        ]
    ),
    create_mc_question(
        id="gnss1_002", topic="trilateration",
        question="In 2D positioning using range measurements, how many distance measurements to known points are needed for a unique solution?",
        correct="Three — two circles intersect at two points (ambiguous), a third circle resolves the ambiguity",
        distractors=[
            "One — a single range defines a unique position",
            "Two — two ranges always give a unique intersection",
            "Four — the same number as in 3D positioning"
        ]
    ),
    create_mc_question(
        id="gnss1_003", topic="four_unknowns",
        question="In real-world GNSS 3D positioning, a minimum of four satellite measurements is required. Why four instead of three?",
        correct="In addition to the three unknown coordinates $(x, y, z)$, there is a fourth unknown: the receiver clock error $u_R$, which must be solved simultaneously",
        distractors=[
            "Four satellites are needed to resolve carrier phase ambiguities",
            "The ionosphere introduces one additional unknown per satellite",
            "Four measurements are needed to correct for tropospheric delay"
        ]
    ),
    create_mc_question(
        id="gnss1_004", topic="pseudorange",
        question="A GNSS receiver measures the time-of-fly (ToF) of a signal from the satellite and multiplies by the speed of light to get a range. Why is this called a pseudorange rather than a true range?",
        correct="Because the satellite and receiver clocks are not perfectly synchronized — the clock errors contaminate the measured range, so it is only an approximation of the true geometric distance",
        distractors=[
            "Because the signal travels through a vacuum where the speed of light is only approximate",
            "Because the receiver cannot determine which satellite sent the signal",
            "Because the measurement is made using radio waves, not laser light"
        ]
    ),
    create_mc_question(
        id="gnss1_005", topic="pseudorange_equation",
        question="The pseudorange observation equation is $\\rho_R^S = [(X^S - x_R)^2 + (Y^S - y_R)^2 + (Z^S - z_R)^2]^{1/2} + (u_R - u^S)c$. What does the term $(u_R - u^S)c$ represent?",
        correct="The total range error due to the clock difference between receiver and satellite, converted to meters by multiplying by the speed of light",
        distractors=[
            "The ionospheric delay in meters",
            "The tropospheric delay in meters",
            "The multipath error in meters"
        ]
    ),
    create_mc_question(
        id="gnss1_006", topic="carrier_phase",
        question="Carrier phase measurements are much more precise than code (pseudorange) measurements. What is the key challenge introduced by carrier phase measurements?",
        correct="The integer ambiguity $N$ — the receiver does not know how many full carrier wavelength cycles were between the satellite and receiver when tracking started",
        distractors=[
            "The carrier frequency is unknown and must be estimated",
            "The carrier wave cannot penetrate the ionosphere",
            "Carrier phase measurements require an atomic clock in the receiver"
        ]
    ),
    create_mc_question(
        id="gnss1_007", topic="carrier_phase",
        question="In the carrier phase observational equation $L_R^S = \\rho_{SR} + (u_R - u^S)c + \\lambda N_R^S + (\\alpha_R + \\alpha^S) + B_{\\text{carrier}}$, the ambiguity $N_R^S$ remains constant as long as:",
        correct="The receiver continuously tracks the satellite signal without losing lock — if tracking is interrupted (e.g., by an obstruction), $N$ changes and must be re-determined",
        distractors=[
            "The satellite maintains its orbital position",
            "The ionospheric conditions remain stable",
            "The receiver clock does not drift"
        ]
    ),
    create_mc_question(
        id="gnss1_008", topic="code_vs_carrier",
        question="Code (pseudorange) measurements have meter-level accuracy while carrier phase measurements achieve millimeter-level accuracy. Why does high-precision GNSS surveying use both?",
        correct="Code measurements give noisy but unambiguous distances (no integer ambiguity), while carrier phase is precise but ambiguous — code is used to find an approximate solution, which then helps resolve the integer ambiguity",
        distractors=[
            "Code measurements work in the ionosphere while carrier phase works in the troposphere",
            "Code is used for horizontal positioning and carrier phase for vertical",
            "They measure fundamentally different physical quantities"
        ]
    ),
    create_mc_question(
        id="gnss1_009", topic="signal_modulation",
        question="A GNSS navigation signal is created by modulating a PRN (Pseudorandom Noise) code onto a carrier wave. What does the modulation physically do?",
        correct="The code values ($\\pm 1$) multiply the carrier, effectively flipping the phase of the carrier wave by 180° to encode the digital information",
        distractors=[
            "It changes the frequency of the carrier wave",
            "It increases the amplitude of the carrier wave",
            "It reduces the wavelength of the carrier wave"
        ]
    ),
    create_mc_question(
        id="gnss1_010", topic="radio_waves",
        question="GNSS systems use signals in the L-Band (approximately 1.2–1.6 GHz). Why is this frequency range chosen?",
        correct="L-Band signals can penetrate the atmosphere and ionosphere with manageable distortion while being high enough to carry the necessary data",
        distractors=[
            "L-Band signals travel faster than the speed of light in the ionosphere",
            "L-Band is the only frequency range not affected by multipath",
            "L-Band signals can be generated without atomic clocks"
        ]
    ),
    create_mc_question(
        id="gnss1_011", topic="tof_measurement",
        question="A GNSS receiver determines the Time-of-Fly (ToF) by comparing the received satellite PRN code with an internally generated replica. How is the ToF measured?",
        correct="The receiver time-shifts its internal replica code until it perfectly correlates with the received code — the required time shift equals the signal travel time",
        distractors=[
            "The receiver measures the frequency difference between sent and received signals",
            "The receiver counts the number of carrier wave cycles",
            "The receiver uses a stopwatch triggered by the satellite's navigation message"
        ]
    ),
    create_mc_question(
        id="gnss1_012", topic="satellite_clock",
        question="In the pseudorange equation, the satellite clock correction $u^S$ is handled differently from the receiver clock correction $u_R$. Why?",
        correct="The satellite clock correction $u^S$ is calculated by the control segment and transmitted to the receiver as part of the navigation message — it is assumed known. The receiver clock correction $u_R$ remains an unknown that must be estimated",
        distractors=[
            "The satellite clock is perfect and has no error",
            "Both corrections are unknown and estimated simultaneously",
            "The receiver clock correction is always zero for atomic clocks"
        ]
    ),
    create_mc_question(
        id="gnss1_013", topic="positioning_geometry",
        question="In 2D positioning, the intersection of distance circles from known points is called trilateration. In 3D GNSS positioning, the surfaces of position are:",
        correct="Spheres centered on each satellite — the receiver lies at the intersection of four or more spheres",
        distractors=[
            "Planes tangent to each satellite's orbit",
            "Cones with vertices at each satellite",
            "Cylinders aligned with the satellite-receiver direction"
        ]
    ),
    tf(
        id="gnss1_014", topic="gnss_advantages",
        question="GNSS positioning works only in clear weather conditions and requires direct line-of-sight to the sky.",
        correct=False  # GNSS is an all-weather technique, though it does need sky visibility
    ),
    create_mc_question(
        id="gnss1_015", topic="doppler",
        question="GNSS receivers can also measure the Doppler shift of the carrier wave. What information does the Doppler measurement primarily provide?",
        correct="The rate of change of the satellite-receiver distance, which gives the receiver's velocity",
        distractors=[
            "The absolute distance to the satellite",
            "The ionospheric electron content along the signal path",
            "The satellite's clock correction"
        ]
    ),
    tf(
        id="gnss1_016", topic="phase_concept",
        question="The total phase of a carrier wave $\\Phi_t = \\omega t + \\phi_0$ increases continuously over time. One full cycle corresponds to a phase change of $2\\pi$ radians.",
        correct=True
    ),
    create_mc_question(
        id="gnss1_017", topic="slr_limitation",
        question="Satellite Laser Ranging (SLR) provides extremely precise range measurements. Why is it not used for general navigation like GNSS?",
        correct="SLR requires large, stationary, specialized equipment at fixed ground stations — it cannot be miniaturized into portable receivers",
        distractors=[
            "Laser signals cannot penetrate clouds",
            "SLR is less accurate than GNSS",
            "SLR satellites are too few for global coverage"
        ]
    ),
    create_mc_question(
        id="gnss1_018", topic="measurement_types",
        question="The two primary GNSS observables are code-phase (pseudorange) and carrier-phase measurements. Their observational equations are structurally very similar. What is the key structural difference?",
        correct="The carrier-phase equation includes an integer ambiguity term $\\lambda N_R^S$ that is absent in the pseudorange equation",
        distractors=[
            "The pseudorange equation includes a tropospheric term that the carrier-phase equation lacks",
            "The carrier-phase equation uses a different geometric distance formula",
            "The pseudorange equation accounts for relativistic effects while the carrier-phase equation does not"
        ]
    ),
]

# ============================================================
# TOPIC: gnss_signals_errors (L05) — 23 questions
# ============================================================
gnss_signals_errors = [
    create_mc_question(
        id="gnss2_001", topic="gps_signals",
        question="GPS satellites transmit signals on two primary frequencies, L1 (1575.42 MHz, $\\lambda \\approx 19$ cm) and L2 (1227.60 MHz, $\\lambda \\approx 24.4$ cm). Why are two frequencies necessary?",
        correct="Dual-frequency reception allows the receiver to calculate and remove the frequency-dependent ionospheric delay, which is the largest single error source",
        distractors=[
            "Two frequencies double the data transmission rate",
            "L1 is used for civilian users and L2 is exclusively for military use",
            "Two frequencies are needed to measure the Doppler shift"
        ]
    ),
    create_mc_question(
        id="gnss2_002", topic="ca_code",
        question="The C/A (Coarse/Acquisition) code on GPS L1 has a chipping rate of 1023 chips per millisecond and a code wavelength of approximately 293 m. What two purposes does the C/A code serve?",
        correct="Satellite identification (each satellite has a unique C/A code) and timing/pseudorange measurement (by correlating the received code with the receiver's internal replica)",
        distractors=[
            "Encryption of the military signal and ionospheric correction",
            "Satellite orbit determination and clock synchronization",
            "Carrier phase tracking and ambiguity resolution"
        ]
    ),
    create_mc_question(
        id="gnss2_003", topic="p_code",
        question="The P-code (Precise code) is transmitted on both L1 and L2 frequencies. What distinguishes it from the C/A code?",
        correct="The P-code has a much higher chipping rate and shorter wavelength (29.3 m vs. 293 m), providing higher precision, and it is encrypted as Y-code ($Y = P \\cdot W$) for authorized users only",
        distractors=[
            "The P-code is transmitted only on L1 while C/A is on both L1 and L2",
            "The P-code has a longer wavelength, providing better atmospheric penetration",
            "The P-code carries the navigation message while C/A does not"
        ]
    ),
    create_mc_question(
        id="gnss2_004", topic="signal_structure",
        question="The GPS L1 signal can be written as $S_{L1}(t) = A_P P(t)D(t)\\sin(\\omega_1 t + \\phi_1) + A_C C(t)D(t)\\cos(\\omega_1 t + \\phi_1)$. The two terms are called I-term and Q-term. Why are sine and cosine used?",
        correct="The P-code and C/A code are transmitted simultaneously on the same frequency by placing them in quadrature (90° phase offset) — this prevents them from interfering with each other",
        distractors=[
            "Sine is for ascending satellite paths and cosine for descending",
            "Sine carries the code and cosine carries the navigation message",
            "One is for military and one for civilian — they use different modulation"
        ]
    ),
    create_mc_question(
        id="gnss2_005", topic="ionosphere",
        question="The ionosphere delays code measurements but advances carrier phase measurements. How does this difference manifest in the observational equations?",
        correct="The ionospheric term $I$ appears with a positive sign in the code equation and a negative sign in the carrier-phase equation",
        distractors=[
            "The ionosphere affects code measurements but has no effect on carrier phase",
            "Both code and carrier phase are delayed equally by the ionosphere",
            "The ionosphere affects only L2 frequency signals, not L1"
        ]
    ),
    create_mc_question(
        id="gnss2_006", topic="error_sources",
        question="The User Equivalent Range Error (UERE) summarizes all random error influences on the satellite-receiver range. The final positioning accuracy depends on:",
        correct="UERE multiplied by the Dilution of Precision (DOP) — poor satellite geometry amplifies the range errors",
        distractors=[
            "UERE divided by the number of visible satellites",
            "UERE multiplied by the carrier wavelength",
            "UERE alone — satellite geometry has no effect"
        ]
    ),
    create_mc_question(
        id="gnss2_007", topic="error_magnitudes",
        question="Among all GNSS error sources, which one has the largest typical magnitude (up to 100 meters) if left uncorrected?",
        correct="Ionospheric delay — it ranges from 1 to 100 meters and requires dual-frequency or model correction",
        distractors=[
            "Tropospheric delay (5 to 40 cm)",
            "Multipath on carrier phase (1 to 5 cm)",
            "Satellite clock error (5 to 20 cm after correction)"
        ]
    ),
    create_mc_question(
        id="gnss2_008", topic="carrier_phase_accuracy",
        question="The instrumental noise of carrier-phase measurements is approximately:",
        correct="$\\pm 0.2$ to $\\pm 5$ mm — over 100 times more precise than code measurements",
        distractors=[
            "$\\pm 10$ to $\\pm 100$ cm",
            "$\\pm 1$ to $\\pm 10$ m",
            "$\\pm 1$ to $\\pm 5$ cm"
        ]
    ),
    create_mc_question(
        id="gnss2_009", topic="cycle_slips",
        question="A cycle slip in GNSS carrier-phase tracking occurs when:",
        correct="The receiver temporarily loses lock on the satellite signal (e.g., due to obstruction), causing an abrupt jump in the integer ambiguity count",
        distractors=[
            "The satellite switches from one PRN code to another",
            "The ionospheric delay exceeds the carrier wavelength",
            "The receiver's battery voltage drops below a threshold"
        ]
    ),
    create_mc_question(
        id="gnss2_010", topic="multipath",
        question="Multipath is a significant GNSS error source. What causes multipath errors?",
        correct="The signal reaches the receiver not only directly from the satellite but also via reflections off nearby surfaces (buildings, ground), causing additional delayed signal copies",
        distractors=[
            "Multiple satellites transmitting on the same frequency",
            "The signal splitting into multiple frequencies in the ionosphere",
            "The receiver processing signals from multiple constellations simultaneously"
        ]
    ),
    create_mc_question(
        id="gnss2_011", topic="gnss_segments",
        question="A fully operational GNSS consists of three main segments. The Control Segment includes monitoring stations, a master control station, and ground control stations. What is its primary function?",
        correct="Continuously tracking satellites to estimate their precise orbits and clock parameters, then uploading corrections to the satellites for broadcast to users",
        distractors=[
            "Manufacturing and launching new satellites",
            "Providing real-time positioning to military users only",
            "Operating the receiver hardware for end users"
        ]
    ),
    create_mc_question(
        id="gnss2_012", topic="igs",
        question="The International GNSS Service (IGS) operates a global network of over 500 permanent tracking stations. What products does it provide?",
        correct="Precise satellite orbits (cm-level), precise clock corrections, station coordinates and velocities, and Earth Rotation Parameters — far more accurate than the broadcast navigation message",
        distractors=[
            "Only raw observation data from tracking stations",
            "Only ionospheric correction models",
            "Only the broadcast ephemeris in a different format"
        ]
    ),
    create_mc_question(
        id="gnss2_013", topic="space_segment",
        question="The GPS constellation requires a minimum of 24 satellites to ensure global coverage. Why is this the minimum?",
        correct="To guarantee that at least four satellites are visible from any point on Earth's surface at any time — four are needed to solve for three coordinates plus the receiver clock error",
        distractors=[
            "24 satellites can each cover exactly 15° of longitude",
            "24 is the maximum number that can fit in the MEO altitude band",
            "Each satellite must have a backup, so 24 = 12 active + 12 backup"
        ]
    ),
    create_mc_question(
        id="gnss2_014", topic="antenna_coverage",
        question="GPS satellite antennas point toward the Earth's center and their signal beam covers about 27.8° as viewed from the satellite. What area does this cover?",
        correct="The entire visible disk of the Earth plus an additional zone extending to approximately 3,000 km above the surface",
        distractors=[
            "Only a 100 km spot directly below the satellite",
            "Exactly one hemisphere of the Earth",
            "The entire sphere of the Earth including the far side"
        ]
    ),
    create_mc_question(
        id="gnss2_015", topic="differential_gnss",
        question="Differential GNSS (DGNSS) improves positioning accuracy by using a reference station at a known location. What principle does it exploit?",
        correct="Errors affecting the reference station and nearby user receiver are strongly correlated — the reference station computes corrections from its known position and transmits them to the user",
        distractors=[
            "The reference station has an atomic clock that eliminates all clock errors",
            "DGNSS uses two frequencies while standard GNSS uses only one",
            "The reference station directly measures ionospheric electron density"
        ]
    ),
    create_mc_question(
        id="gnss2_016", topic="dop",
        question="The Dilution of Precision (DOP) quantifies the effect of satellite geometry on positioning accuracy. What satellite configuration gives the worst (highest) DOP?",
        correct="When all visible satellites are clustered close together in the sky — this amplifies the effect of measurement errors on the position solution",
        distractors=[
            "When satellites are evenly distributed across the sky",
            "When exactly four satellites are visible at the zenith",
            "When satellites are at low elevation angles"
        ]
    ),
    create_mc_question(
        id="gnss2_017", topic="itrf_wgs84",
        question="The ITRF (International Terrestrial Reference Frame) and WGS84 are closely related. How?",
        correct="WGS84 is aligned with the ITRF — the IGS provides precise GNSS data combined with other techniques (SLR, VLBI) to maintain the ITRF, and commercial GPS (WGS84) is kept consistent with it",
        distractors=[
            "WGS84 is an entirely independent reference frame with no connection to ITRF",
            "ITRF is the American version and WGS84 is the European version",
            "WGS84 was replaced by ITRF in 2000"
        ]
    ),
    create_mc_question(
        id="gnss2_018", topic="l5_frequency",
        question="A third civilian frequency, L5 (1176.45 MHz), is being added to GPS satellites. What is its primary purpose?",
        correct="Providing greater robustness and accuracy — a third frequency enables better ionospheric correction, improved ambiguity resolution, and a safety-of-life signal for aviation",
        distractors=[
            "Replacing L2 for military use",
            "Enabling communication between GPS satellites",
            "Transmitting weather data to receivers"
        ]
    ),
    create_mc_question(
        id="gnss2_019", topic="pcv",
        question="Antenna Phase Center Variations (PCV) are an error source in precise GNSS positioning. What are they?",
        correct="The physical point from which the antenna effectively receives the signal varies slightly with the direction of the incoming signal, introducing direction-dependent position errors",
        distractors=[
            "Changes in the satellite's orbital velocity that affect the carrier phase",
            "Variations in the ionospheric delay due to the satellite's elevation angle",
            "Fluctuations in the receiver's internal temperature"
        ]
    ),
    tf(
        id="gnss2_020", topic="code_unambiguous",
        question="Code (pseudorange) measurements are unambiguous — unlike carrier phase measurements, they do not have an integer ambiguity.",
        correct=True
    ),
    create_mc_question(
        id="gnss2_021", topic="acquisition",
        question="When a GNSS receiver first acquires a satellite signal, what process must it perform?",
        correct="Search for the correct code delay and Doppler shift by aligning its internal PRN code replica and adjusting frequency to match the received signal — once stable alignment is achieved, tracking begins",
        distractors=[
            "Send a request signal to the satellite asking for its navigation message",
            "Wait for the satellite to pass directly overhead for best signal strength",
            "Download the complete almanac from the internet before any signal processing"
        ]
    ),
    create_mc_question(
        id="gnss2_022", topic="ambiguity_resolution",
        question="Resolving the integer ambiguity $N$ in carrier-phase GNSS is critical for achieving centimeter-level accuracy. What approaches are used?",
        correct="Using multiple satellites, multiple epochs, and/or multiple frequencies to over-determine the system and fix $N$ to its correct integer value",
        distractors=[
            "Increasing the receiver's crystal oscillator frequency",
            "Using only one satellite for a very long observation time",
            "Switching from carrier phase to code-only measurements"
        ]
    ),
    create_mc_question(
        id="gnss2_023", topic="hardware_delays",
        question="In the extended GNSS observational models, hardware delays $\\alpha_R$, $\\alpha^S$ (carrier) and $\\beta_R$, $\\beta^S$ (code) appear. Why are carrier hardware delays and code hardware delays different?",
        correct="The signal paths through the satellite and receiver electronics are different for the code and carrier processing chains, introducing different systematic delays",
        distractors=[
            "Code uses digital processing while carrier uses analog processing",
            "Code delays are known exactly while carrier delays are unknown",
            "They are actually the same but given different symbols by convention"
        ]
    ),
]

# ============================================================
# TOPIC: gnss_remote_sensing (L06) — 10 questions
# ============================================================
gnss_remote_sensing = [
    create_mc_question(
        id="gnssrs_001", topic="concept",
        question="GNSS Remote Sensing turns what are normally considered errors in positioning into useful scientific signals. Which GNSS 'errors' are exploited?",
        correct="Atmospheric delays (ionospheric and tropospheric) and signal reflections — these contain information about the atmosphere and Earth's surface",
        distractors=[
            "Satellite clock errors and orbital perturbations",
            "Receiver noise and multipath from buildings",
            "Integer ambiguities and cycle slips"
        ]
    ),
    create_mc_question(
        id="gnssrs_002", topic="ground_based",
        question="Ground-based GNSS atmosphere sounding derives two key quantities from the signal delays. What are TEC and IWV?",
        correct="TEC (Total Electron Content) is derived from the ionospheric delay; IWV (Integrated Water Vapor) is derived from the tropospheric delay",
        distractors=[
            "TEC (Total Error Correction) and IWV (Intermediate Wave Velocity)",
            "TEC (Terrestrial Earth Coordinates) and IWV (Ionospheric Wave Variation)",
            "TEC (Thermal Energy Content) and IWV (Ice Volume Water)"
        ]
    ),
    create_mc_question(
        id="gnssrs_003", topic="radio_occultation",
        question="GNSS Radio Occultation (RO) is a satellite-based technique for atmosphere sounding. What is its basic principle?",
        correct="A LEO satellite receives GNSS signals that pass through the Earth's atmosphere at the limb — the signal bending and delay profile reveals the atmospheric refractivity (temperature, pressure, humidity) as a function of altitude",
        distractors=[
            "Bouncing GNSS signals off the ocean surface and measuring the reflection",
            "Measuring the Doppler shift of GNSS signals due to Earth's rotation",
            "Using GNSS signals to detect lightning in the ionosphere"
        ]
    ),
    create_mc_question(
        id="gnssrs_004", topic="reflectometry",
        question="GNSS Reflectometry (GNSS-R) is an innovative observation technique. What does it measure?",
        correct="Properties of the Earth's surface (sea state, soil moisture, ice thickness) by analyzing GNSS signals reflected off the surface",
        distractors=[
            "The reflectivity of satellite solar panels",
            "The reflection of laser pulses from retroreflectors on satellites",
            "The phase of signals reflected within the receiver hardware"
        ]
    ),
    tf(
        id="gnssrs_005", topic="climate",
        question="GNSS-derived tropospheric delays can be used for long-term climate monitoring, including water vapor trend analysis over decades.",
        correct=True
    ),
    create_mc_question(
        id="gnssrs_006", topic="ionospheric_maps",
        question="The IGS produces Global Ionospheric Maps (GIM) from GNSS data. What quantity do these maps display?",
        correct="The Total Electron Content (TEC) of the ionosphere, mapped globally from the distributed network of GNSS ground stations",
        distractors=[
            "The temperature profile of the ionosphere",
            "The wind speed at ionospheric altitudes",
            "The density of neutral atoms in the ionosphere"
        ]
    ),
    create_mc_question(
        id="gnssrs_007", topic="cosmic",
        question="The COSMIC and COSMIC-2 missions are major GNSS Radio Occultation satellite constellations. What makes them valuable for weather and climate science?",
        correct="They provide thousands of globally distributed vertical atmosphere profiles daily with high accuracy — these are assimilated into weather forecast models and used for climate monitoring",
        distractors=[
            "They carry radar instruments for direct cloud measurement",
            "They replace weather balloons entirely",
            "They provide real-time positioning for aircraft"
        ]
    ),
    create_mc_question(
        id="gnssrs_008", topic="ztd",
        question="ZTD (Zenith Total Delay) is a key parameter in GNSS meteorology. What does it represent?",
        correct="The total signal delay caused by the troposphere for a signal arriving from the zenith — it is the sum of the hydrostatic (dry) and wet delay components",
        distractors=[
            "The delay caused by the ionosphere at zenith",
            "The total time for a signal to travel from satellite to receiver",
            "The clock error accumulated over one day"
        ]
    ),
    create_mc_question(
        id="gnssrs_009", topic="sbas",
        question="Satellite-Based Augmentation Systems (SBAS) like WAAS, EGNOS, and MSAS improve GNSS accuracy. How do they work?",
        correct="They use a network of ground reference stations to compute atmospheric, orbital, and clock corrections, which are then broadcast to users via geostationary satellites in real time",
        distractors=[
            "They add additional navigation satellites to improve geometry",
            "They encrypt the GNSS signal for higher precision",
            "They replace the standard GNSS signals with more precise ones"
        ]
    ),
    create_mc_question(
        id="gnssrs_010", topic="smartphone_gnss",
        question="Recent research has explored using GNSS data from smartphones for atmospheric sensing. What is the main challenge compared to geodetic-grade receivers?",
        correct="Smartphones have lower-quality antennas with more noise, multipath, and less stable clocks — but with large numbers of devices, statistical methods can still extract useful atmospheric information",
        distractors=[
            "Smartphones cannot receive GNSS signals at all",
            "Smartphones only receive L1 frequency, making ionospheric correction impossible",
            "Smartphone GNSS chips are deliberately degraded by manufacturers"
        ]
    ),
]

# ============================================================
# TOPIC: satellite_orbits (L07) — 14 questions
# ============================================================
satellite_orbits = [
    create_mc_question(
        id="orb_001", topic="gravity",
        question="The gravitational acceleration $g$ at distance $r$ from a body of mass $M$ is $g = GM/r^2$. The product $GM$ is called the gravitational parameter. At Earth's surface ($r \\approx 6370$ km), $g \\approx$:",
        correct="9.8 m/s²",
        distractors=[
            "1.6 m/s² (that's the Moon's surface gravity)",
            "3.7 m/s² (that's Mars' surface gravity)",
            "0.034 m/s² (that's the centrifugal acceleration at the equator)"
        ]
    ),
    create_mc_question(
        id="orb_002", topic="circular_orbit",
        question="For a stable circular orbit, gravitational force must equal centrifugal force: $GMm/r^2 = mv^2/r$. From this, the orbital speed $v$ and period $T$ are derived. How does the orbital period $T$ relate to the orbital radius $r$?",
        correct="$T^2 = \\frac{4\\pi^2}{GM}r^3$ — the period squared is proportional to the cube of the radius (Kepler's third law)",
        distractors=[
            "$T = 2\\pi r/GM$ — the period is linearly proportional to the radius",
            "$T^2 = GM/r$ — the period squared is inversely proportional to the radius",
            "$T = \\sqrt{r/GM}$ — the period is proportional to the square root of the radius"
        ]
    ),
    create_mc_question(
        id="orb_003", topic="escape_velocity",
        question="The escape velocity from distance $r$ is $v_e = \\sqrt{2GM/r}$. How does it compare to the circular orbital velocity $v_c = \\sqrt{GM/r}$ at the same distance?",
        correct="The escape velocity is exactly $\\sqrt{2}$ (about 1.41) times the orbital velocity — a satellite in circular orbit needs only a 41% speed increase to escape",
        distractors=[
            "The escape velocity is twice the orbital velocity",
            "The escape velocity is half the orbital velocity",
            "They are equal — any orbiting body can escape at its orbital speed"
        ]
    ),
    create_mc_question(
        id="orb_004", topic="kepler_first",
        question="Kepler's First Law states that planetary orbits are ellipses with the central body at one focus. What defines the shape of the ellipse?",
        correct="Two parameters: the semi-major axis $a$ (size) and the eccentricity $e$ (how elongated the ellipse is, from $e=0$ for a circle to $e \\to 1$ for a very elongated orbit)",
        distractors=[
            "The semi-major axis and the inclination",
            "The period and the mean anomaly",
            "The mass of the orbiting body and the central body"
        ]
    ),
    create_mc_question(
        id="orb_005", topic="kepler_second",
        question="Kepler's Second Law states that a line connecting a planet to the Sun sweeps out equal areas in equal times. What physical principle is this equivalent to?",
        correct="Conservation of angular momentum — when the planet is closer to the Sun ($r$ decreases), it must speed up ($v$ increases) to keep $L = mvr$ constant",
        distractors=[
            "Conservation of energy",
            "Conservation of linear momentum",
            "Newton's third law of action and reaction"
        ]
    ),
    create_mc_question(
        id="orb_006", topic="orbital_elements",
        question="A satellite orbit is fully described by six Keplerian orbital elements. Which element determines the orientation of the orbital plane relative to the equatorial plane?",
        correct="Inclination $i$ — the angle between the orbital plane and the equatorial plane",
        distractors=[
            "Eccentricity $e$ — the shape of the orbit",
            "Argument of perigee $\\omega$ — the orientation of the ellipse within the orbital plane",
            "Mean anomaly $M$ — the position of the satellite along the orbit"
        ]
    ),
    create_mc_question(
        id="orb_007", topic="orbit_types",
        question="GNSS satellites (GPS, Galileo, GLONASS) orbit in MEO (Medium Earth Orbit). What altitude range characterizes MEO?",
        correct="Approximately 2,000 to 36,000 km — GPS satellites are at about 20,200 km with an orbital period of approximately 12 hours",
        distractors=[
            "200 to 2,000 km (that is LEO)",
            "Exactly 35,786 km (that is geostationary orbit)",
            "Beyond 36,000 km (that is HEO)"
        ]
    ),
    create_mc_question(
        id="orb_008", topic="geo",
        question="A geostationary orbit (GEO) has a period of exactly 24 hours and the satellite appears stationary over the equator. What orbital characteristics are required?",
        correct="Circular orbit ($e = 0$), equatorial plane ($i = 0°$), altitude of approximately 35,786 km, and prograde direction (same direction as Earth's rotation)",
        distractors=[
            "Any circular orbit at any altitude with period 24 hours",
            "An elliptical orbit with apogee at 35,786 km",
            "A polar orbit at high altitude"
        ]
    ),
    create_mc_question(
        id="orb_009", topic="sun_synchronous",
        question="A sun-synchronous orbit crosses the equator at the same local solar time on every pass. What orbital property enables this?",
        correct="The orbit's ascending node precesses at exactly 360°/year (about 0.986°/day) due to the Earth's oblateness ($J_2$ effect), matching the Earth's motion around the Sun",
        distractors=[
            "The orbit is exactly polar (inclination = 90°)",
            "The satellite adjusts its orbit using thrusters every day",
            "The satellite is in a geostationary orbit over the terminator"
        ]
    ),
    create_mc_question(
        id="orb_010", topic="energy_conservation",
        question="For a satellite in orbit, the sum of kinetic energy $E = mv^2/2$ and gravitational potential energy $U = -GMm/r$ remains constant. What does this imply?",
        correct="As the satellite moves closer to Earth ($r$ decreases), it speeds up ($v$ increases) — potential energy converts to kinetic energy, and vice versa",
        distractors=[
            "The satellite moves at constant speed throughout its orbit",
            "The satellite's altitude remains constant",
            "Energy is continuously added by gravitational forces"
        ]
    ),
    create_mc_question(
        id="orb_011", topic="leo",
        question="Low Earth Orbit (LEO) is defined as orbits below approximately 2,000 km. What is a key challenge for satellites in LEO?",
        correct="Atmospheric drag — residual atmosphere at LEO altitudes gradually decelerates the satellite, causing orbital decay that requires periodic re-boosting",
        distractors=[
            "LEO satellites are invisible to ground stations",
            "LEO satellites cannot achieve stable orbits",
            "Solar radiation is blocked by the Earth at LEO altitudes"
        ]
    ),
    create_mc_question(
        id="orb_012", topic="lagrange",
        question="Lagrangian points are positions where the gravitational forces of two large bodies and the centrifugal force balance. The James Webb Space Telescope orbits around which Lagrange point?",
        correct="L2 — located about 1.5 million km from Earth, opposite the Sun, providing a stable thermal environment for observations",
        distractors=[
            "L1 — between Earth and the Sun",
            "L4 — 60° ahead of Earth in its orbit",
            "L3 — on the opposite side of the Sun from Earth"
        ]
    ),
    tf(
        id="orb_013", topic="kepler",
        question="Kepler's laws were derived empirically from planetary observations. Newton later showed they follow from his law of universal gravitation.",
        correct=True
    ),
    create_mc_question(
        id="orb_014", topic="hohmann",
        question="A Hohmann transfer orbit is used to move a satellite from one circular orbit to another. How does it work?",
        correct="Two engine burns: the first raises one side of the orbit to an ellipse touching the target orbit, the second circularizes the orbit at the new altitude — it is the most fuel-efficient two-impulse transfer",
        distractors=[
            "A single continuous burn that gradually spirals outward",
            "Three burns at 120° intervals around the orbit",
            "A gravitational slingshot using the Moon"
        ]
    ),
]

# ============================================================
# TOPIC: numerical_integration (L08) — 17 questions
# ============================================================
numerical_integration = [
    create_mc_question(
        id="numint_001", topic="motivation",
        question="Satellite orbits are determined by numerically integrating the equation of motion $\\ddot{\\mathbf{r}} = \\mathbf{f}(\\mathbf{r}, \\dot{\\mathbf{r}}, t)$. Why is numerical integration necessary instead of analytical solutions?",
        correct="The actual forces on a satellite (non-spherical gravity, atmospheric drag, solar radiation pressure, third-body effects) make the equation of motion too complex for closed-form analytical solutions",
        distractors=[
            "Computers are faster than analytical calculations",
            "Kepler's laws provide exact solutions that numerical methods verify",
            "Analytical solutions exist but are classified for military reasons"
        ]
    ),
    create_mc_question(
        id="numint_002", topic="euler",
        question="The Euler method is the simplest numerical integration scheme. Given the ODE $y' = f(t, y)$, it approximates the next value as $y_{n+1} = y_n + h \\cdot f(t_n, y_n)$. What is the geometric interpretation?",
        correct="It follows the tangent line at the current point for one step of size $h$ — the slope at the current point is used to extrapolate the next value",
        distractors=[
            "It uses the average slope between two points",
            "It fits a parabola through three consecutive points",
            "It uses the slope at the midpoint of the interval"
        ]
    ),
    create_mc_question(
        id="numint_003", topic="euler_error",
        question="The Euler method has a significant weakness that causes error accumulation. What is it?",
        correct="It uses only the slope at the beginning of each interval — the true function may curve away from this tangent line, and the error accumulates with each step, especially for large step sizes",
        distractors=[
            "It requires the second derivative, which is often unavailable",
            "It can only handle linear differential equations",
            "It always diverges regardless of step size"
        ]
    ),
    create_mc_question(
        id="numint_004", topic="rk4",
        question="The classical 4th-order Runge-Kutta method (RK4) computes four slopes $k_1, k_2, k_3, k_4$ within each step. What is the key advantage over the Euler method?",
        correct="By sampling the slope at multiple points within the interval and taking a weighted average, RK4 achieves much higher accuracy without needing higher-order derivatives of $f$",
        distractors=[
            "RK4 uses smaller step sizes automatically",
            "RK4 requires only one function evaluation per step",
            "RK4 works only for linear systems but gives exact solutions"
        ]
    ),
    create_mc_question(
        id="numint_005", topic="rk4_slopes",
        question="In RK4, the four slopes are: $k_1 = hf(t_n, y_n)$, $k_2 = hf(t_n + h/2, y_n + k_1/2)$, $k_3 = hf(t_n + h/2, y_n + k_2/2)$, $k_4 = hf(t_n + h, y_n + k_3)$. The increment function combines them as:",
        correct="$\\Phi = \\frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)$ — a weighted average giving double weight to the two midpoint slopes",
        distractors=[
            "$\\Phi = (k_1 + k_2 + k_3 + k_4)/4$ — a simple average",
            "$\\Phi = k_4$ — only the final slope is used",
            "$\\Phi = (k_1 + k_4)/2$ — average of first and last slopes"
        ]
    ),
    create_mc_question(
        id="numint_006", topic="rk4_properties",
        question="RK4 is a 4th-order method. What does '4th order' mean for the local truncation error?",
        correct="The local error per step is proportional to $h^5$ (where $h$ is the step size), making the global error proportional to $h^4$ — halving the step size reduces the error by a factor of 16",
        distractors=[
            "The method uses exactly 4 function evaluations per step",
            "The method works for 4th-degree polynomial functions only",
            "The error is proportional to $h^2$"
        ]
    ),
    create_mc_question(
        id="numint_007", topic="rk_advantage",
        question="A key advantage of Runge-Kutta methods over Taylor series methods for integrating orbits is:",
        correct="They avoid computing higher-order derivatives of the force function $f$ — instead, they sample $f$ at multiple points within the interval, which is much simpler to implement",
        distractors=[
            "They require no function evaluations at all",
            "They provide exact solutions for all problems",
            "They are the only methods that work for nonlinear equations"
        ]
    ),
    create_mc_question(
        id="numint_008", topic="multistep",
        question="Multistep methods (like Adams-Bashforth/Moulton) differ fundamentally from single-step methods like RK4. How?",
        correct="They use information from multiple previous steps (previously computed values of $y$ and $f$) to predict the next value, rather than using only the current point",
        distractors=[
            "They use multiple step sizes simultaneously",
            "They compute the solution at multiple future points in one step",
            "They require the analytical solution as a starting point"
        ]
    ),
    create_mc_question(
        id="numint_009", topic="predictor_corrector",
        question="A predictor-corrector method for numerical integration works by:",
        correct="First predicting the next value using an explicit formula (predictor), then refining it using an implicit formula that uses the predicted value to compute a corrected result (corrector)",
        distractors=[
            "Using two different step sizes and averaging the results",
            "Predicting the error and correcting the step size",
            "Running the integration forward and backward and comparing"
        ]
    ),
    create_mc_question(
        id="numint_010", topic="step_size",
        question="In numerical orbit integration, the choice of step size $h$ involves a tradeoff. What is it?",
        correct="Smaller $h$ gives higher accuracy but requires more computation steps (and accumulates more rounding errors); larger $h$ is faster but introduces larger truncation errors",
        distractors=[
            "Step size has no effect on accuracy — only the method order matters",
            "Smaller $h$ is always better with no downsides",
            "The step size must be exactly 1 second for satellite orbits"
        ]
    ),
    create_mc_question(
        id="numint_011", topic="applications",
        question="Numerical orbit integration is fundamental to satellite geodesy. Which of the following is NOT a direct application?",
        correct="Determining the shape of continents from topographic surveys",
        distractors=[
            "Computing precise satellite ephemerides for GNSS",
            "Gravity field determination from satellite tracking data",
            "Orbit determination for SLR target satellites"
        ]
    ),
    create_mc_question(
        id="numint_012", topic="taylor_concept",
        question="A Taylor polynomial approximates a function near a point using its derivatives. The $n$-th order Taylor polynomial of $f(x)$ around $x_0$ is $f(x) \\approx \\sum_{k=0}^{n} \\frac{f^{(k)}(x_0)}{k!}(x - x_0)^k$. What determines the quality of this approximation?",
        correct="The order $n$ and the distance from $x_0$ — higher order and closer to $x_0$ give better approximations; the error is bounded by the $(n+1)$-th derivative term",
        distractors=[
            "Only the value of $f$ at $x_0$ matters",
            "The approximation is exact for all functions regardless of $n$",
            "The quality depends only on the step size, not the order"
        ]
    ),
    tf(
        id="numint_013", topic="euler",
        question="The Euler method is a first-order method — its global error is proportional to the step size $h$.",
        correct=True
    ),
    create_mc_question(
        id="numint_014", topic="orbit_integration_ivp",
        question="Orbit integration is an initial value problem (IVP). What initial conditions are needed to integrate a satellite's trajectory?",
        correct="The satellite's position vector $\\mathbf{r}(t_0)$ and velocity vector $\\dot{\\mathbf{r}}(t_0)$ at the initial epoch $t_0$ — six values defining the state in 3D",
        distractors=[
            "Only the satellite's position at two different times",
            "The satellite's mass and the gravitational constant",
            "The six Keplerian orbital elements and their rates of change"
        ]
    ),
    create_mc_question(
        id="numint_015", topic="rk_vs_multistep",
        question="Runge-Kutta methods are self-starting, while multistep methods are not. What does this mean?",
        correct="RK methods can start from a single initial point, while multistep methods need several previous solution values — these must first be computed by another method (like RK) before multistep integration can begin",
        distractors=[
            "RK methods initialize themselves from the boundary conditions",
            "Multistep methods require no initial conditions at all",
            "Self-starting means the method can determine its own step size"
        ]
    ),
    create_mc_question(
        id="numint_016", topic="orbit_interpolation",
        question="After integrating a satellite orbit at discrete time steps, orbit interpolation is needed to obtain positions at arbitrary times. What method is commonly used?",
        correct="Polynomial interpolation (e.g., Lagrange or Chebyshev polynomials) through nearby computed orbit points",
        distractors=[
            "Linear interpolation between consecutive points only",
            "Re-running the numerical integration for each desired time",
            "Using Kepler's equation directly without the numerical integration results"
        ]
    ),
    create_mc_question(
        id="numint_017", topic="tangent_vs_secant",
        question="In the context of numerical integration, the Euler method uses a tangent approximation. What does the Runge-Kutta approach use instead?",
        correct="A secant-like approximation — by sampling the slope at multiple points within the interval, it effectively computes an average slope that better approximates the curve than the single tangent at the start",
        distractors=[
            "A parabolic approximation that requires second derivatives",
            "An exact analytical solution within each interval",
            "A tangent at the endpoint instead of the start"
        ]
    ),
]

# ============================================================
# TOPIC: spherical_harmonics (L09) — 19 questions
# ============================================================
spherical_harmonics = [
    create_mc_question(
        id="sh_001", topic="gravitational_potential",
        question="The gravitational potential $V$ of a point mass $M$ at distance $r$ is $V = GM/r$. Why is the potential (a scalar) used instead of the gravitational acceleration (a vector) in geodesy?",
        correct="The potential is a scalar field that is easier to work with mathematically — the acceleration can be derived from it as the gradient: $\\mathbf{g} = \\text{grad}(V)$",
        distractors=[
            "The potential can be measured directly by satellite sensors",
            "The acceleration is always constant and carries no information",
            "The potential is used only for visualization purposes"
        ]
    ),
    create_mc_question(
        id="sh_002", topic="inhomogeneous_earth",
        question="The Earth is not a homogeneous sphere. Why does this matter for satellite orbits?",
        correct="An inhomogeneous mass distribution creates a non-spherical gravity field with variations that perturb satellite orbits from perfect Keplerian ellipses — these perturbations contain information about the Earth's internal mass distribution",
        distractors=[
            "Only homogeneous bodies can have satellites",
            "Inhomogeneity makes the escape velocity undefined",
            "The orbital period does not depend on the gravity field"
        ]
    ),
    create_mc_question(
        id="sh_003", topic="geoid",
        question="The geoid is a fundamental concept in geodesy. How is it defined?",
        correct="The equipotential surface of the Earth's gravity field that coincides with mean sea level in the open ocean — gravity vectors are everywhere perpendicular to it",
        distractors=[
            "The surface of the best-fitting reference ellipsoid",
            "The physical topographic surface of the Earth",
            "A sphere with the Earth's average radius"
        ]
    ),
    create_mc_question(
        id="sh_004", topic="geoid_vs_ellipsoid",
        question="The geoid and the reference ellipsoid are different surfaces. What is the geoid height (or geoid undulation)?",
        correct="The separation between the geoid and the reference ellipsoid — it varies globally by up to about $\\pm$100 meters",
        distractors=[
            "The height of the ocean surface above the sea floor",
            "The altitude of a satellite above the ellipsoid",
            "The difference between geodetic latitude and geocentric latitude"
        ]
    ),
    create_mc_question(
        id="sh_005", topic="sh_expansion",
        question="Spherical harmonics are used to represent the gravitational potential on a sphere. The potential is expanded as $V(r,\\vartheta,\\lambda) = \\frac{GM}{r}\\sum_{n=0}^{\\infty}\\sum_{m=0}^{n}\\left(\\frac{a}{r}\\right)^n (C_{nm}\\cos m\\lambda + S_{nm}\\sin m\\lambda)P_{nm}(\\cos\\vartheta)$. What are $C_{nm}$ and $S_{nm}$?",
        correct="Spherical harmonic coefficients (Stokes coefficients) — they quantify the contribution of each harmonic degree $n$ and order $m$ to the gravity field",
        distractors=[
            "The Cartesian coordinates of mass anomalies",
            "The eigenvalues of the gravitational potential matrix",
            "The phase and amplitude of tidal waves"
        ]
    ),
    create_mc_question(
        id="sh_006", topic="degree_order",
        question="In spherical harmonics, the degree $n$ and order $m$ have specific physical interpretations. Higher degree $n$ corresponds to:",
        correct="Finer spatial resolution — higher degrees capture smaller-scale features of the gravity field",
        distractors=[
            "Larger-scale features of the gravity field",
            "Higher temporal frequencies of gravity changes",
            "Greater orbital altitudes for satellite observations"
        ]
    ),
    create_mc_question(
        id="sh_007", topic="c20",
        question="The spherical harmonic coefficient $C_{20}$ is by far the largest coefficient (about $-4.84 \\times 10^{-4}$), roughly 1000 times larger than other coefficients. What does it describe?",
        correct="The Earth's oblateness (flattening) — the equatorial bulge caused by Earth's rotation",
        distractors=[
            "The total mass of the Earth",
            "The location of the center of mass",
            "The Earth's tidal deformation"
        ]
    ),
    create_mc_question(
        id="sh_008", topic="geocenter",
        question="The degree-1 spherical harmonic coefficients ($C_{10}$, $C_{11}$, $S_{11}$) are set to zero in the gravity field model. What does this enforce?",
        correct="The center of mass of the Earth system coincides with the coordinate origin — these coefficients describe the displacement of the center of mass from the origin",
        distractors=[
            "The gravity field has no tidal component",
            "The geoid is symmetric about the equator",
            "The Earth's rotation rate is constant"
        ]
    ),
    create_mc_question(
        id="sh_009", topic="basis_functions",
        question="For each degree $n$, how many independent spherical harmonic basis functions exist?",
        correct="$2n + 1$ — for example, degree 2 has 5 basis functions ($m = 0, 1, 2$ with cosine and sine terms for $m > 0$)",
        distractors=[
            "$n^2$ basis functions",
            "$n + 1$ basis functions",
            "Exactly 3 basis functions for all degrees"
        ]
    ),
    create_mc_question(
        id="sh_010", topic="laplace",
        question="Spherical harmonics arise as solutions to the Laplace equation $\\nabla^2 V = 0$. What does this equation describe physically?",
        correct="A potential field in source-free (empty) space — the gravitational potential outside the Earth satisfies the Laplace equation because there are no masses in the space above the surface",
        distractors=[
            "The distribution of mass inside the Earth",
            "The equation of motion for a satellite",
            "The wave equation for electromagnetic radiation"
        ]
    ),
    create_mc_question(
        id="sh_011", topic="homogeneous_polynomials",
        question="Homogeneous polynomials have the scaling property $H_n(\\lambda x, \\lambda y, \\lambda z) = \\lambda^n H_n(x, y, z)$. Why are they important in the context of spherical harmonics?",
        correct="Homogeneous harmonic polynomials (those satisfying both homogeneity and the Laplace equation) restricted to the unit sphere form the spherical harmonics — they provide a complete orthogonal basis for functions on the sphere",
        distractors=[
            "They simplify the computation of satellite positions",
            "They are the only polynomials that can represent ellipsoidal surfaces",
            "They eliminate the need for numerical integration"
        ]
    ),
    create_mc_question(
        id="sh_012", topic="resolution",
        question="The WGS84 geoid model (EGM96) uses spherical harmonics up to degree 360. What spatial resolution does this correspond to?",
        correct="Approximately 100 km at the equator — the resolution is roughly $20000/n$ km, where $n$ is the maximum degree",
        distractors=[
            "Approximately 1 km at the equator",
            "Approximately 1000 km at the equator",
            "The resolution is independent of the maximum degree"
        ]
    ),
    tf(
        id="sh_013", topic="gravity_field",
        question="The Earth's gravity field is the largest force acting on low-orbiting satellites.",
        correct=True
    ),
    create_mc_question(
        id="sh_014", topic="gravity_surface",
        question="At the Earth's surface, spherical harmonics are used for height system definition. How is height defined in a physically meaningful way?",
        correct="Using equipotential surfaces of the gravity field — height is defined relative to the geoid, which is the equipotential surface at mean sea level",
        distractors=[
            "Height is always defined as distance from the ellipsoid surface",
            "Height is defined as the radial distance from the center of mass",
            "Height is defined using barometric pressure measurements only"
        ]
    ),
    create_mc_question(
        id="sh_015", topic="potential_units",
        question="The gravitational potential $V = GM/r$ has SI units of:",
        correct="$\\text{m}^2/\\text{s}^2$ (or equivalently J/kg) — it is energy per unit mass",
        distractors=[
            "$\\text{m/s}^2$ (that is acceleration, not potential)",
            "Newtons (that is force, not potential)",
            "Dimensionless (no units)"
        ]
    ),
    create_mc_question(
        id="sh_016", topic="zonal_tesseral_sectorial",
        question="Spherical harmonics of degree $n$ and order $m$ are classified by the pattern of their nodal lines. Zonal harmonics ($m = 0$) have:",
        correct="Nodal lines that are parallels of latitude only — they depend only on co-latitude $\\vartheta$, creating bands (zones) around the sphere",
        distractors=[
            "Nodal lines that are meridians only",
            "A checkerboard pattern of nodal lines",
            "No nodal lines at all"
        ]
    ),
    create_mc_question(
        id="sh_017", topic="associated_legendre",
        question="The latitude-dependent part of spherical harmonics is described by associated Legendre functions $P_{nm}(\\cos\\vartheta)$. What is the role of these functions?",
        correct="They provide an orthogonal basis for functions on the sphere in the co-latitude direction, complementing the trigonometric functions ($\\cos m\\lambda$, $\\sin m\\lambda$) in the longitude direction",
        distractors=[
            "They convert between Cartesian and spherical coordinates",
            "They compute the orbital elements of satellites",
            "They model the temporal variations of the gravity field"
        ]
    ),
    tf(
        id="sh_018", topic="completeness",
        question="Spherical harmonics form a complete orthogonal basis on the sphere — any square-integrable function on the sphere can be represented as a series of spherical harmonics.",
        correct=True
    ),
    create_mc_question(
        id="sh_019", topic="satellite_applications",
        question="In outer space, the gravitational potential and its derivatives are needed for:",
        correct="Satellite orbit computation — the forces on the satellite are derived from the gradient of the potential, determining the satellite's trajectory",
        distractors=[
            "Measuring atmospheric temperature profiles",
            "Calibrating satellite cameras",
            "Determining the color of celestial objects"
        ]
    ),
]

# ============================================================
# TOPIC: slr_prare_doris (L10) — 16 questions
# ============================================================
slr_prare_doris = [
    create_mc_question(
        id="slr_001", topic="slr_principle",
        question="Satellite Laser Ranging (SLR) measures the distance to a satellite by:",
        correct="Sending a short laser pulse from a ground station to retroreflectors on the satellite and measuring the round-trip time of flight — distance equals $c \\cdot \\Delta t / 2$",
        distractors=[
            "Measuring the Doppler shift of a reflected laser beam",
            "Counting interference fringes between two laser beams",
            "Measuring the intensity attenuation of the reflected laser"
        ]
    ),
    create_mc_question(
        id="slr_002", topic="slr_accuracy",
        question="The accuracy of SLR depends primarily on three factors. Which of the following is one of them?",
        correct="The duration (temporal width) of the laser pulse — shorter pulses allow more precise time-of-flight measurements",
        distractors=[
            "The color (wavelength) of the laser, which must be infrared",
            "The mass of the satellite, which affects the reflection efficiency",
            "The rotation rate of the satellite"
        ]
    ),
    create_mc_question(
        id="slr_003", topic="retroreflectors",
        question="SLR satellites carry retroreflectors (corner cubes). What special property do retroreflectors have?",
        correct="They reflect incoming light exactly back toward its source regardless of the angle of incidence — this ensures the laser pulse returns to the ground station",
        distractors=[
            "They amplify the laser signal for better detection",
            "They convert the laser to a different wavelength for atmospheric correction",
            "They scatter light uniformly in all directions"
        ]
    ),
    create_mc_question(
        id="slr_004", topic="lageos",
        question="LAGEOS (Laser Geodynamics Satellite) is a dedicated geodetic satellite used for SLR. What makes it ideal for precise geodetic measurements?",
        correct="It is a dense, compact sphere covered with retroreflectors with minimal surface area-to-mass ratio, minimizing non-gravitational perturbations (atmospheric drag, radiation pressure)",
        distractors=[
            "It has an active propulsion system to maintain its orbit precisely",
            "It transmits its own positioning signals like a GNSS satellite",
            "It orbits in geostationary orbit for continuous visibility"
        ]
    ),
    create_mc_question(
        id="slr_005", topic="slr_model",
        question="The SLR observation model includes corrections for satellite center of mass ($d_{\\text{sat}}$), station reference point ($d^0$), detector-specific delays ($d^d$), and atmospheric corrections ($d^a$). Why are these corrections necessary?",
        correct="The measurement is from the station detector to the satellite retroreflector array — corrections are needed to relate this to the geometric distance between the station reference point and the satellite center of mass",
        distractors=[
            "SLR measurements are inherently biased toward shorter distances",
            "The laser beam changes wavelength as it travels through space",
            "Retroreflectors introduce a frequency-dependent delay"
        ]
    ),
    create_mc_question(
        id="slr_006", topic="llr",
        question="Lunar Laser Ranging (LLR) measures the Earth-Moon distance using retroreflectors placed on the Moon. What has LLR revealed about the Earth-Moon system?",
        correct="The Moon is receding from Earth at about 3.82 cm/year due to tidal friction — LLR also provides precise lunar ephemerides and contributes to determining all five EOP",
        distractors=[
            "The Moon is moving closer to Earth at 3.82 cm/year",
            "The Moon's rotation rate is increasing",
            "The Moon has no measurable distance change"
        ]
    ),
    create_mc_question(
        id="slr_007", topic="prare",
        question="PRARE (Precise Range and Range Rate Equipment) was a microwave tracking system. What two quantities did it measure?",
        correct="The range (distance) and the range rate (rate of change of distance, i.e., radial velocity via Doppler shift) between a satellite and ground stations",
        distractors=[
            "The azimuth and elevation angles to the satellite",
            "The temperature and pressure of the atmosphere",
            "The satellite's attitude and spin rate"
        ]
    ),
    create_mc_question(
        id="slr_008", topic="doris",
        question="DORIS (Doppler Orbitography and Radiopositioning Integrated by Satellite) differs from GNSS in a fundamental way. What is it?",
        correct="In DORIS, the ground beacons transmit signals and the satellite receives them (uplink system) — the inverse of GNSS where satellites transmit and ground receivers listen",
        distractors=[
            "DORIS uses laser signals instead of radio waves",
            "DORIS works only over the oceans",
            "DORIS requires an atomic clock at every ground station"
        ]
    ),
    create_mc_question(
        id="slr_009", topic="non_gravitational",
        question="Non-gravitational forces perturb satellite orbits and must be modeled. Which of the following is a non-gravitational perturbation?",
        correct="Solar radiation pressure — photons from the Sun impart momentum to the satellite's surface, pushing it away from the Sun",
        distractors=[
            "The gravitational attraction of the Moon",
            "The $J_2$ effect of Earth's oblateness",
            "Tidal deformation of the solid Earth"
        ]
    ),
    create_mc_question(
        id="slr_010", topic="non_gravitational",
        question="Atmospheric drag is a significant perturbation for LEO satellites. What determines the magnitude of the drag force?",
        correct="The atmospheric density at the satellite's altitude, the satellite's velocity relative to the atmosphere, its cross-sectional area, and the drag coefficient",
        distractors=[
            "Only the satellite's mass and altitude",
            "The gravitational constant and the Earth's rotation rate",
            "The satellite's surface color and reflectivity"
        ]
    ),
    create_mc_question(
        id="slr_011", topic="tracking_purpose",
        question="Why are tracking systems (SLR, GNSS, DORIS) needed for satellites in addition to the initial orbit determination?",
        correct="Satellite orbits are continuously perturbed by gravitational and non-gravitational forces — tracking provides the measurements needed to update and refine the orbit, and the orbit residuals contain valuable geophysical information",
        distractors=[
            "Satellites lose power over time and need tracking for recharging",
            "Tracking is only needed for communication, not for science",
            "The initial orbit determination is always sufficient for the satellite's lifetime"
        ]
    ),
    create_mc_question(
        id="slr_012", topic="tropospheric_correction",
        question="SLR measurements require a tropospheric correction. How is the tropospheric delay for laser signals modeled?",
        correct="Using atmospheric models based on local temperature, pressure, and humidity measurements — the delay is smaller for laser (optical) signals than for radio (microwave) signals used by GNSS",
        distractors=[
            "No correction is needed because laser light is unaffected by the atmosphere",
            "By measuring the delay at two different laser wavelengths",
            "By comparing with simultaneous GNSS measurements only"
        ]
    ),
    tf(
        id="slr_013", topic="slr_ionosphere",
        question="Unlike GNSS radio signals, SLR laser signals are not significantly affected by the ionosphere.",
        correct=True  # Optical frequencies are too high to be affected by ionospheric free electrons
    ),
    create_mc_question(
        id="slr_014", topic="slr_products",
        question="SLR contributes to several geodetic products. Which is a unique strength of SLR compared to other techniques?",
        correct="Determination of the geocenter (Earth's center of mass) and the absolute scale of the terrestrial reference frame — SLR is the primary technique for defining the origin and scale of the ITRF",
        distractors=[
            "SLR is the only technique that can determine polar motion",
            "SLR provides the most precise satellite clock corrections",
            "SLR determines the orientation of the celestial reference frame"
        ]
    ),
    create_mc_question(
        id="slr_015", topic="doris_products",
        question="DORIS contributes to precise orbit determination for altimetry satellites (like Jason). Why is precise orbit determination critical for altimetry?",
        correct="Altimetry measures the distance from the satellite to the sea surface — to convert this to absolute sea surface height, the satellite's altitude above the reference ellipsoid must be known with centimeter-level precision",
        distractors=[
            "DORIS corrects the altimeter's radar frequency",
            "DORIS provides the ocean temperature data",
            "Precise orbit determination is only needed for communication satellites"
        ]
    ),
    create_mc_question(
        id="slr_016", topic="yarkovsky",
        question="The Yarkovsky effect is a non-gravitational perturbation caused by:",
        correct="Thermal emission from the satellite — the satellite absorbs solar radiation, heats up, and re-radiates infrared photons, creating a small but measurable thrust",
        distractors=[
            "The gravitational attraction of distant stars",
            "Magnetic interaction with Earth's magnetic field",
            "Aerodynamic lift in the upper atmosphere"
        ]
    ),
]

# ============================================================
# TOPIC: vlbi (L11) — 6 questions
# ============================================================
vlbi = [
    create_mc_question(
        id="vlbi_001", topic="principle",
        question="VLBI (Very Long Baseline Interferometry) determines the time delay $\\tau$ of a radio wavefront arriving at two widely separated antennas observing the same quasar. The delay is $\\tau = \\frac{\\mathbf{b} \\cdot \\mathbf{k}}{c}$. What are $\\mathbf{b}$ and $\\mathbf{k}$?",
        correct="$\\mathbf{b}$ is the baseline vector between the two antennas; $\\mathbf{k}$ is the unit vector toward the quasar (radio source direction)",
        distractors=[
            "$\\mathbf{b}$ is the velocity of the antennas; $\\mathbf{k}$ is the frequency of the signal",
            "$\\mathbf{b}$ is the orbital vector of the Earth; $\\mathbf{k}$ is the gravitational force direction",
            "$\\mathbf{b}$ is the signal amplitude; $\\mathbf{k}$ is the wavelength"
        ]
    ),
    create_mc_question(
        id="vlbi_002", topic="unique_strength",
        question="VLBI has a unique capability among all space geodetic techniques. What is it?",
        correct="It directly realizes the celestial reference frame (ICRF) by observing quasars, and it is the only technique that can determine all five Earth Orientation Parameters",
        distractors=[
            "It achieves the highest ranging accuracy to satellites",
            "It provides real-time positioning for moving platforms",
            "It determines the gravity field of the Earth"
        ]
    ),
    create_mc_question(
        id="vlbi_003", topic="ut1",
        question="VLBI is the only technique that can directly determine UT1 (Universal Time 1), which is related to the Earth Rotation Angle. Why can't satellite techniques determine UT1?",
        correct="UT1 is correlated with the longitude of the ascending node ($\\Omega$) of satellite orbits — satellite-based techniques cannot separate Earth rotation from orbital precession",
        distractors=[
            "Satellites do not carry atomic clocks",
            "Satellite signals are blocked by the ionosphere",
            "Satellites are too close to Earth to observe the rotation"
        ]
    ),
    create_mc_question(
        id="vlbi_004", topic="baseline",
        question="VLBI measures baseline lengths between stations with sub-millimeter precision. What geophysical phenomenon can be directly observed from changes in baseline lengths over time?",
        correct="Tectonic plate motion — VLBI baselines crossing plate boundaries show measurable length changes of millimeters to centimeters per year",
        distractors=[
            "Changes in atmospheric temperature",
            "Variations in ocean salinity",
            "Fluctuations in the solar wind"
        ]
    ),
    tf(
        id="vlbi_005", topic="e_vlbi",
        question="Modern e-VLBI (electronic VLBI) transmits data in real time over fiber-optic networks, enabling rapid processing — this has replaced the earlier practice of shipping recorded data tapes to a correlator.",
        correct=True
    ),
    create_mc_question(
        id="vlbi_006", topic="ivs",
        question="The International VLBI Service (IVS) coordinates global VLBI observations. What is the primary operational challenge of VLBI compared to GNSS?",
        correct="VLBI requires large, expensive radio telescopes at fixed stations and coordinated observation sessions — it cannot provide continuous, real-time global coverage like GNSS",
        distractors=[
            "VLBI signals are absorbed by the atmosphere",
            "VLBI can only observe objects within the solar system",
            "VLBI accuracy is limited to meters"
        ]
    ),
]

# ============================================================
# TOPIC: ggos (L12) — 5 questions
# ============================================================
ggos = [
    create_mc_question(
        id="ggos_001", topic="ggos_mission",
        question="The Global Geodetic Observing System (GGOS) integrates multiple space-geodetic techniques. What is its mission?",
        correct="To provide the geodetic infrastructure (reference frames, Earth rotation, gravity field) necessary for monitoring the Earth system and global change with the highest precision",
        distractors=[
            "To operate a single global navigation system",
            "To replace all existing space agencies",
            "To provide weather forecasting services"
        ]
    ),
    create_mc_question(
        id="ggos_002", topic="accuracy_requirements",
        question="GGOS aims for reference frame accuracy of 1 mm with stability of 0.1 mm/year. Why is such extreme precision needed?",
        correct="To detect small but important signals of global change — sea level rise of ~3 mm/year, post-glacial rebound, tectonic deformation — require a reference frame more accurate than the signals being measured",
        distractors=[
            "To improve GPS navigation accuracy for consumer devices",
            "To detect gravitational waves from black holes",
            "To measure the expansion of the universe"
        ]
    ),
    create_mc_question(
        id="ggos_003", topic="technique_combination",
        question="GGOS combines data from VLBI, SLR, GNSS, and DORIS. Why is a combination of techniques necessary rather than relying on a single technique?",
        correct="Each technique has unique strengths and weaknesses — VLBI provides orientation and UT1, SLR provides the scale and geocenter, GNSS provides dense spatial coverage, DORIS provides precise orbits for altimetry. Together they overcome individual limitations",
        distractors=[
            "A single technique would be sufficient but is too expensive",
            "Different countries prefer different techniques, so all must be included for political reasons",
            "The techniques are identical in capability but use different hardware"
        ]
    ),
    create_mc_question(
        id="ggos_004", topic="iers",
        question="The International Earth Rotation and Reference Systems Service (IERS) is responsible for:",
        correct="Maintaining and distributing the International Terrestrial Reference Frame (ITRF), the International Celestial Reference Frame (ICRF), and Earth Orientation Parameters (EOP)",
        distractors=[
            "Operating GNSS satellites and broadcasting navigation messages",
            "Launching geodetic satellites for SLR",
            "Manufacturing and calibrating VLBI antennas"
        ]
    ),
    tf(
        id="ggos_005", topic="co_location",
        question="Co-location sites — where multiple space-geodetic techniques (VLBI, SLR, GNSS, DORIS) operate at the same physical location — are critical for tying the different technique solutions together into a consistent global reference frame.",
        correct=True
    ),
]

# ============================================================
# TOPIC: altimetry (L13) — 15 questions
# ============================================================
altimetry = [
    create_mc_question(
        id="alt_001", topic="principle",
        question="Satellite altimetry measures the distance from a satellite to the ocean surface using a radar pulse. The sea surface height (SSH) above the reference ellipsoid is calculated as:",
        correct="SSH = satellite altitude above ellipsoid minus the measured range from satellite to sea surface",
        distractors=[
            "SSH = measured range plus satellite altitude",
            "SSH = satellite altitude divided by the measured range",
            "SSH = measured range minus the geoid height"
        ]
    ),
    create_mc_question(
        id="alt_002", topic="tide_gauges",
        question="Before satellite altimetry, mean sea level was determined using tide gauges. What is a key limitation of tide gauges?",
        correct="They measure relative sea level at discrete coastal points — they cannot distinguish whether the sea surface is rising or the land is sinking (vertical land motion problem)",
        distractors=[
            "Tide gauges can only measure waves, not sea level",
            "Tide gauges are only available in the Northern Hemisphere",
            "Tide gauges measure absolute sea level with global coverage"
        ]
    ),
    create_mc_question(
        id="alt_003", topic="waveform",
        question="The altimeter receives a reflected radar pulse whose shape (waveform) contains information. A leading-edge ramp in the waveform corresponds to:",
        correct="The time interval during which the radar pulse expands from the nadir point outward over the sea surface — the slope of this ramp is related to significant wave height",
        distractors=[
            "The atmospheric absorption of the radar signal",
            "The satellite's orbital velocity",
            "The ionospheric delay of the signal"
        ]
    ),
    create_mc_question(
        id="alt_004", topic="wave_height",
        question="Significant Wave Height (SWH) is derived from the altimeter waveform. Rougher seas (higher waves) cause:",
        correct="A more stretched (broader) leading-edge ramp — the pulse reaches wave crests earlier and wave troughs later, spreading out the return signal in time",
        distractors=[
            "A sharper, narrower waveform peak",
            "A stronger signal return but with the same shape",
            "No change in the waveform shape"
        ]
    ),
    create_mc_question(
        id="alt_005", topic="orbit_choice",
        question="The orbit configuration for altimetry satellites involves a tradeoff between temporal and spatial resolution. A satellite with a longer repeat cycle:",
        correct="Has denser ground track spacing (better spatial coverage) but revisits the same location less frequently",
        distractors=[
            "Has both better spatial and temporal coverage",
            "Orbits at lower altitude for better accuracy",
            "Cannot measure sea surface topography"
        ]
    ),
    create_mc_question(
        id="alt_006", topic="mssh",
        question="The Mean Sea Surface Height (MSSH) is composed of two main components:",
        correct="The geoid height (the dominant component, reflecting the gravity field) plus the Mean Dynamic Topography (MDT, reflecting permanent ocean currents)",
        distractors=[
            "The ellipsoid height plus the atmospheric pressure effect",
            "Tidal oscillations plus wave-induced setup",
            "The topographic height of the ocean floor"
        ]
    ),
    create_mc_question(
        id="alt_007", topic="dynamic_topography",
        question="The Mean Dynamic Topography (MDT) is the difference between MSSH and the geoid. What does it represent physically?",
        correct="The permanent deviation of the sea surface from the geoid caused by ocean currents, temperature, and salinity differences — it is used to derive geostrophic ocean currents",
        distractors=[
            "The tidal variation of sea level",
            "The wind-driven wave height",
            "The atmospheric pressure at the sea surface"
        ]
    ),
    create_mc_question(
        id="alt_008", topic="geostrophic_currents",
        question="Geostrophic ocean currents are derived from altimetry data. The relationship between sea surface slope and current velocity relies on:",
        correct="A balance between the pressure gradient force (due to the sea surface slope) and the Coriolis force (due to Earth's rotation) — the current flows perpendicular to the slope",
        distractors=[
            "The temperature difference between the surface and the deep ocean",
            "The friction between the wind and the ocean surface",
            "The gravitational attraction of the Moon"
        ]
    ),
    create_mc_question(
        id="alt_009", topic="topex_poseidon",
        question="The TOPEX/Poseidon mission (1992–2006) was a pioneering altimetry satellite. What was its key contribution?",
        correct="It provided the first continuous, high-accuracy global measurements of sea surface height, enabling the study of ocean circulation, sea level rise, and El Niño events",
        distractors=[
            "It was the first satellite to orbit the Moon",
            "It discovered the Van Allen radiation belts",
            "It provided the first images of the Earth from space"
        ]
    ),
    create_mc_question(
        id="alt_010", topic="cryosat",
        question="CryoSat (ESA) uses Synthetic Aperture Radar (SAR) altimetry. What advantages does SAR altimetry offer over conventional pulse-limited altimetry?",
        correct="Higher along-track resolution (about 250 m vs. several km) by coherently processing multiple successive radar echoes — important for measuring sea ice and ice sheet edges",
        distractors=[
            "SAR altimetry works in visible light instead of radar",
            "SAR altimetry has unlimited swath width",
            "SAR altimetry requires no orbit determination"
        ]
    ),
    create_mc_question(
        id="alt_011", topic="multi_mission",
        question="Multi-mission altimetry combines data from several satellites operating simultaneously. Why is this important?",
        correct="Individual satellites have gaps in spatial and temporal coverage — combining multiple satellites with different orbit configurations provides more complete sampling of ocean variability",
        distractors=[
            "A single satellite provides sufficient global coverage",
            "Multiple satellites are needed because each measures a different ocean property",
            "Multi-mission data is only used for calibration, not science"
        ]
    ),
    create_mc_question(
        id="alt_012", topic="sea_level_rise",
        question="Satellite altimetry has measured global mean sea level rise of approximately 3 mm/year since the 1990s. This rate is:",
        correct="Accelerating — recent decades show a faster rate than the long-term average from tide gauges (about 1.5 mm/year over the 20th century)",
        distractors=[
            "Constant and unchanged over the past century",
            "Decelerating — the rate is slowing down",
            "Too small to be detected by current instruments"
        ]
    ),
    tf(
        id="alt_013", topic="ocean_vs_land",
        question="Altimetry waveforms over land and ice are much more complex and variable than over the open ocean, because the reflecting surface is rougher and more heterogeneous.",
        correct=True
    ),
    create_mc_question(
        id="alt_014", topic="corrections",
        question="Altimetry measurements require several corrections. Which correction accounts for the slowing of the radar signal as it passes through the troposphere?",
        correct="The wet and dry tropospheric corrections — water vapor and dry gas cause signal delays that must be subtracted from the measured range",
        distractors=[
            "The ionospheric correction — free electrons in the ionosphere",
            "The solid Earth tide correction — vertical motion of the ground",
            "The ocean tide correction — tidal height variations"
        ]
    ),
    create_mc_question(
        id="alt_015", topic="precise_orbits",
        question="For altimetry, the satellite's radial orbit error directly maps into sea surface height error. What accuracy is required for the orbit determination of altimetry satellites?",
        correct="Centimeter-level radial accuracy — achieved through precise orbit determination using GNSS, SLR, and DORIS tracking data",
        distractors=[
            "Meter-level accuracy is sufficient",
            "Only kilometer-level accuracy is needed since the ocean is large",
            "No orbit determination is needed because the satellite altitude is constant"
        ]
    ),
]

# ============================================================
# TOPIC: orbit_perturbations (L14) — 5 questions
# ============================================================
orbit_perturbations = [
    create_mc_question(
        id="perturb_001", topic="j2_effect",
        question="The $J_2$ coefficient describes the Earth's oblateness. What are the two main orbital effects of $J_2$ on a satellite?",
        correct="Regression of the ascending node ($\\dot{\\Omega}$) and rotation of the argument of perigee ($\\dot{\\omega}$) — both are secular (continuously accumulating) effects",
        distractors=[
            "Changes in the satellite's mass and surface area",
            "Periodic oscillations in the orbital eccentricity only",
            "A single impulsive change to the orbital plane"
        ]
    ),
    create_mc_question(
        id="perturb_002", topic="sun_sync_j2",
        question="Sun-synchronous orbits exploit the $J_2$-induced nodal regression. The regression rate $\\dot{\\Omega}$ depends on:",
        correct="The orbital altitude, eccentricity, and inclination — by choosing the right inclination (typically 96–99°, slightly retrograde), the node precesses at exactly 360°/year to match the Earth's orbital motion around the Sun",
        distractors=[
            "Only the satellite's mass",
            "The satellite's launch date and time",
            "The strength of the solar wind"
        ]
    ),
    create_mc_question(
        id="perturb_003", topic="drag",
        question="Atmospheric drag causes a satellite's orbit to decay. The drag force depends on $F_D = \\frac{1}{2}C_D \\rho A v^2$. How does a satellite's cross-sectional area affect drag?",
        correct="Larger cross-sectional area $A$ increases the drag force proportionally — this is why geodetic satellites like LAGEOS are compact spheres with minimal area-to-mass ratio",
        distractors=[
            "The cross-sectional area has no effect on drag",
            "Larger area reduces drag by spreading the force over more surface",
            "Cross-sectional area only matters for satellites above 2000 km"
        ]
    ),
    create_mc_question(
        id="perturb_004", topic="aerobraking",
        question="Aerobraking is a technique that deliberately uses atmospheric drag to change a satellite's orbit. How is it used in planetary missions?",
        correct="The spacecraft dips into the upper atmosphere of a planet, using drag to gradually slow down and lower its orbit — this saves fuel compared to propulsive braking",
        distractors=[
            "The spacecraft accelerates by burning fuel in the atmosphere",
            "The spacecraft uses the atmosphere to generate lift for orbital changes",
            "Aerobraking can only be used at Earth, not at other planets"
        ]
    ),
    create_mc_question(
        id="perturb_005", topic="radiation_pressure",
        question="Solar radiation pressure (SRP) is a non-gravitational perturbation that affects satellite orbits. The force depends on:",
        correct="The satellite's cross-sectional area facing the Sun, the solar flux (intensity of sunlight), and the surface reflectivity — it pushes the satellite away from the Sun",
        distractors=[
            "Only the satellite's mass and orbital altitude",
            "The satellite's magnetic properties",
            "The number of solar panels on the satellite"
        ]
    ),
]

# ============================================================
# TOPIC: gravity_missions (L15) — 12 questions
# ============================================================
gravity_missions = [
    create_mc_question(
        id="grav_001", topic="measurement_principle",
        question="The coarse principle of satellite gravity field determination is: satellite orbits are perturbed by gravity field variations. By precisely tracking the orbit and comparing with a model, what can be determined?",
        correct="The difference between the true gravity field and the model — orbit residuals contain information about unmodeled gravity field features, which are used to improve the gravity model",
        distractors=[
            "The satellite's fuel consumption",
            "The atmospheric composition at orbital altitude",
            "The Earth's magnetic field strength"
        ]
    ),
    create_mc_question(
        id="grav_002", topic="champ",
        question="CHAMP (2000–2010) was the first dedicated gravity field satellite mission. What measurement principle did it use?",
        correct="High-Low Satellite-to-Satellite Tracking (HL-SST) — continuous GPS tracking of the LEO satellite at 1 Hz provided precise orbit data, from which the gravity field was recovered",
        distractors=[
            "Low-Low SST between two co-orbiting satellites",
            "Satellite gradiometry using differential accelerometers",
            "SLR tracking from ground stations only"
        ]
    ),
    create_mc_question(
        id="grav_003", topic="champ_accelerometer",
        question="CHAMP carried a STAR accelerometer. What was its purpose?",
        correct="To measure non-gravitational accelerations (atmospheric drag, solar radiation pressure) acting on the satellite — these must be subtracted from the total acceleration to isolate the gravitational signal",
        distractors=[
            "To measure the gravitational acceleration directly",
            "To stabilize the satellite's orientation",
            "To measure the speed of the satellite"
        ]
    ),
    create_mc_question(
        id="grav_004", topic="grace",
        question="GRACE (2002–2017) used a fundamentally different measurement concept from CHAMP. What was it?",
        correct="Low-Low Satellite-to-Satellite Tracking (LL-SST) — two identical satellites flew about 220 km apart and measured their inter-satellite distance changes using a K-band microwave ranging system with micrometer precision",
        distractors=[
            "A single satellite with a gravity gradiometer",
            "Laser altimetry of the ocean surface",
            "Optical tracking by ground-based telescopes"
        ]
    ),
    create_mc_question(
        id="grav_005", topic="grace_principle",
        question="In GRACE, when the leading satellite passes over a mass anomaly (e.g., a mountain), what happens to the inter-satellite distance?",
        correct="The leading satellite is accelerated toward the mass anomaly first, increasing the inter-satellite distance — when the trailing satellite passes over it, the distance decreases again. These distance changes reveal the gravity field variations",
        distractors=[
            "Both satellites are affected simultaneously, so no distance change occurs",
            "The trailing satellite is always accelerated more than the leading one",
            "The inter-satellite distance remains constant because both are in free fall"
        ]
    ),
    create_mc_question(
        id="grav_006", topic="grace_applications",
        question="GRACE revealed time-variable gravity — changes in the gravity field over months and years. What is a major application?",
        correct="Monitoring mass transport in the Earth system — ice sheet melting in Greenland and Antarctica, groundwater depletion, post-glacial rebound, and seasonal water cycle variations",
        distractors=[
            "Measuring tectonic plate motion",
            "Determining the positions of GNSS satellites",
            "Monitoring volcanic eruptions in real time"
        ]
    ),
    create_mc_question(
        id="grav_007", topic="grace_vs_champ",
        question="Why did GRACE achieve much higher spatial resolution in the gravity field compared to CHAMP?",
        correct="GRACE's LL-SST measured gravity differences between two nearby points with micrometer precision, effectively sensing the gravity gradient — this is far more sensitive than CHAMP's HL-SST, which measured the integral effect on the orbit",
        distractors=[
            "GRACE orbited at a higher altitude",
            "GRACE had better solar panels",
            "GRACE used optical instead of microwave ranging"
        ]
    ),
    create_mc_question(
        id="grav_008", topic="goce",
        question="GOCE (2009–2013) introduced a new measurement principle for satellite gravimetry. What was it?",
        correct="Satellite Gravity Gradiometry (SGG) — measuring the gravity gradient tensor (second derivatives of the potential) using a 3-axis differential accelerometer (gradiometer) on board the satellite",
        distractors=[
            "Interferometric laser ranging between two satellites",
            "Continuous SLR tracking from a dense ground network",
            "Radar altimetry of the ocean surface"
        ]
    ),
    create_mc_question(
        id="grav_009", topic="goce_orbit",
        question="GOCE orbited at an extremely low altitude of about 250 km. Why was such a low orbit chosen despite the challenge of atmospheric drag?",
        correct="The gravity signal attenuates rapidly with altitude — a lower orbit provides a stronger gravity signal, enabling higher spatial resolution. GOCE used ion thrusters for continuous drag compensation",
        distractors=[
            "Lower orbits are more stable against radiation damage",
            "GOCE needed to be below the ionosphere for its measurements",
            "Lower orbits require less fuel to achieve"
        ]
    ),
    create_mc_question(
        id="grav_010", topic="grace_c",
        question="GRACE-C (planned for launch ~2028) will continue the GRACE mission concept. What is the primary motivation for continuity?",
        correct="The time-variable gravity field data record must be maintained without gaps — interruptions would compromise the ability to detect long-term trends in ice mass loss, groundwater changes, and sea level rise",
        distractors=[
            "GRACE-C will use a fundamentally new measurement principle",
            "The previous missions' data has been lost",
            "GRACE-C is purely an engineering demonstration"
        ]
    ),
    tf(
        id="grav_011", topic="ice_loss",
        question="GRACE data has shown that Greenland and Antarctica are losing hundreds of gigatons of ice mass per year, contributing to global sea level rise.",
        correct=True
    ),
    create_mc_question(
        id="grav_012", topic="hl_vs_ll",
        question="High-Low SST (HL-SST) as used by CHAMP tracks the LEO satellite using GNSS satellites at higher altitude. Low-Low SST (LL-SST) as used by GRACE measures the distance between two co-orbiting LEO satellites. What is the fundamental advantage of LL-SST?",
        correct="LL-SST is sensitive to shorter-wavelength (smaller-scale) gravity field features because it measures differential acceleration between two nearby points, acting as a spatial high-pass filter",
        distractors=[
            "LL-SST requires only one satellite while HL-SST requires two",
            "HL-SST has higher precision than LL-SST",
            "LL-SST works in any orbit while HL-SST requires a specific inclination"
        ]
    ),
]

# ============================================================
# TOPIC: navigation (L16) — 5 questions
# ============================================================
navigation = [
    create_mc_question(
        id="nav_001", topic="navigation_definition",
        question="What distinguishes navigation from positioning?",
        correct="Navigation is dynamic positioning — it involves continuously determining position and possibly velocity while moving, whereas positioning can be a single static determination",
        distractors=[
            "Navigation uses satellites while positioning uses ground-based methods",
            "Positioning is more accurate than navigation",
            "Navigation works only at sea while positioning works only on land"
        ]
    ),
    create_mc_question(
        id="nav_002", topic="position_fixing",
        question="In navigation, position fixing determines location from external references. What is the alternative method that does not require external references?",
        correct="Dead reckoning — estimating the current position by advancing a known previous position using measured heading (direction) and speed over time",
        distractors=[
            "Triangulation using nearby landmarks",
            "Satellite altimetry",
            "Inertial navigation using star trackers"
        ]
    ),
    create_mc_question(
        id="nav_003", topic="dead_reckoning",
        question="Dead reckoning has a fundamental weakness. What is it?",
        correct="Errors accumulate over time — small errors in measured heading or speed grow without bound because each new position estimate is based on the previous (potentially erroneous) one",
        distractors=[
            "It cannot work in three dimensions",
            "It requires an internet connection",
            "It is limited to speeds below 100 km/h"
        ]
    ),
    create_mc_question(
        id="nav_004", topic="agps",
        question="Assisted GPS (A-GPS) was developed for mobile phone positioning. What does the assistance data provide?",
        correct="Satellite almanac, approximate position, and atmospheric corrections from the cellular network — this dramatically reduces the time-to-first-fix compared to standalone GPS by eliminating the need to download the full navigation message",
        distractors=[
            "A direct connection to the GPS control segment",
            "Higher signal power from the satellites",
            "An alternative positioning method that replaces GPS entirely"
        ]
    ),
    create_mc_question(
        id="nav_005", topic="celestial_navigation",
        question="Celestial (astronomical) navigation was used for centuries before satellite positioning. It determines position by:",
        correct="Measuring the angles between celestial bodies (stars, Sun, Moon) and the horizon, then using these angles with precise time to compute latitude and longitude",
        distractors=[
            "Tracking the motion of planets to predict future weather",
            "Using the gravitational pull of the Moon to determine heading",
            "Counting the stars visible in the sky to estimate latitude"
        ]
    ),
]

# ============================================================
# Write all topic files
# ============================================================
print("Generating Space Geodesy quiz questions:")
write_topic("reference_systems", reference_systems)
write_topic("earth_orientation", earth_orientation)
write_topic("gnss_fundamentals", gnss_fundamentals)
write_topic("gnss_signals_errors", gnss_signals_errors)
write_topic("gnss_remote_sensing", gnss_remote_sensing)
write_topic("satellite_orbits", satellite_orbits)
write_topic("numerical_integration", numerical_integration)
write_topic("spherical_harmonics", spherical_harmonics)
write_topic("slr_prare_doris", slr_prare_doris)
write_topic("vlbi", vlbi)
write_topic("ggos", ggos)
write_topic("altimetry", altimetry)
write_topic("orbit_perturbations", orbit_perturbations)
write_topic("gravity_missions", gravity_missions)
write_topic("navigation", navigation)

# Summary
all_topics = [
    reference_systems, earth_orientation, gnss_fundamentals, gnss_signals_errors,
    gnss_remote_sensing, satellite_orbits, numerical_integration, spherical_harmonics,
    slr_prare_doris, vlbi, ggos, altimetry, orbit_perturbations, gravity_missions, navigation
]
total = sum(len(t) for t in all_topics)
print(f"\nTotal: {total} questions across {len(all_topics)} topics")