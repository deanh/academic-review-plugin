#!/usr/bin/env python3
"""Generate GIS (Geoinformatics) quiz question files for exam prep."""

import json
from pathlib import Path
from quiz_utils import create_mc_question

OUTPUT_DIR = Path(__file__).parent.parent / "server" / "data" / "questions" / "gis"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def tf(id, question, correct, topic):
    return {"id": id, "type": "true_false", "question": question, "correct": correct, "topic": topic}


def write_topic(filename, questions):
    path = OUTPUT_DIR / f"{filename}.json"
    path.write_text(json.dumps(questions, indent=2))
    print(f"  {filename}: {len(questions)} questions")


# ============================================================
# TOPIC: introduction (Lecture 01)
# ============================================================
introduction = [
    create_mc_question(
        id="intro_001", topic="geoinformatics_definition",
        question="Geoinformatics is the science that deals with digital geo data. What defines 'geo data'?",
        correct="Digital information about the earth that has a spatial reference",
        distractors=[
            "Any digital information stored in a database",
            "Data collected exclusively by satellite sensors",
            "Information about the earth that is stored only in raster format"
        ]
    ),
    create_mc_question(
        id="intro_002", topic="spatial_reference",
        question="Geo data requires a spatial reference. What are the two types of spatial reference?",
        correct="Direct spatial reference (coordinates) and indirect spatial reference (relating to a well-established spatial object)",
        distractors=[
            "Absolute reference (GPS) and relative reference (compass)",
            "Primary reference (measured) and secondary reference (derived)",
            "Horizontal reference and vertical reference"
        ]
    ),
    create_mc_question(
        id="intro_003", topic="gis_definition",
        question="A Geographical Information System (GIS) is a computer-based system for performing four key functions on geo data. Which mnemonic summarizes these functions?",
        correct="IMAP: Input and Update, Management and Modeling, Analysis and Simulation, Presentation and Output",
        distractors=[
            "CRUD: Create, Read, Update, Delete",
            "ACID: Atomicity, Consistency, Isolation, Durability",
            "SMAP: Storage, Mapping, Analysis, Printing"
        ]
    ),
    create_mc_question(
        id="intro_004", topic="gis_components",
        question="The 4-component model of a GIS includes structural components with different life spans. Which component has the longest life span?",
        correct="Data (textual, numeric, graphical) — approximately 25 to 75 years",
        distractors=[
            "Hardware — approximately 25 to 75 years",
            "Software — approximately 25 to 75 years",
            "Users — their expertise lasts the longest"
        ]
    ),
    tf(
        id="intro_005", topic="gis_vs_software",
        question="A GIS is a software product, not a system.",
        correct=False
    ),
    create_mc_question(
        id="intro_006", topic="gis_types",
        question="Which type of GIS is specifically designed for mapping of operating resources such as gas, water, energy, and telecommunication networks?",
        correct="Network Information Systems (NIS)",
        distractors=[
            "Land Information Systems (LIS)",
            "Environmental Information Systems (EIS)",
            "Spatial Information Systems (SIS)"
        ]
    ),
    create_mc_question(
        id="intro_007", topic="gis_types",
        question="A Land Information System (LIS) is primarily concerned with:",
        correct="Legal foundation and documentation, such as cadastral maps and registers",
        distractors=[
            "Routing and navigation for vehicles",
            "Environmental impact assessments",
            "Mapping of utility networks"
        ]
    ),
    create_mc_question(
        id="intro_008", topic="gis_linking",
        question="A fundamental capability of a GIS is establishing the relationship between thematic information and cartographic mapping. What enables this linkage?",
        correct="The spatial reference (georeferencing) that both thematic and geometric data share",
        distractors=[
            "A common file format used by all GIS layers",
            "Manual annotation by the user",
            "Automatic image recognition of map features"
        ]
    ),
    tf(
        id="intro_009", topic="gis_analysis",
        question="A simulation in GIS is used to obtain system knowledge for spatial phenomena by automatic variant generation of a given model.",
        correct=True
    ),
    create_mc_question(
        id="intro_010", topic="gis_functional",
        question="Which of the following is one of the four functional components of a GIS?",
        correct="Analyses and Simulations",
        distractors=[
            "Data Encryption",
            "User Authentication",
            "Version Control"
        ]
    ),
]

# ============================================================
# TOPIC: thematic_modeling (Lecture 02)
# ============================================================
thematic_modeling = [
    create_mc_question(
        id="thematic_001", topic="modeling",
        question="In GIS, modeling constitutes the process of transforming the real world into a conceptual or digital representation. What is the fundamental requirement of this process?",
        correct="Abstraction — models can capture only selected aspects of reality",
        distractors=[
            "Completeness — models must capture every aspect of reality",
            "Compression — models must minimize storage space",
            "Automation — models must be generated without human input"
        ]
    ),
    create_mc_question(
        id="thematic_002", topic="data_model_vs_structure",
        question="What is the difference between a data model and a data structure?",
        correct="A data model is a high-level conceptual framework defining logical organization; a data structure is a technical implementation for organizing data in memory",
        distractors=[
            "A data model is for raster data; a data structure is for vector data",
            "A data model describes geometry; a data structure describes attributes",
            "They are the same thing — the terms are interchangeable"
        ]
    ),
    create_mc_question(
        id="thematic_003", topic="discrete_objects",
        question="In the discrete object view, geographic phenomena are conceptualized as distinct, identifiable entities. What are the three dimensionalities used to represent discrete objects?",
        correct="0D (points), 1D (lines), 2D (polygons)",
        distractors=[
            "1D (lines), 2D (surfaces), 3D (volumes)",
            "Points, pixels, and voxels",
            "Scalars, vectors, and tensors"
        ]
    ),
    create_mc_question(
        id="thematic_004", topic="continuous_fields",
        question="In the continuous field view, the world is conceptualized as spatially continuous phenomena. Which of the following is an example of a vector field (as opposed to a scalar field)?",
        correct="Wind — it has both magnitude and direction at every location",
        distractors=[
            "Temperature — it varies continuously across space",
            "Elevation — it has a measurable value at every point",
            "Precipitation — it has a numeric value at each location"
        ]
    ),
    create_mc_question(
        id="thematic_005", topic="layer_principle",
        question="In the thematic layer principle, how are layers implicitly linked to each other?",
        correct="Through georeferencing — defined by the coordinate reference system and spatial extent",
        distractors=[
            "Through foreign keys in a relational database",
            "Through a shared attribute table",
            "Through a common file naming convention"
        ]
    ),
    create_mc_question(
        id="thematic_006", topic="object_class_principle",
        question="The object class principle (OCP) in GIS is comparable to which programming paradigm?",
        correct="Object-oriented programming (OOP) — classes define attributes and relationships, and support inheritance",
        distractors=[
            "Functional programming — data is immutable and transformations are composable",
            "Procedural programming — operations are organized in sequential procedures",
            "Logic programming — relationships are expressed as logical rules"
        ]
    ),
    create_mc_question(
        id="thematic_007", topic="layer_vs_ocp",
        question="What is a key limitation of the thematic layer principle compared to the object class principle?",
        correct="Layers are defined independently — entities sharing a subset of properties but not being similar must be modeled in different layers",
        distractors=[
            "Layers cannot store geometric information",
            "Layers cannot be overlaid or combined",
            "Layers are limited to raster data only"
        ]
    ),
    create_mc_question(
        id="thematic_008", topic="4_layer_model",
        question="The 4-layer model in GIS describes four views. Which view handles thematic, geometric, and topological modeling of a section of the real world?",
        correct="Conceptual view",
        distractors=[
            "External view",
            "Logical view",
            "Internal view"
        ]
    ),
    create_mc_question(
        id="thematic_009", topic="4_layer_model",
        question="In the GIS 4-layer model, the logical view handles:",
        correct="Representation of the models in data structures",
        distractors=[
            "How the GIS is presented to the user (interface)",
            "Thematic and geometric modeling of the real world",
            "Physical data storage and management"
        ]
    ),
    tf(
        id="thematic_010", topic="continuous_fields",
        question="Continuous fields must always be defined over two-dimensional areas; they cannot be defined along one-dimensional spaces.",
        correct=False
    ),
    create_mc_question(
        id="thematic_011", topic="networks",
        question="In GIS, a network is modeled using which two components?",
        correct="Geometry modeled by lines (ordered sequences of connected points) and topology modeled by graphs using vertices and edges",
        distractors=[
            "Raster cells and their neighborhood relationships",
            "Points and their Voronoi diagrams",
            "Polygons and their centroid coordinates"
        ]
    ),
    create_mc_question(
        id="thematic_012", topic="modeling_challenges",
        question="A significant difficulty in geographic modeling is that the world is dynamic. Which of the following illustrates this challenge?",
        correct="A forest area (polygon) might shrink to a few separate trees (points), requiring a change in geometry type",
        distractors=[
            "Converting data from one coordinate system to another",
            "Storing very large raster datasets efficiently",
            "Ensuring that all attributes use the same data type"
        ]
    ),
    tf(
        id="thematic_013", topic="layer_vs_ocp",
        question="In practice, data models (blueprints) are often defined using the object class principle, while GIS software organizes data according to the layer principle (layers in QGIS, tables in PostGIS).",
        correct=True
    ),
    create_mc_question(
        id="thematic_014", topic="richness",
        question="Regarding the richness of a GIS data model, which statement best describes the challenge?",
        correct="Too simple oversimplifies reality; too detailed adds complexity and raises costs — getting it right is difficult, and stability is crucial since changes affect existing data",
        distractors=[
            "Models should always be as detailed as possible to ensure accuracy",
            "The simplest possible model is always preferred for efficiency",
            "Model richness is irrelevant since data can always be re-modeled"
        ]
    ),
]

# ============================================================
# TOPIC: geometric_modeling (Lecture 03)
# ============================================================
geometric_modeling = [
    create_mc_question(
        id="geom_001", topic="point_sets",
        question="In point set modeling, the interior of a point set is defined as the set of points where:",
        correct="The neighborhood of each point is completely inside the point set",
        distractors=[
            "The points lie on the boundary of the set",
            "At least half the neighborhood is inside the set",
            "The points are the farthest from the boundary"
        ]
    ),
    create_mc_question(
        id="geom_002", topic="point_sets",
        question="What is the 'closure' of a point set?",
        correct="The set of points that are in the interior and on the boundary",
        distractors=[
            "Only the interior points",
            "Only the boundary points",
            "The exterior of the point set"
        ]
    ),
    create_mc_question(
        id="geom_003", topic="raster_model",
        question="In a raster model, how are discrete objects distinguished when multiple objects of the same category are present?",
        correct="Different object instances are distinguished by integer values (integer IDs) assigned to each cell",
        distractors=[
            "Each object is stored in a separate raster layer",
            "Objects are distinguished by their color in the visualization",
            "Each cell stores the object's full attribute table"
        ]
    ),
    create_mc_question(
        id="geom_004", topic="vector_model",
        question="Which of the following is true about vector models for representing geometry?",
        correct="The models are unambiguous (no room for interpretation) and unique (only one way to represent a geometry), and they are compact",
        distractors=[
            "Vector models are always larger than raster models",
            "Vector models can represent the same geometry in multiple equivalent ways",
            "Vector models require less computational power than raster models for all operations"
        ]
    ),
    create_mc_question(
        id="geom_005", topic="raster_vs_vector",
        question="Doubling the resolution of a raster model causes the data size to increase by approximately:",
        correct="Four times (n² increase for n times the resolution)",
        distractors=[
            "Two times",
            "Eight times",
            "Sixteen times"
        ]
    ),
    create_mc_question(
        id="geom_006", topic="raster_vs_vector",
        question="For spatial overlays (intersection of layers), which model is simpler and more efficient?",
        correct="Raster — overlay is simple cell-by-cell operations on grid values",
        distractors=[
            "Vector — boolean operations on polygons are straightforward",
            "Both are equally efficient",
            "Neither supports spatial overlays"
        ]
    ),
    create_mc_question(
        id="geom_007", topic="brep",
        question="In a 3D boundary representation (BREP), a solid is described by:",
        correct="Its bounding surface — a collection of polygonal faces glued together to form a closed skin",
        distractors=[
            "A voxel grid that fills the volume",
            "A point cloud of interior points",
            "A single polygon representing its largest face"
        ]
    ),
    create_mc_question(
        id="geom_008", topic="georeferencing",
        question="Every raster needs georeferencing information. What does this information provide?",
        correct="A mapping from the index of raster cells to real world coordinates in some coordinate reference system",
        distractors=[
            "The color palette used to display the raster",
            "The compression algorithm used for storage",
            "The projection from 3D to 2D screen coordinates"
        ]
    ),
    create_mc_question(
        id="geom_009", topic="h3",
        question="Uber's H3 Hexagonal Hierarchical Spatial Index uses hexagonal cells. Why are 12 pentagons unavoidable in the H3 tiling?",
        correct="They are located at the vertices of the icosahedron — a mathematical necessity when tiling a sphere with hexagons",
        distractors=[
            "They are used as special index markers for the hierarchy",
            "They result from data loss during projection",
            "They are a design choice to mark the boundaries between resolution levels"
        ]
    ),
    tf(
        id="geom_010", topic="h3",
        question="H3 is a method for modeling geometry.",
        correct=False  # It is a spatial index, not a method for modeling geometry
    ),
    create_mc_question(
        id="geom_011", topic="raster_vs_vector",
        question="Raster models have weak topology because they consider only neighboring cells, not objects. What is a consequence of this?",
        correct="Topological analyses (e.g., network analysis) are complex and not well-suited for raster data",
        distractors=[
            "Raster models cannot store continuous field data",
            "Raster models cannot represent point features",
            "Raster cells must all have the same value"
        ]
    ),
    create_mc_question(
        id="geom_012", topic="raster_vs_vector",
        question="When is the raster model the preferred choice over vector?",
        correct="For area-covering problems with high spatial and thematic density and low demands for precision",
        distractors=[
            "When high precision of coordinates is required",
            "When the data is sparse and only a few features exist",
            "When topological analysis is the primary goal"
        ]
    ),
    create_mc_question(
        id="geom_013", topic="vector_model",
        question="In the vector model, an area (polygon) is defined by:",
        correct="An exterior ring and optionally several interior rings (holes), each being a closed sequence of points",
        distractors=[
            "A single closed sequence of points with no holes allowed",
            "A set of connected raster cells",
            "A bounding box and a fill value"
        ]
    ),
    tf(
        id="geom_014", topic="raster_vs_vector",
        question="Continuous field data of high spatial and thematic density (e.g., temperature or elevation data) is more efficiently stored in raster format than in vector format.",
        correct=True
    ),
    create_mc_question(
        id="geom_015", topic="raster_model",
        question="In a raster model for continuous fields, how are cells with no data value typically handled?",
        correct="A special numeric value is defined that is not a valid value for the variable (e.g., -1 for temperature in Kelvin)",
        distractors=[
            "The cell is simply left empty in memory",
            "The cell is assigned the average of its neighbors",
            "The cell is removed from the raster"
        ]
    ),
]

# ============================================================
# TOPIC: spatial_overlays (Lecture 04)
# ============================================================
spatial_overlays = [
    create_mc_question(
        id="overlay_001", topic="point_in_polygon",
        question="The point-in-polygon test is based on the Jordan curve theorem. What does this theorem state?",
        correct="A closed, intersection-free curve divides the plane into an inside and an outside region",
        distractors=[
            "Any polygon can be triangulated into non-overlapping triangles",
            "A convex polygon always contains its centroid",
            "Every closed curve has a finite area"
        ]
    ),
    create_mc_question(
        id="overlay_002", topic="point_in_polygon",
        question="In the ray crossing test for point-in-polygon, a ray is cast from the test point. How is the result determined?",
        correct="Odd number of intersections with the polygon boundary → point inside; even number → point outside",
        distractors=[
            "If the ray hits any edge → point inside; if it misses → point outside",
            "Count intersections: more than 2 → inside; 2 or fewer → outside",
            "If the first intersection is with an exterior ring → inside; interior ring → outside"
        ]
    ),
    create_mc_question(
        id="overlay_003", topic="point_in_polygon",
        question="Before performing the actual point-in-polygon test, what optimization is typically applied?",
        correct="A test with the minimum bounding box — if the point is outside the bounding box, it cannot be inside the polygon",
        distractors=[
            "The polygon is first triangulated",
            "The point is projected onto the nearest edge",
            "The polygon is simplified by removing interior rings"
        ]
    ),
    create_mc_question(
        id="overlay_004", topic="boolean_operations",
        question="In the Margalit and Knott algorithm for boolean intersection of two polygons, what is the first step?",
        correct="Classification of all polygon points as Inside (I), Outside (O), or on the Boundary (B) of the other polygon",
        distractors=[
            "Computing the convex hull of both polygons",
            "Triangulating both polygons",
            "Finding the centroid of each polygon"
        ]
    ),
    create_mc_question(
        id="overlay_005", topic="boolean_operations",
        question="In the Margalit-Knott algorithm, after classifying points and splitting intersecting edges, edges are classified. For a boolean intersection, which edges are kept?",
        correct="Inside edges and boundary edges are kept; outside edges are discarded",
        distractors=[
            "Only boundary edges are kept",
            "Only outside edges are kept",
            "All edges are kept and then filtered by area"
        ]
    ),
    create_mc_question(
        id="overlay_006", topic="boolean_operations",
        question="In the Margalit-Knott algorithm, when two identical edges with opposite directions are found during polygon generation, what happens?",
        correct="Both edges are removed",
        distractors=[
            "One edge is removed and the other is kept",
            "Both edges are kept in the result",
            "The edges are merged into a single edge"
        ]
    ),
    create_mc_question(
        id="overlay_007", topic="map_algebra",
        question="Tomlin's Map Algebra model defines three types of operations on raster layers. A local operation:",
        correct="Combines the values taken at the same raster location from one or many layers according to some function",
        distractors=[
            "Summarizes data values that fall within given zones",
            "Determines cell values from a defined local neighborhood (e.g., 3×3 window)",
            "Computes the shortest path between two cells"
        ]
    ),
    create_mc_question(
        id="overlay_008", topic="map_algebra",
        question="In Map Algebra, a focal operation determines a cell's value by combining values from its local neighborhood. Which of the following is an example of a focal operation?",
        correct="Computing slope, aspect, or curvature from a digital elevation model",
        distractors=[
            "Adding two raster layers cell by cell",
            "Computing the average elevation per land-use zone",
            "Reclassifying elevation values into categories"
        ]
    ),
    create_mc_question(
        id="overlay_009", topic="map_algebra",
        question="A zonal operation in Map Algebra:",
        correct="Summarizes data values that fall within given zones (e.g., mean elevation per district)",
        distractors=[
            "Applies a function to each cell independently",
            "Uses a moving window to compute neighborhood statistics",
            "Creates new zones by intersecting two polygon layers"
        ]
    ),
    tf(
        id="overlay_010", topic="boolean_operations",
        question="The Margalit-Knott algorithm for boolean polygon operations requires that both input polygons have the same orientation of vertices (both clockwise or both counterclockwise).",
        correct=True
    ),
    create_mc_question(
        id="overlay_011", topic="map_algebra",
        question="Map Algebra was originally designed for raster data, but its principles can also be applied to vector data. When applied to vector data:",
        correct="Operations need to be adapted, with focus shifting to objects such as points, lines, and polygons, but the core idea of combining data mathematically remains",
        distractors=[
            "The operations are identical to the raster versions",
            "Only local operations are applicable to vector data",
            "Map Algebra concepts cannot be meaningfully applied to vector data"
        ]
    ),
    create_mc_question(
        id="overlay_012", topic="boolean_operations",
        question="Why are boolean set operations on polygons (intersection, union, difference) considered difficult to implement?",
        correct="They involve many steps, require additional algorithms (point-in-polygon, line segment intersection), and are difficult to implement robustly",
        distractors=[
            "They can only work with convex polygons",
            "They require 3D geometry processing",
            "They always produce invalid geometries"
        ]
    ),
]

# ============================================================
# TOPIC: topological_data_structures (Lecture 05) — DEEP
# ============================================================
topological_data_structures = [
    create_mc_question(
        id="topo_ds_001", topic="topology_types",
        question="Three types of topology are distinguished in GIS. Connectivity refers to:",
        correct="Information about links between spatial objects, such as line features meeting at common endpoints",
        distractors=[
            "Information about direct neighbors sharing common boundaries",
            "Information about features occupying the same space",
            "The number of holes in a polygon"
        ]
    ),
    create_mc_question(
        id="topo_ds_002", topic="topology_types",
        question="Adjacency topology provides:",
        correct="Information about the direct neighbors of spatial objects, e.g., area features sharing common boundaries with edges storing left/right polygon information",
        distractors=[
            "Information about which features are connected by common endpoints",
            "The coordinates of all vertices in the dataset",
            "Information about which features completely contain other features"
        ]
    ),
    create_mc_question(
        id="topo_ds_003", topic="topology_types",
        question="Containment topology deals with:",
        correct="Information about the overlap between spatial objects, where topological primitives (node, edge, face) contain information about features sharing space",
        distractors=[
            "Whether one polygon is larger than another",
            "Whether two features are connected at endpoints",
            "The hierarchical nesting of coordinate reference systems"
        ]
    ),
    create_mc_question(
        id="topo_ds_004", topic="why_topology",
        question="Without a topological data structure, editing the coordinates of one polygon in a tessellation (space-filling map) results in:",
        correct="Gaps or overlaps with neighboring polygons, because shared boundaries are stored independently",
        distractors=[
            "Automatic updates to all neighboring polygons",
            "No change to the overall map",
            "The polygon being deleted"
        ]
    ),
    create_mc_question(
        id="topo_ds_005", topic="why_topology",
        question="Which of the following is NOT a benefit of topological data structures?",
        correct="Faster rendering of individual polygon fills",
        distractors=[
            "Reduced data storage by storing boundaries only once",
            "Prevention of inconsistencies from incorrect digitizing",
            "Efficient analyses based on connectivity, adjacency, and containment"
        ]
    ),
    create_mc_question(
        id="topo_ds_006", topic="2_manifold",
        question="A 2-manifold surface requires that each point (except on boundaries of open faces) is surrounded by a two-dimensional neighborhood belonging to the surface. Which configuration violates the 2-manifold property?",
        correct="Two objects that touch only at a single point or along a line segment",
        distractors=[
            "A closed cube made of six planar faces",
            "A sphere",
            "A cylinder without caps"
        ]
    ),
    create_mc_question(
        id="topo_ds_007", topic="polygon_boundary_model",
        question="In the polygon-based boundary model (spaghetti model), how are faces defined?",
        correct="Each face is a sequence of coordinate triplets; coordinates are redundantly stored in each face that shares them",
        distractors=[
            "Faces reference shared edges, which reference shared vertices",
            "Faces reference shared vertices that hold coordinates",
            "Faces are stored as references to half-edges"
        ]
    ),
    create_mc_question(
        id="topo_ds_008", topic="vertex_boundary_model",
        question="The vertex-based boundary model improves on the spaghetti model by:",
        correct="Introducing vertices as independent topological entities that hold coordinates, so polygons reference vertices instead of duplicating coordinates",
        distractors=[
            "Adding edge entities between vertices and faces",
            "Storing topology information in each vertex",
            "Eliminating the need for face definitions"
        ]
    ),
    create_mc_question(
        id="topo_ds_009", topic="edge_boundary_model",
        question="In the edge-based boundary model, what three tables are used to define the topology?",
        correct="A face table (listing edges per face), an edge table (listing start and end vertices per edge), and a vertex table (listing coordinates)",
        distractors=[
            "A face table, a point table, and a coordinate table",
            "A vertex table, a normal table, and a texture table",
            "An edge table, a half-edge table, and a vertex table"
        ]
    ),
    create_mc_question(
        id="topo_ds_010", topic="winged_edge",
        question="In the winged-edge data structure, each edge stores links to $e_{n+}$ and $e_{n-}$. What do these represent?",
        correct="$e_{n+}$ is the next edge when the edge is positively directed (same as face orientation); $e_{n-}$ is the next edge when negatively directed",
        distractors=[
            "$e_{n+}$ is the edge to the right; $e_{n-}$ is the edge to the left",
            "$e_{n+}$ is the next edge clockwise; $e_{n-}$ is the next edge counterclockwise",
            "$e_{n+}$ links to the start vertex; $e_{n-}$ links to the end vertex"
        ]
    ),
    create_mc_question(
        id="topo_ds_011", topic="winged_edge",
        question="In the winged-edge data structure, a face only needs to store one piece of information (besides an ID). What is it?",
        correct="A reference to one arbitrary (starting) edge — all other edges can be found by following the linked edge pointers",
        distractors=[
            "A list of all edges forming its boundary",
            "The coordinates of its centroid",
            "The total number of edges in its boundary"
        ]
    ),
    create_mc_question(
        id="topo_ds_012", topic="winged_edge_traversal",
        question="To traverse all edges of a face in the winged-edge data structure, you start with the first edge and follow links. How do you determine if an edge is positively or negatively directed with respect to the face?",
        correct="Compare the start vertex of the current edge with the end vertex of the previous edge — if they match, the edge is positively directed; otherwise, swap start/end and follow the negative link",
        distractors=[
            "Check if the edge is stored in the face's edge list in forward order",
            "Look at the face normal and compare with the edge direction",
            "The direction is always positive for the first half of edges"
        ]
    ),
    create_mc_question(
        id="topo_ds_013", topic="winged_edge",
        question="In the extended winged-edge data structure, each edge stores $f_+$ and $f_-$. What do these represent?",
        correct="$f_+$ is the face on the right side (when the edge is positively directed) and $f_-$ is the face on the left side",
        distractors=[
            "$f_+$ is the face above the edge and $f_-$ is the face below",
            "$f_+$ is the face with more edges and $f_-$ is the face with fewer",
            "$f_+$ and $f_-$ are the two faces created when the edge is split"
        ]
    ),
    create_mc_question(
        id="topo_ds_014", topic="winged_edge",
        question="With the extended winged-edge data structure storing $f_+$ and $f_-$ on each edge, the face table no longer needs to store:",
        correct="The direction/sign of the first edge — it can be determined by checking whether the face ID appears in $f_+$ or $f_-$ of the edge",
        distractors=[
            "The first edge reference",
            "The face ID",
            "Any geometric information"
        ]
    ),
    create_mc_question(
        id="topo_ds_015", topic="winged_edge",
        question="The full winged-edge data structure adds $e_{p+}$ and $e_{p-}$ (previous edge links) in addition to $e_{n+}$ and $e_{n-}$. What additional capability does this provide?",
        correct="Finding all edges incident to a given vertex by cycling through edge links, without needing to traverse an entire face boundary",
        distractors=[
            "Finding the area of each face more efficiently",
            "Supporting non-planar faces",
            "Enabling parallel processing of edges"
        ]
    ),
    create_mc_question(
        id="topo_ds_016", topic="polygon_holes",
        question="In the winged-edge data structure, faces with interior rings (holes) can be handled in two ways. What is Alternative 1?",
        correct="Connect exterior and interior rings with auxiliary (bridge) edges, creating a single boundary ring — auxiliary edges appear twice in the same polygon",
        distractors=[
            "Store holes in a separate data structure",
            "Triangulate the polygon to eliminate holes",
            "Ignore holes and store only the exterior ring"
        ]
    ),
    create_mc_question(
        id="topo_ds_017", topic="validity",
        question="For a boundary model to be valid, which of the following conditions must hold?",
        correct="The set of faces forms a closed hull (each edge is incident to exactly 2 faces), faces do not intersect except at edges/vertices, and face boundaries are simple (no self-intersections)",
        distractors=[
            "All faces must be triangles",
            "All faces must have the same number of edges",
            "The solid must be convex"
        ]
    ),
    create_mc_question(
        id="topo_ds_018", topic="exterior_face",
        question="In the winged-edge data structure for a planar subdivision, what role does the 'exterior face' play?",
        correct="It represents the unbounded exterior region, allowing every edge to be incident to exactly two faces, which completes the data structure",
        distractors=[
            "It is the largest polygon in the dataset",
            "It stores metadata about the entire dataset",
            "It is only used for visualization purposes"
        ]
    ),
    tf(
        id="topo_ds_019", topic="spaghetti",
        question="The polygon-based boundary model (spaghetti model) has no topological data structure at all — it stores faces as independent sequences of coordinates with high redundancy.",
        correct=True
    ),
    create_mc_question(
        id="topo_ds_020", topic="half_edge",
        question="Besides the winged-edge data structure, another common topological representation mentioned in the lectures is:",
        correct="The half-edge data structure, where each edge is represented by two half-edges with opposite directions",
        distractors=[
            "The quarter-edge data structure with four directed segments per edge",
            "The full-edge data structure with all faces stored per edge",
            "The dual-edge data structure connecting faces to their duals"
        ]
    ),
]

# ============================================================
# TOPIC: topological_modeling (Lecture 06)
# ============================================================
topological_modeling = [
    create_mc_question(
        id="topo_mod_001", topic="graph_definition",
        question="A graph $G = (V, E)$ consists of a collection of vertices $V$ and edges $E$. How are edges defined?",
        correct="As a set of (unordered) pairs of vertices: $E \\subseteq V \\times V$",
        distractors=[
            "As a set of ordered triplets of vertices",
            "As a mapping from vertices to real numbers",
            "As a sequence of coordinates"
        ]
    ),
    create_mc_question(
        id="topo_mod_002", topic="degree",
        question="The degree $d(v)$ of a vertex $v$ is defined as:",
        correct="The number of edges that are incident to vertex $v$",
        distractors=[
            "The number of vertices adjacent to $v$ that have been visited",
            "The distance from $v$ to the root of the graph",
            "The weight of the heaviest edge incident to $v$"
        ]
    ),
    create_mc_question(
        id="topo_mod_003", topic="path_cycle",
        question="What distinguishes a cycle from a path in a graph?",
        correct="A cycle is a path where the start vertex and the end vertex are the same",
        distractors=[
            "A cycle visits every vertex exactly once; a path may skip vertices",
            "A cycle uses every edge exactly once; a path may reuse edges",
            "A cycle only exists in directed graphs; paths exist in undirected graphs"
        ]
    ),
    create_mc_question(
        id="topo_mod_004", topic="eulerian",
        question="An Eulerian path uses each edge exactly once. For a connected planar graph, what condition must hold for an Eulerian path to exist?",
        correct="All vertices have even degree, except possibly the start and end vertices (which may have odd degree)",
        distractors=[
            "All vertices must have odd degree",
            "The graph must have an even number of vertices",
            "The graph must be a tree"
        ]
    ),
    create_mc_question(
        id="topo_mod_005", topic="eulerian",
        question="An Eulerian cycle (using each edge exactly once and returning to the start) exists in a connected graph if and only if:",
        correct="The degree of every vertex is even",
        distractors=[
            "The degree of every vertex is odd",
            "The graph has an even number of edges",
            "The graph is planar and has no self-loops"
        ]
    ),
    create_mc_question(
        id="topo_mod_006", topic="hamiltonian",
        question="What distinguishes a Hamiltonian path from an Eulerian path?",
        correct="A Hamiltonian path visits each vertex exactly once; an Eulerian path uses each edge exactly once",
        distractors=[
            "A Hamiltonian path uses each edge exactly once; an Eulerian path visits each vertex exactly once",
            "A Hamiltonian path exists only in weighted graphs; an Eulerian path in unweighted graphs",
            "They are the same concept with different names"
        ]
    ),
    create_mc_question(
        id="topo_mod_007", topic="hamiltonian",
        question="Determining whether a graph contains a Hamiltonian path or cycle is:",
        correct="Computationally hard — no efficient algorithm is known; one must try all possibilities",
        distractors=[
            "Solvable in linear time by checking vertex degrees",
            "Equivalent to finding an Eulerian cycle",
            "Always solvable in $O(n \\log n)$ time"
        ]
    ),
    create_mc_question(
        id="topo_mod_008", topic="planar_graph",
        question="A graph is planar if:",
        correct="It can be drawn on the Euclidean plane without any edge crossings",
        distractors=[
            "All its vertices have the same degree",
            "It contains no cycles",
            "It has fewer edges than vertices"
        ]
    ),
    create_mc_question(
        id="topo_mod_009", topic="connected_graph",
        question="A graph is connected if:",
        correct="There exists a path from any vertex to any other vertex in the graph",
        distractors=[
            "Every vertex is adjacent to every other vertex",
            "The graph contains at least one cycle",
            "Every vertex has degree ≥ 2"
        ]
    ),
    create_mc_question(
        id="topo_mod_010", topic="koenigsberg",
        question="Euler's analysis of the Seven Bridges of Königsberg showed that a walk crossing each bridge exactly once was impossible because:",
        correct="All four landmasses (vertices) had odd degree, so neither an Eulerian path nor cycle exists",
        distractors=[
            "The graph was not connected",
            "There were too many bridges",
            "The graph was not planar"
        ]
    ),
    create_mc_question(
        id="topo_mod_011", topic="tsp",
        question="The Hamiltonian cycle problem is a special case of which well-known optimization problem?",
        correct="The Traveling Salesman Problem (TSP) — with all distances equal, finding a Hamiltonian cycle is equivalent to finding the shortest tour",
        distractors=[
            "The shortest path problem",
            "The minimum spanning tree problem",
            "The maximum flow problem"
        ]
    ),
    tf(
        id="topo_mod_012", topic="topology_rubber_sheet",
        question="Topology is sometimes called 'rubber sheet geometry' because metric relations (distances, angles) play no role — only spatial relations like connectivity and adjacency matter.",
        correct=True
    ),
]

# ============================================================
# TOPIC: graph_traversal (Lecture 08) — DEEP
# ============================================================
graph_traversal = [
    create_mc_question(
        id="trav_001", topic="traversal_definition",
        question="Graph traversal means:",
        correct="Visiting each vertex of a graph, performing an operation or collecting information from vertices with certain properties",
        distractors=[
            "Finding the shortest path between two vertices",
            "Removing all edges from the graph",
            "Sorting the vertices by their degree"
        ]
    ),
    create_mc_question(
        id="trav_002", topic="dfs",
        question="Depth First Search (DFS) is implemented as a recursive algorithm. At each vertex $v$, the algorithm:",
        correct="Marks $v$ as visited, then for each unvisited neighbor $n$, stores $v$ as parent of $n$ and recursively performs DFS on $n$",
        distractors=[
            "Marks $v$ as visited, adds all neighbors to a queue, then processes the queue",
            "Visits all neighbors of $v$ before moving deeper into the graph",
            "Marks $v$ as visited and moves to the neighbor with the highest degree"
        ]
    ),
    create_mc_question(
        id="trav_003", topic="bfs",
        question="Breadth First Search (BFS) uses which data structure to manage the vertices to be visited?",
        correct="A queue (FIFO: First In, First Out)",
        distractors=[
            "A stack (LIFO: Last In, First Out)",
            "A priority queue ordered by vertex degree",
            "A hash map of visited vertices"
        ]
    ),
    create_mc_question(
        id="trav_004", topic="bfs",
        question="In BFS, the algorithm starts by enqueuing the start vertex. Then, while the queue is not empty, it:",
        correct="Dequeues the next vertex $v$, marks it as visited, and enqueues all unvisited neighbors of $v$ that are not already in the queue",
        distractors=[
            "Dequeues the next vertex $v$ and recursively visits its deepest descendant",
            "Dequeues all vertices at once and processes them in parallel",
            "Dequeues the vertex with the smallest label"
        ]
    ),
    create_mc_question(
        id="trav_005", topic="dfs_vs_bfs",
        question="Which statement correctly distinguishes DFS from BFS?",
        correct="DFS explores as deep as possible along each branch before backtracking; BFS explores all neighbors at the current depth before going deeper",
        distractors=[
            "DFS uses a queue; BFS uses recursion",
            "DFS is always faster than BFS",
            "DFS finds shortest paths; BFS does not"
        ]
    ),
    create_mc_question(
        id="trav_006", topic="spanning_tree",
        question="Both DFS and BFS generate a spanning tree of the graph. What is a spanning tree?",
        correct="A connected, cycle-free subgraph $S = (V, E')$ that contains all vertices of $G$ — the minimal set of edges connecting all vertices",
        distractors=[
            "A subgraph containing all edges of $G$ but possibly fewer vertices",
            "A binary tree constructed from the graph's adjacency matrix",
            "The shortest path tree from every vertex to every other vertex"
        ]
    ),
    create_mc_question(
        id="trav_007", topic="bfs_shortest_path",
        question="The spanning tree generated by BFS has a special property. What is it?",
        correct="It provides the shortest path (fewest edges) from the root vertex to all other vertices, assuming all edge weights are equal",
        distractors=[
            "It has the minimum total edge weight among all spanning trees",
            "It is always a balanced binary tree",
            "It contains exactly one cycle"
        ]
    ),
    create_mc_question(
        id="trav_008", topic="queue_operations",
        question="The queue data structure supports four operations. Which operation adds a given element to the end of the queue?",
        correct="Enqueue",
        distractors=[
            "Dequeue",
            "Push",
            "Insert"
        ]
    ),
    create_mc_question(
        id="trav_009", topic="recursive_algorithm",
        question="A recursive algorithm solves a problem by calling itself with a smaller version of the same problem. In the factorial example $n! = n \\cdot (n-1)!$, what is the base case (termination condition)?",
        correct="$n = 0$, which returns 1",
        distractors=[
            "$n = 1$, which returns $n$",
            "$n < 0$, which returns 0",
            "When the call stack is full"
        ]
    ),
    tf(
        id="trav_010", topic="dfs",
        question="DFS is an iterative algorithm that uses a queue to manage vertices.",
        correct=False  # DFS is recursive (or uses a stack); BFS uses a queue
    ),
    create_mc_question(
        id="trav_011", topic="dfs_termination",
        question="In recursive DFS, the recursion terminates when:",
        correct="The current vertex has no unvisited neighbors — the algorithm returns to the previous vertex and continues with the next neighbor",
        distractors=[
            "The queue is empty",
            "All edges have been traversed",
            "A cycle is detected"
        ]
    ),
    tf(
        id="trav_012", topic="spanning_tree",
        question="A spanning tree of a connected graph with $n$ vertices always has exactly $n - 1$ edges.",
        correct=True
    ),
]

# ============================================================
# TOPIC: dijkstra (Lecture 09) — DEEP
# ============================================================
dijkstra = [
    create_mc_question(
        id="dijk_001", topic="weighted_graph",
        question="In a weighted graph, the weight of a path is defined as:",
        correct="The sum of the weights of all edges that belong to the path",
        distractors=[
            "The maximum weight among all edges in the path",
            "The number of edges in the path",
            "The product of all edge weights"
        ]
    ),
    create_mc_question(
        id="dijk_002", topic="shortest_path_variants",
        question="The single-source shortest path problem asks to find:",
        correct="The shortest path from one start vertex (source) to all other vertices in the graph",
        distractors=[
            "The shortest path between one specific pair of vertices",
            "The shortest paths between every pair of vertices",
            "The shortest path from all vertices to a single destination"
        ]
    ),
    create_mc_question(
        id="dijk_003", topic="dijkstra_init",
        question="In Dijkstra's algorithm, what is the initialization step?",
        correct="Set the distance of the starting vertex to 0 and the distances of all other vertices to $\\infty$; mark all vertices as unvisited; insert the start vertex into the priority queue with priority 0",
        distractors=[
            "Set all distances to 0 and mark all vertices as visited",
            "Set the distance of all vertices to 1 and the start vertex to 0",
            "Compute the distances between all pairs of adjacent vertices"
        ]
    ),
    create_mc_question(
        id="dijk_004", topic="relaxation",
        question="In Dijkstra's algorithm, 'distance relaxation' refers to:",
        correct="If a shorter path to vertex $n$ is found via vertex $v$ (i.e., $D(v) + w(v,n) < D(n)$), update $D(n)$ and set $v$ as parent of $n$",
        distractors=[
            "Removing edges that are too long from the graph",
            "Setting the distance of visited vertices to $\\infty$",
            "Reducing edge weights by a constant factor"
        ]
    ),
    create_mc_question(
        id="dijk_005", topic="dijkstra_selection",
        question="At each iteration of Dijkstra's algorithm, which vertex is selected as the current vertex?",
        correct="The unvisited vertex with the smallest distance value — extracted from the priority queue via extractMin()",
        distractors=[
            "The vertex with the most neighbors",
            "The vertex most recently added to the queue",
            "A random unvisited vertex"
        ]
    ),
    create_mc_question(
        id="dijk_006", topic="dijkstra_finality",
        question="Once a vertex is marked as visited (extracted from the priority queue) in Dijkstra's algorithm:",
        correct="Its distance value is final — no shorter path to this vertex will be found",
        distractors=[
            "Its distance may still be updated if a shorter path is found later",
            "It is removed from the graph",
            "All its neighbors are also marked as visited"
        ]
    ),
    create_mc_question(
        id="dijk_007", topic="dijkstra_single_pair",
        question="To solve the single-pair shortest path problem (from source $s$ to target $t$), Dijkstra's algorithm can be modified by:",
        correct="Adding a check after extractMin(): if the extracted vertex is $t$, break out of the while loop — the shortest path to $t$ is known",
        distractors=[
            "Running the algorithm in reverse from $t$ to $s$",
            "Only inserting vertex $t$ into the priority queue",
            "Removing all vertices except $s$ and $t$ from the graph"
        ]
    ),
    create_mc_question(
        id="dijk_008", topic="priority_queue",
        question="In Dijkstra's algorithm, the priority queue stores vertices with their current distance as priority. The decreaseKey operation is needed when:",
        correct="A shorter path to a vertex already in the queue is found during relaxation — its priority must be updated",
        distractors=[
            "A vertex is first discovered and added to the queue",
            "A vertex is extracted from the queue",
            "The algorithm terminates"
        ]
    ),
    create_mc_question(
        id="dijk_009", topic="priority_queue",
        question="In a priority queue implemented as a heap, the operations insert() and extractMin() have a runtime of:",
        correct="$O(\\log n)$, where $n$ is the number of elements in the priority queue",
        distractors=[
            "$O(1)$ — constant time",
            "$O(n)$ — linear time",
            "$O(n^2)$ — quadratic time"
        ]
    ),
    tf(
        id="dijk_010", topic="dijkstra_negative",
        question="Dijkstra's algorithm works correctly even when some edge weights are negative.",
        correct=False  # Dijkstra requires non-negative edge weights
    ),
    create_mc_question(
        id="dijk_011", topic="shortest_path_unweighted",
        question="For finding shortest paths in an unweighted graph (all edges have equal weight), which algorithm is sufficient?",
        correct="Breadth First Search (BFS) — it naturally finds the shortest path in terms of number of edges",
        distractors=[
            "Depth First Search (DFS)",
            "Dijkstra's algorithm is the only option",
            "Kruskal's algorithm"
        ]
    ),
    create_mc_question(
        id="dijk_012", topic="shortest_path_recovery",
        question="After running Dijkstra's algorithm, how is the actual shortest path from source $s$ to target $t$ recovered?",
        correct="Follow the parent pointers from $t$ back to $s$, then reverse the sequence",
        distractors=[
            "The path is stored directly in the priority queue",
            "Re-run the algorithm from $t$ to $s$",
            "Read the edges in the order they were relaxed"
        ]
    ),
    create_mc_question(
        id="dijk_013", topic="dijkstra_trace",
        question="Consider a graph where vertex A (source) connects to C (weight 1), D (weight 5), and E (weight 9). After initializing and processing vertex A, which vertex is processed next?",
        correct="C — it has the smallest distance value (1) among unvisited vertices",
        distractors=[
            "D — it is the next alphabetically",
            "E — it has the largest weight",
            "A is processed again to verify distances"
        ]
    ),
    create_mc_question(
        id="dijk_014", topic="single_destination",
        question="The single-destination shortest path problem (shortest paths from all vertices to one destination) can be solved for undirected graphs by:",
        correct="Running the single-source shortest path algorithm with the destination vertex as the source",
        distractors=[
            "Running Dijkstra from every vertex separately",
            "Using BFS from the destination but only on directed edges",
            "This problem has no efficient solution"
        ]
    ),
]

# ============================================================
# TOPIC: minimum_spanning_trees (Lecture 10a) — DEEP
# ============================================================
minimum_spanning_trees = [
    create_mc_question(
        id="mst_001", topic="spanning_tree_def",
        question="A spanning tree of a connected graph $G$ is:",
        correct="A subgraph that contains all vertices of $G$, is connected, and is cycle-free",
        distractors=[
            "A subgraph containing all edges of $G$ and no cycles",
            "Any connected subgraph of $G$",
            "The shortest path tree from a specific source vertex"
        ]
    ),
    create_mc_question(
        id="mst_002", topic="mst_def",
        question="A minimum spanning tree (MST) of a weighted graph is the spanning tree where:",
        correct="The sum of the weights of its edges is minimal among all possible spanning trees",
        distractors=[
            "The maximum edge weight is minimized",
            "The number of edges is minimized",
            "The longest path between any two vertices is minimized"
        ]
    ),
    create_mc_question(
        id="mst_003", topic="kruskal",
        question="Kruskal's algorithm builds a minimum spanning tree by:",
        correct="Starting with all vertices as separate trees (forest), then repeatedly adding the lowest-weight edge that connects two different trees",
        distractors=[
            "Starting from a single vertex and greedily adding the nearest unvisited vertex",
            "Finding the shortest path between every pair of vertices",
            "Removing the heaviest edges one by one until a tree remains"
        ]
    ),
    create_mc_question(
        id="mst_004", topic="kruskal",
        question="In Kruskal's algorithm, when an edge is removed from the priority queue, it is discarded if:",
        correct="Both endpoints belong to the same tree (adding it would create a cycle)",
        distractors=[
            "Its weight exceeds the average edge weight",
            "One of its endpoints has already been visited",
            "The edge is longer than the previously added edge"
        ]
    ),
    create_mc_question(
        id="mst_005", topic="kruskal_early_termination",
        question="Kruskal's algorithm can terminate early when the spanning tree has been found. For a graph with $m$ vertices, how many edges does the MST contain?",
        correct="$m - 1$ edges",
        distractors=[
            "$m$ edges",
            "$m + 1$ edges",
            "$2m - 1$ edges"
        ]
    ),
    create_mc_question(
        id="mst_006", topic="union_find",
        question="Kruskal's algorithm uses the disjoint-set (union-find) data structure. What are its three core operations?",
        correct="makeSet (initialize sets), find (return canonical element of a set), and union (merge two sets)",
        distractors=[
            "insert, delete, and search",
            "push, pop, and peek",
            "enqueue, dequeue, and contains"
        ]
    ),
    create_mc_question(
        id="mst_007", topic="union_find",
        question="In a tree-based implementation of union-find, the find operation returns the canonical element by:",
        correct="Traversing parent pointers from the given element up to the root of its tree",
        distractors=[
            "Searching a hash table for the element's set ID",
            "Comparing the element with all other elements",
            "Returning the element with the smallest value in the set"
        ]
    ),
    create_mc_question(
        id="mst_008", topic="path_compression",
        question="Path compression is an optimization for the union-find data structure. What does it do?",
        correct="During a find operation, every traversed vertex is re-linked directly to the root, flattening the tree for faster future lookups",
        distractors=[
            "It compresses the graph by removing redundant edges",
            "It shortens all paths in the MST",
            "It reduces the weight of the heaviest edge in each union"
        ]
    ),
    create_mc_question(
        id="mst_009", topic="connected_components",
        question="A connected component of an undirected graph is:",
        correct="A subgraph in which every pair of vertices is connected by a path, and which is maximal (no additional vertices can be added while maintaining connectivity)",
        distractors=[
            "Any subgraph that contains a cycle",
            "A vertex and all its immediate neighbors",
            "The set of all vertices with the same degree"
        ]
    ),
    create_mc_question(
        id="mst_010", topic="forest",
        question="In graph theory, a forest is defined as:",
        correct="An undirected graph without any cycles (an acyclic graph) — its connected components are trees",
        distractors=[
            "A graph where every vertex has degree ≤ 2",
            "A connected graph with exactly one cycle",
            "A directed acyclic graph (DAG)"
        ]
    ),
    create_mc_question(
        id="mst_011", topic="kruskal_disconnected",
        question="If Kruskal's algorithm is applied to a graph that is not connected, the result is:",
        correct="A minimum spanning forest — the union of MSTs for each connected component",
        distractors=[
            "An error — the algorithm only works on connected graphs",
            "A single tree with additional disconnected vertices",
            "A minimum spanning tree with infinite-weight edges bridging components"
        ]
    ),
    create_mc_question(
        id="mst_012", topic="priority_queue",
        question="In Kruskal's algorithm, the priority queue stores edges ordered by their weight. The extractMin operation returns:",
        correct="The edge with the smallest weight, removing it from the queue",
        distractors=[
            "The edge with the largest weight",
            "A random edge",
            "The edge most recently inserted"
        ]
    ),
    tf(
        id="mst_013", topic="kruskal_dual",
        question="Kruskal described a 'dual method' for finding an MST: among the edges not yet chosen, repeatedly remove the longest edge whose removal will not disconnect the graph.",
        correct=True
    ),
    create_mc_question(
        id="mst_014", topic="subgraph",
        question="A graph $G' = (V', E')$ is a subgraph of $G = (V, E)$ if:",
        correct="$V' \\subseteq V$ and $E' \\subseteq E$",
        distractors=[
            "$V' = V$ and $E' \\subseteq E$",
            "$V' \\subseteq V$ and $E' = E$",
            "$|V'| < |V|$ and $|E'| < |E|$"
        ]
    ),
]

# ============================================================
# TOPIC: search_trees (Lecture 10b) — DEEP
# ============================================================
search_trees = [
    create_mc_question(
        id="stree_001", topic="binary_tree",
        question="A complete tree of order $k$ is one where every vertex has either 0 or $k$ successors. A binary tree has order:",
        correct="$k = 2$ — all interior vertices have exactly 2 children",
        distractors=[
            "$k = 1$ — each vertex has at most 1 child",
            "$k = 3$ — each vertex has at most 3 children",
            "$k = n$ — where $n$ is the number of vertices"
        ]
    ),
    create_mc_question(
        id="stree_002", topic="tree_terminology",
        question="The depth of a vertex $v$ in a tree is defined as:",
        correct="The number of edges along the path from the root to vertex $v$",
        distractors=[
            "The number of edges along the longest path from $v$ to a leaf",
            "The total number of descendants of $v$",
            "The number of siblings of $v$"
        ]
    ),
    create_mc_question(
        id="stree_003", topic="tree_terminology",
        question="The height of a tree is defined as:",
        correct="The height of the root, which equals the number of edges along the longest path from the root to any leaf",
        distractors=[
            "The total number of vertices in the tree",
            "The number of leaf nodes",
            "The maximum degree of any vertex"
        ]
    ),
    create_mc_question(
        id="stree_004", topic="bst_property",
        question="A binary search tree (BST) satisfies the following ordering property for every subtree $T' = (T_l, y, T_r)$:",
        correct="All values in the left subtree $T_l$ are less than $y$, and all values in the right subtree $T_r$ are greater than or equal to $y$",
        distractors=[
            "All values in $T_l$ are greater than $y$, and all values in $T_r$ are less than $y$",
            "The left subtree has fewer nodes than the right subtree",
            "Each node value is greater than its parent's value"
        ]
    ),
    create_mc_question(
        id="stree_005", topic="bst_insert",
        question="When inserting a new element into a binary search tree, the algorithm:",
        correct="Recursively traverses the tree from root to a leaf position, comparing keys at each step, and inserts at the first empty child position",
        distractors=[
            "Inserts the element at the root and pushes everything else down",
            "Finds the node with the closest value and inserts as its sibling",
            "Adds the element to a queue and rebalances the tree"
        ]
    ),
    create_mc_question(
        id="stree_006", topic="bst_delete",
        question="Deleting an interior vertex with two children from a binary search tree is handled by:",
        correct="Replacing the vertex with the smallest vertex in its right subtree (the next greater or equal vertex)",
        distractors=[
            "Simply removing the vertex and reconnecting its children to the parent",
            "Replacing it with the largest vertex in the left subtree only",
            "Removing the vertex and reinserting all its descendants"
        ]
    ),
    create_mc_question(
        id="stree_007", topic="bst_delete",
        question="Deleting an interior vertex with exactly one child from a BST is done by:",
        correct="Replacing the vertex with its single child, regardless of whether it is a left or right child",
        distractors=[
            "Replacing the vertex with the smallest element in the tree",
            "Removing both the vertex and its child",
            "Swapping the vertex with its parent"
        ]
    ),
    create_mc_question(
        id="stree_008", topic="balanced_tree",
        question="A balanced binary tree with $N$ vertices has a height of:",
        correct="$h = \\log_2(N+1) - 1$",
        distractors=[
            "$h = N - 1$",
            "$h = N / 2$",
            "$h = \\sqrt{N}$"
        ]
    ),
    create_mc_question(
        id="stree_009", topic="balanced_tree",
        question="Why are balanced search trees important?",
        correct="They guarantee $O(\\log n)$ search time by limiting the tree height to approximately $\\log(n)$",
        distractors=[
            "They use less memory than unbalanced trees",
            "They allow duplicate keys",
            "They can store more elements than unbalanced trees"
        ]
    ),
    create_mc_question(
        id="stree_010", topic="unbalanced_worst_case",
        question="If an ordered sequence of increasing elements is inserted into a standard (non-balancing) BST, the resulting tree has:",
        correct="Height equal to $n - 1$ (a degenerate chain), giving worst-case $O(n)$ search time — no better than a linear search",
        distractors=[
            "Height $\\log_2(n)$ — the tree remains balanced",
            "Two branches of equal height",
            "Height 1 — all elements become leaves"
        ]
    ),
    create_mc_question(
        id="stree_011", topic="2_3_tree",
        question="A 2-3 search tree differs from a binary search tree in that:",
        correct="Nodes can hold 1 key (2-node with 2 links) or 2 keys (3-node with 3 links), and the tree is always perfectly balanced",
        distractors=[
            "Each node holds exactly 3 keys",
            "It is a binary tree with at most 3 levels",
            "Only leaf nodes store keys; interior nodes store links"
        ]
    ),
    create_mc_question(
        id="stree_012", topic="2_3_tree_insert",
        question="When inserting a key into a 2-3 tree and the target leaf is a 3-node (already full with 2 keys), what happens?",
        correct="A temporary 4-node is created, then split: the middle key is pushed up to the parent, and the left and right keys become separate 2-nodes",
        distractors=[
            "The key is inserted into the next available 2-node",
            "The 3-node is expanded to hold 3 keys permanently",
            "The tree is rebuilt from scratch"
        ]
    ),
    create_mc_question(
        id="stree_013", topic="2_3_tree_insert",
        question="In a 2-3 tree, inserting a new key into a 2-node (a node with only 1 key) is straightforward:",
        correct="The 2-node is replaced with a 3-node, with the new key placed before or after the existing key based on value",
        distractors=[
            "A new child node is created below the 2-node",
            "The 2-node is split into two 2-nodes",
            "The key is inserted at the root"
        ]
    ),
    create_mc_question(
        id="stree_014", topic="2_3_tree_growth",
        question="A 2-3 search tree grows in an unusual way. How does its height increase?",
        correct="It only grows upward — when a split propagates to the root and the root is split, a new root is created, increasing the height by one",
        distractors=[
            "New levels are added at the bottom when leaves overflow",
            "The tree is restructured and rebalanced after every insertion",
            "The height increases by one after every $n$ insertions"
        ]
    ),
    create_mc_question(
        id="stree_015", topic="2_3_tree_properties",
        question="All splitting transformations in a 2-3 tree are local, meaning:",
        correct="Only the 4-node and its parent need to be examined and modified — yet the global properties (ordered, balanced, equal path lengths) are preserved",
        distractors=[
            "The entire tree must be rebalanced after each split",
            "Only leaf nodes can be split",
            "Splits only happen at the root"
        ]
    ),
    tf(
        id="stree_016", topic="2_3_tree_search",
        question="Searching in a 2-3 tree works like a BST: compare the search key against node keys and follow the appropriate link. If a null link is reached, the key is not in the tree.",
        correct=True
    ),
    create_mc_question(
        id="stree_017", topic="bst_search",
        question="The search algorithm in a BST has a time complexity of $O(\\log n)$ in the best case (balanced tree) and $O(n)$ in the worst case (degenerate tree). What operation achieves $O(\\log n)$ in a 2-3 tree regardless of insertion order?",
        correct="Search — because the 2-3 tree is always perfectly balanced, the path from root to any leaf has the same length",
        distractors=[
            "Only insertion is guaranteed $O(\\log n)$; search may be slower",
            "Deletion — the tree is only balanced after deletions",
            "No operation is guaranteed $O(\\log n)$ in a 2-3 tree"
        ]
    ),
]

# ============================================================
# TOPIC: kd_tree (Lecture 11) — DEEP
# ============================================================
kd_tree = [
    create_mc_question(
        id="kd_001", topic="kd_motivation",
        question="The KD-Tree is designed to efficiently answer which types of spatial queries on point collections?",
        correct="Window queries (points in a rectangular region), k-nearest neighbor queries, and ball/fixed-radius queries",
        distractors=[
            "Only exact point lookup by coordinates",
            "Only range queries on 1D data",
            "Only polygon containment queries"
        ]
    ),
    create_mc_question(
        id="kd_002", topic="kd_structure",
        question="A KD-Tree is fundamentally a:",
        correct="Binary search tree that recursively partitions multi-dimensional point sets by splitting along alternating dimensions",
        distractors=[
            "Balanced ternary tree for 3D data",
            "A hash table with spatial buckets",
            "A quad-tree generalized to arbitrary dimensions"
        ]
    ),
    create_mc_question(
        id="kd_003", topic="kd_construction",
        question="When constructing a KD-Tree for 2D points, the set $P$ is recursively partitioned by:",
        correct="Splitting alternately along $x$ and $y$ dimensions, using the median coordinate value to ensure roughly equal-sized subsets",
        distractors=[
            "Always splitting along the $x$-axis",
            "Splitting along the dimension with the largest range of values",
            "Randomly choosing a split dimension and value"
        ]
    ),
    create_mc_question(
        id="kd_004", topic="kd_median",
        question="Why is the median used as the splitting value in KD-Tree construction?",
        correct="It ensures that the two resulting subsets $P_1$ and $P_2$ are approximately the same size, keeping the tree balanced",
        distractors=[
            "The median is the fastest value to compute",
            "The median minimizes the total distance between points",
            "Any value would work equally well"
        ]
    ),
    create_mc_question(
        id="kd_005", topic="kd_partitioning",
        question="In a 2D KD-Tree, the partitioning values ($l_x$ and $l_y$) can be interpreted geometrically as:",
        correct="Axis-aligned straight lines that divide the space into two rectangular half-spaces",
        distractors=[
            "Circles centered at the median point",
            "Diagonal lines at 45 degrees",
            "Arbitrary curves that separate point clusters"
        ]
    ),
    create_mc_question(
        id="kd_006", topic="kd_termination",
        question="The recursive partitioning in KD-Tree construction terminates when:",
        correct="The subset $P$ contains only one point, or a pre-defined minimum number of points that will be queried sequentially",
        distractors=[
            "A maximum tree depth is reached",
            "All points have been assigned to leaf nodes regardless of subset size",
            "The splitting line passes through a point"
        ]
    ),
    create_mc_question(
        id="kd_007", topic="window_query",
        question="A window query on a KD-Tree finds all points within a rectangular region $W$. Starting from the root, the algorithm recursively tests the relation between $W$ and the region $R$ of each node. If $R$ is completely within $W$:",
        correct="All points of the subtree are added to the result set without further recursion",
        distractors=[
            "Only the root point of the subtree is added",
            "The subtree is searched further to verify each point",
            "The subtree is pruned and its points are discarded"
        ]
    ),
    create_mc_question(
        id="kd_008", topic="window_query",
        question="During a KD-Tree window query, if region $R$ of a node intersects (overlaps) the query window $W$ but is not fully contained:",
        correct="Both the left and right subtrees must be searched recursively",
        distractors=[
            "Only the subtree closer to the center of $W$ is searched",
            "The node's point is added and recursion stops",
            "The subtree is skipped entirely"
        ]
    ),
    create_mc_question(
        id="kd_009", topic="window_query",
        question="During a KD-Tree window query, if region $R$ is completely disjoint from the query window $W$:",
        correct="No further action is required — the recursion is aborted for this branch",
        distractors=[
            "All points in $R$ are added to the result",
            "The algorithm switches to a brute-force search",
            "The parent node's region is re-checked"
        ]
    ),
    create_mc_question(
        id="kd_010", topic="window_query",
        question="When a leaf node is reached during a KD-Tree window query, what happens?",
        correct="Each point in the leaf's region is individually tested to check if it lies inside the query window, and matching points are added to the result set",
        distractors=[
            "All points are automatically added since the leaf was reached",
            "The leaf is split further until each point is in its own region",
            "The algorithm returns to the root and starts over"
        ]
    ),
    create_mc_question(
        id="kd_011", topic="kd_vs_bst",
        question="How does a KD-Tree differ from a standard 1D binary search tree?",
        correct="A KD-Tree operates on multi-dimensional data by alternating the comparison dimension at each tree level, whereas a BST compares on a single key",
        distractors=[
            "A KD-Tree is always balanced; a BST is never balanced",
            "A KD-Tree stores data only in leaf nodes; a BST stores data in all nodes",
            "There is no meaningful difference"
        ]
    ),
    tf(
        id="kd_012", topic="kd_assumption",
        question="For the KD-Tree construction presented in the lectures, it is assumed that all $x$-coordinates and all $y$-coordinates of the points are different.",
        correct=True
    ),
    create_mc_question(
        id="kd_013", topic="kd_complexity",
        question="The KD-Tree is efficient for spatial queries because it prunes large portions of the search space. For a window query, what is the key efficiency gain?",
        correct="When a node's region is completely inside or completely disjoint from the query window, entire subtrees can be included or excluded without visiting individual points",
        distractors=[
            "The tree is always perfectly balanced regardless of point distribution",
            "Every query visits exactly $\\log n$ nodes",
            "The tree stores precomputed distances between all pairs of points"
        ]
    ),
]

# ============================================================
# Write all topic files
# ============================================================
print("Generating GIS quiz questions:")
write_topic("introduction", introduction)
write_topic("thematic_modeling", thematic_modeling)
write_topic("geometric_modeling", geometric_modeling)
write_topic("spatial_overlays", spatial_overlays)
write_topic("topological_data_structures", topological_data_structures)
write_topic("topological_modeling", topological_modeling)
write_topic("graph_traversal", graph_traversal)
write_topic("dijkstra", dijkstra)
write_topic("minimum_spanning_trees", minimum_spanning_trees)
write_topic("search_trees", search_trees)
write_topic("kd_tree", kd_tree)

# Summary
all_topics = [
    introduction, thematic_modeling, geometric_modeling, spatial_overlays,
    topological_data_structures, topological_modeling, graph_traversal,
    dijkstra, minimum_spanning_trees, search_trees, kd_tree
]
total = sum(len(t) for t in all_topics)
print(f"\nTotal: {total} questions across {len(all_topics)} topics")
