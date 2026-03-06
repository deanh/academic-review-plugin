#!/usr/bin/env python3
"""Generate additional geodatabases quiz questions for topics needing deeper coverage."""

import json
from pathlib import Path
from quiz_utils import create_mc_question

OUTPUT_DIR = Path(__file__).parent.parent / "server" / "data" / "questions" / "geodatabases"


def tf(id, question, correct, topic):
    return {"id": id, "type": "true_false", "question": question, "correct": correct, "topic": topic}


def append_to_topic(filename, new_questions):
    path = OUTPUT_DIR / f"{filename}.json"
    existing = json.loads(path.read_text())
    existing.extend(new_questions)
    path.write_text(json.dumps(existing, indent=2))
    print(f"  {filename}: added {len(new_questions)} → total {len(existing)}")


# ============================================================
# ADDITIONAL: simple_features (deeper coverage)
# ============================================================
sf_extra = [
    create_mc_question(
        id="sf_016", topic="geometry_hierarchy",
        question="In the OGC Simple Feature model, which of the following is an abstract class that cannot be instantiated directly?",
        correct="Curve — it is an abstract superclass; LineString is the concrete subclass",
        distractors=[
            "Point — all point geometries are abstract",
            "Polygon — only MultiPolygon can be instantiated",
            "LineString — it must be subclassed further"
        ]
    ),
    create_mc_question(
        id="sf_017", topic="line_types",
        question="What distinguishes a Line from a LineString in the Simple Feature model?",
        correct="A Line is a LineString with exactly 2 points",
        distractors=[
            "A Line can have curves; a LineString cannot",
            "A Line is always closed; a LineString is always open",
            "They are the same thing"
        ]
    ),
    create_mc_question(
        id="sf_018", topic="coordinate_dimension",
        question="A geometry has coordinates (x, y, m). What are its coordinateDimension and spatialDimension?",
        correct="coordinateDimension = 3, spatialDimension = 2 (the m coordinate is not a spatial dimension)",
        distractors=[
            "coordinateDimension = 2, spatialDimension = 2",
            "coordinateDimension = 3, spatialDimension = 3",
            "coordinateDimension = 2, spatialDimension = 3"
        ]
    ),
    create_mc_question(
        id="sf_019", topic="boundary",
        question="What is the boundary of a closed curve (a curve whose start and end point are the same)?",
        correct="The boundary is empty",
        distractors=[
            "The boundary consists of the start point only",
            "The boundary is the set of all points on the curve",
            "The boundary consists of the start and end points"
        ]
    ),
    create_mc_question(
        id="sf_020", topic="boundary",
        question="What is the boundary of a non-closed LineString?",
        correct="The two endpoints (start point and end point)",
        distractors=[
            "All points on the LineString",
            "The boundary is empty",
            "The midpoint of the LineString"
        ]
    ),
    create_mc_question(
        id="sf_021", topic="valid_polygons",
        question="Which of the following is NOT a valid polygon according to the Simple Feature specification?",
        correct="A polygon whose exterior ring and interior ring cross each other at two points",
        distractors=[
            "A polygon with no interior rings (holes)",
            "A polygon whose exterior and interior rings touch at exactly one point",
            "A polygon with three interior rings"
        ]
    ),
    create_mc_question(
        id="sf_022", topic="multipolygon",
        question="In the Simple Feature model, what constraint applies to the elements of a MultiPolygon?",
        correct="The polygon elements must be disjoint (their interiors must not intersect)",
        distractors=[
            "All polygons must share at least one boundary point",
            "All polygons must have the same number of rings",
            "The polygons must be ordered by area"
        ]
    ),
    create_mc_question(
        id="sf_023", topic="wkt",
        question="What does the following WKT represent? MULTIPOLYGON(((0 0, 0 20, 20 20, 20 0, 0 0),(5 5, 5 15, 15 15, 15 5, 5 5)),((30 30, 30 40, 40 40, 40 30, 30 30)))",
        correct="Two polygons: the first has an exterior ring and one hole, the second is a simple polygon",
        distractors=[
            "One polygon with two exterior rings",
            "Two separate polygons, each with one hole",
            "A single polygon with two holes"
        ]
    ),
    create_mc_question(
        id="sf_024", topic="feature",
        question="In the OGC Simple Feature specification, what is a 'feature'?",
        correct="An abstraction of a real-world phenomenon (geo-object), stored as a dataset in a feature table",
        distractors=[
            "A method that operates on geometry data",
            "A spatial reference system definition",
            "A type of spatial index"
        ]
    ),
    create_mc_question(
        id="sf_025", topic="simple_feature_limits",
        question="The OGC Simple Feature Access standard has specific limitations. Which of the following is a limitation?",
        correct="It only models 0- to 2-dimensional shapes with linear interpolation between points, and has no explicit topology representation",
        distractors=[
            "It cannot store point geometries",
            "It requires 3D coordinates for all geometry types",
            "It only supports Oracle Spatial, not PostGIS"
        ]
    ),
    tf(
        id="sf_026", topic="polygon_interior",
        question="According to the Simple Feature specification, the interior of every valid polygon must be a connected point set.",
        correct=True
    ),
    tf(
        id="sf_027", topic="polygon_exterior",
        question="The exterior of a polygon with one or more holes is a connected point set.",
        correct=False
    ),
    create_mc_question(
        id="sf_028", topic="iso_sqlmm",
        question="The ISO SQL/MM Spatial standard introduces additional geometry types not found in the OGC Simple Feature model. Which of the following is an example?",
        correct="ST_CircularString — a curve type composed of circular arc segments",
        distractors=[
            "ST_Point — a basic point geometry",
            "ST_Polygon — a planar surface with rings",
            "ST_MultiPoint — a collection of points"
        ]
    ),
    create_mc_question(
        id="sf_029", topic="spatial_query",
        question="Given tables 'cities' (with geometry column) and 'states' (with geometry column), which query finds cities that are neighbours of 'Paunzhausen' (share a boundary)?",
        correct="SELECT c2.name FROM cities c1 JOIN cities c2 ON c1.name='Paunzhausen' AND ST_Touches(c1.geometry, c2.geometry);",
        distractors=[
            "SELECT name FROM cities WHERE ST_Touches(geometry, 'Paunzhausen');",
            "SELECT name FROM cities WHERE geometry = 'Paunzhausen';",
            "SELECT c2.name FROM cities c1, cities c2 WHERE ST_Distance(c1.geometry, c2.geometry) = 0;"
        ]
    ),
    create_mc_question(
        id="sf_030", topic="convex_hull",
        question="The convexHull() method returns the smallest convex geometry that contains a given geometry. For a simple convex polygon, what does convexHull() return?",
        correct="The polygon itself, since it is already convex",
        distractors=[
            "The bounding box of the polygon",
            "A circle enclosing the polygon",
            "An empty geometry"
        ]
    ),
]

# ============================================================
# ADDITIONAL: sql_basics — deeper JOINs coverage
# ============================================================
joins_extra = [
    create_mc_question(
        id="sql_021", topic="inner_join",
        question="Given a 'teacher' table with ids (1,2,3) and a 'course' table with teacher foreign keys (1,3,4), an INNER JOIN on teacher.id = course.teacher returns:",
        correct="Only 2 rows — for teacher ids 1 and 3, because only those have matches in both tables",
        distractors=[
            "3 rows — one for each teacher",
            "3 rows — one for each course",
            "4 rows — including NULL for non-matching entries"
        ]
    ),
    create_mc_question(
        id="sql_022", topic="left_join",
        question="Using the same tables (teacher ids 1,2,3 and course teacher foreign keys 1,3,4), a LEFT JOIN from teacher to course returns:",
        correct="3 rows — teachers 1 and 3 with their courses, and teacher 2 (Hubble) with NULL course values",
        distractors=[
            "2 rows — only matching teachers",
            "4 rows — including the course with teacher=4",
            "3 rows — but teacher 2 is excluded"
        ]
    ),
    create_mc_question(
        id="sql_023", topic="right_join",
        question="A RIGHT JOIN from teacher to course (with teacher ids 1,2,3 and course teacher keys 1,3,4) returns:",
        correct="3 rows — courses with teacher 1 and 3 showing teacher data, and the course with teacher=4 showing NULL for teacher columns",
        distractors=[
            "2 rows — only matching entries",
            "3 rows — all teachers with NULL courses where no match",
            "4 rows — all possible combinations"
        ]
    ),
    create_mc_question(
        id="sql_024", topic="full_join",
        question="A FULL JOIN between teacher (ids 1,2,3) and course (teacher keys 1,3,4) returns:",
        correct="4 rows — matched pairs for 1 and 3, plus teacher 2 with NULL course, plus the course with teacher=4 and NULL teacher",
        distractors=[
            "2 rows — only matches",
            "3 rows — just the teacher side",
            "9 rows — the Cartesian product"
        ]
    ),
    create_mc_question(
        id="sql_025", topic="cross_join",
        question="A CROSS JOIN between a table with 3 rows and a table with 4 rows produces how many result rows?",
        correct="12 — the Cartesian product (3 × 4)",
        distractors=[
            "7 — the sum (3 + 4)",
            "3 — the minimum of both",
            "4 — the maximum of both"
        ]
    ),
    create_mc_question(
        id="sql_026", topic="cross_join",
        question="What is a practical use case for a CROSS JOIN with spatial data?",
        correct="Computing pairwise distances between all points in a table by combining every point with every other point",
        distractors=[
            "Finding matching records between two tables",
            "Filtering rows based on a spatial predicate",
            "Removing duplicate geometries"
        ]
    ),
    create_mc_question(
        id="sql_027", topic="join_syntax",
        question="In PostgreSQL, if you write just JOIN (without specifying the type), which join is performed by default?",
        correct="INNER JOIN",
        distractors=["LEFT JOIN", "FULL JOIN", "CROSS JOIN"]
    ),
    create_mc_question(
        id="sql_028", topic="join_on",
        question="The ON clause in a JOIN specifies:",
        correct="The condition that determines which rows from the two tables are matched together",
        distractors=[
            "Which columns to display in the result",
            "The order of the result rows",
            "Which table is the left table"
        ]
    ),
    create_mc_question(
        id="sql_029", topic="join_null",
        question="In a LEFT JOIN result, NULL values appear in the right table's columns when:",
        correct="A row in the left table has no matching row in the right table",
        distractors=[
            "The left table contains NULL values",
            "The right table is empty",
            "The join condition uses an inequality"
        ]
    ),
    create_mc_question(
        id="sql_030", topic="join_commutative",
        question="Which of the following join types are commutative (A JOIN B gives the same result as B JOIN A)?",
        correct="INNER JOIN, FULL JOIN, and CROSS JOIN are commutative; LEFT and RIGHT JOIN are not",
        distractors=[
            "All join types are commutative",
            "Only CROSS JOIN is commutative",
            "No join types are commutative"
        ]
    ),
    create_mc_question(
        id="sql_031", topic="junction_table",
        question="A many-to-many relationship between 'student' and 'course' tables requires:",
        correct="A junction table (e.g., 'enrollment') containing foreign keys referencing both student and course primary keys",
        distractors=[
            "Adding a foreign key column to the student table",
            "Adding a foreign key column to the course table",
            "Using a CROSS JOIN in every query"
        ]
    ),
    tf(
        id="sql_032", topic="left_right_join",
        question="A LEFT JOIN from table A to table B produces the same result as a RIGHT JOIN from table B to table A.",
        correct=True
    ),
    create_mc_question(
        id="sql_033", topic="self_join",
        question="A self-join is when a table is joined to itself. Which syntax correctly finds all pairs of students from the same city?",
        correct="SELECT s1.name, s2.name FROM student s1 JOIN student s2 ON s1.city = s2.city AND s1.id < s2.id;",
        distractors=[
            "SELECT name FROM student WHERE city = city;",
            "SELECT * FROM student SELF JOIN student ON city;",
            "SELECT s1.name FROM student s1 WHERE s1.city IN (SELECT city FROM student);"
        ]
    ),
]

# ============================================================
# ADDITIONAL: spatial_indexing (R-Trees deeper)
# ============================================================
rtree_extra = [
    create_mc_question(
        id="rtree_013", topic="rtree_characteristics",
        question="An R-Tree subdivides the search space in a way that is fundamentally different from a B-tree. What is this key characteristic?",
        correct="Non-disjunctive subdivision — bounding boxes of sibling nodes can overlap",
        distractors=[
            "Disjunctive subdivision — each point belongs to exactly one node",
            "Linear subdivision — the space is split into equal strips",
            "Hierarchical subdivision — each level doubles the number of nodes"
        ]
    ),
    create_mc_question(
        id="rtree_014", topic="point_query",
        question="During a point query in an R-Tree, the algorithm traverses from root to leaves. At an internal node, what happens if the query point falls in the 'dead space' (inside the parent's bounding box but not inside any child's bounding box)?",
        correct="The search in that subtree ends — no child needs to be visited",
        distractors=[
            "All children are visited as a fallback",
            "The nearest child is visited",
            "The query reports an error"
        ]
    ),
    create_mc_question(
        id="rtree_015", topic="point_query",
        question="During a point query in an R-Tree, if the query point falls inside the bounding boxes of multiple children at an internal node, what happens?",
        correct="All children whose bounding box contains the point must be visited — multiple subtrees may need to be searched",
        distractors=[
            "Only the first matching child is visited",
            "The child with the smallest bounding box is visited",
            "An error occurs because points can only be in one bounding box"
        ]
    ),
    create_mc_question(
        id="rtree_016", topic="insertion",
        question="When inserting a new object into an R-Tree, how is the target leaf node selected?",
        correct="Starting from the root, at each level choose the child whose bounding box needs to be enlarged the least to contain the new object",
        distractors=[
            "Always insert into the leftmost leaf node",
            "Choose the child with the most free space",
            "Randomly select a leaf node"
        ]
    ),
    create_mc_question(
        id="rtree_017", topic="overflow",
        question="When an R-Tree node overflows (more than M entries after insertion), what happens?",
        correct="The node is split into two nodes, each receiving at least m entries, and the parent node is updated (split may propagate upward)",
        distractors=[
            "The oldest entry is removed",
            "The tree is rebuilt from scratch",
            "The entry is placed in an overflow buffer"
        ]
    ),
    create_mc_question(
        id="rtree_018", topic="overflow",
        question="If a node split during R-Tree insertion propagates all the way to the root, what happens?",
        correct="The root is split and a new root is created, increasing the tree height by one level",
        distractors=[
            "The insertion is rejected",
            "The tree is rebalanced without adding a level",
            "The oldest entries at the root level are removed"
        ]
    ),
    create_mc_question(
        id="rtree_019", topic="deletion",
        question="After deleting an entry from an R-Tree, if a node has fewer than m entries (underflow), the remaining entries are handled by:",
        correct="Removing the underfull node, then reinserting its remaining entries at the same level they previously belonged to",
        distractors=[
            "Merging the node with a sibling",
            "Leaving the node with fewer than m entries",
            "Moving entries to the parent node"
        ]
    ),
    create_mc_question(
        id="rtree_020", topic="deletion",
        question="During R-Tree deletion and reinsertion of orphaned entries, why must entries be reinserted at the same tree level they originally belonged to?",
        correct="Because internal node entries represent subtrees, not individual objects — inserting them at the wrong level would corrupt the tree structure",
        distractors=[
            "It is just a convention with no technical reason",
            "Because all entries must be in leaf nodes",
            "To ensure the tree remains unbalanced"
        ]
    ),
    create_mc_question(
        id="rtree_021", topic="window_query",
        question="During a window query in an R-Tree, at each internal node the algorithm checks which children's bounding boxes:",
        correct="Intersect or lie within the query rectangle Q",
        distractors=[
            "Are completely contained within Q",
            "Contain Q completely",
            "Have the same area as Q"
        ]
    ),
    create_mc_question(
        id="rtree_022", topic="rtree_performance",
        question="R-Tree query performance depends on minimizing bounding box overlap between sibling nodes. Why?",
        correct="Overlapping bounding boxes force the algorithm to search multiple subtrees for a single query, increasing the number of node accesses",
        distractors=[
            "Overlap causes data corruption in the tree",
            "Overlap makes insertion impossible",
            "Overlap has no effect on query performance"
        ]
    ),
    create_mc_question(
        id="rtree_023", topic="spatial_join_rtree",
        question="When performing a spatial join between two large tables (e.g., cities and rivers), R-Trees improve performance by:",
        correct="First checking bounding box intersections via the index (filter step), then testing exact geometries only for candidates (refine step)",
        distractors=[
            "Computing exact geometric predicates for every pair of objects",
            "Sorting both tables by their centroid coordinates",
            "Pre-computing all pairwise distances"
        ]
    ),
    tf(
        id="rtree_024", topic="rtree_root",
        question="In an R-Tree, the root node must have at least m entries, where m is the minimum fill factor.",
        correct=False  # Root must have at least 2 entries (m>=2 applies to root specifically), not m
    ),
    create_mc_question(
        id="rtree_025", topic="region_query",
        question="A region query identifies all geo-objects that intersect a given query polygon. How does this differ from a window query?",
        correct="A window query uses an axis-aligned rectangle; a region query uses an arbitrary polygon as the query shape",
        distractors=[
            "A region query only returns objects fully inside the query area",
            "A window query works with R-Trees; a region query does not",
            "There is no difference; the terms are interchangeable"
        ]
    ),
]

# ============================================================
# ADDITIONAL: postgis — spatial joins deeper coverage
# ============================================================
postgis_spatial_extra = [
    create_mc_question(
        id="pgis_021", topic="spatial_join",
        question="A spatial join in PostGIS uses a spatial predicate in the join condition instead of matching column values. Which of the following is a correct spatial join?",
        correct="SELECT c.name, r.name FROM cities c JOIN rivers r ON ST_Crosses(c.geom, r.geom);",
        distractors=[
            "SELECT c.name, r.name FROM cities c JOIN rivers r ON c.id = r.city_id;",
            "SELECT c.name FROM cities c WHERE ST_Crosses(c.geom);",
            "SELECT * FROM cities SPATIAL JOIN rivers;"
        ]
    ),
    create_mc_question(
        id="pgis_022", topic="spatial_join",
        question="To find all lakes that lie completely within the state of Berlin, which spatial join query is correct?",
        correct="SELECT lakes.name FROM lakes JOIN states ON states.name = 'Berlin' AND ST_Within(lakes.geom, states.geom);",
        distractors=[
            "SELECT lakes.name FROM lakes WHERE ST_Within(lakes.geom, 'Berlin');",
            "SELECT lakes.name FROM lakes JOIN states ON ST_Crosses(lakes.geom, states.geom) WHERE states.name = 'Berlin';",
            "SELECT lakes.name FROM lakes, states WHERE lakes.geom = states.geom;"
        ]
    ),
    create_mc_question(
        id="pgis_023", topic="gist_index",
        question="In PostGIS, spatial queries can be accelerated by creating a spatial index. Which index type is used and what is the syntax?",
        correct="GiST index: CREATE INDEX idx_geom ON my_table USING GIST (geom);",
        distractors=[
            "B-tree index: CREATE INDEX idx_geom ON my_table (geom);",
            "Hash index: CREATE HASH INDEX idx_geom ON my_table (geom);",
            "R-tree index: CREATE RTREE INDEX idx_geom ON my_table (geom);"
        ]
    ),
    create_mc_question(
        id="pgis_024", topic="spatial_join",
        question="Why is ST_Intersects often preferred over other spatial predicates when writing spatial join queries?",
        correct="ST_Intersects can use spatial indexes (it is 'index-aware'), making it much faster than predicates that cannot use indexes",
        distractors=[
            "ST_Intersects is the only spatial predicate available in PostGIS",
            "ST_Intersects always returns exact results without a refine step",
            "ST_Intersects is faster because it skips the filter step"
        ]
    ),
    create_mc_question(
        id="pgis_025", topic="spatial_join",
        question="To find buildings within 500 meters of a park (assuming projected coordinates in meters), which query pattern is appropriate?",
        correct="SELECT b.name FROM buildings b JOIN parks p ON ST_DWithin(b.geom, p.geom, 500);",
        distractors=[
            "SELECT b.name FROM buildings b JOIN parks p ON ST_Distance(b.geom, p.geom) < 500;",
            "SELECT b.name FROM buildings b WHERE ST_Buffer(b.geom, 500);",
            "SELECT b.name FROM buildings b, parks p WHERE b.geom < 500;"
        ]
    ),
    create_mc_question(
        id="pgis_026", topic="filter_refine",
        question="PostGIS uses a two-phase approach when evaluating spatial predicates. The && operator tests bounding box intersection (filter step). Which statement is true?",
        correct="The && operator is very fast and is used internally by functions like ST_Intersects to quickly eliminate non-candidates before exact geometry testing",
        distractors=[
            "The && operator tests exact geometry intersection",
            "The && operator replaces the need for ST_Intersects",
            "The && operator only works with point geometries"
        ]
    ),
]

# ============================================================
# Write all additions
# ============================================================
print("Adding extra questions:")
append_to_topic("simple_features", sf_extra)
append_to_topic("sql_basics", joins_extra)
append_to_topic("spatial_indexing", rtree_extra)
append_to_topic("postgis", postgis_spatial_extra)
