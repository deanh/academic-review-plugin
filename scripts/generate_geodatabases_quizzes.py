#!/usr/bin/env python3
"""Generate geodatabases quiz question files."""

import json
from pathlib import Path
from quiz_utils import create_mc_question

OUTPUT_DIR = Path(__file__).parent.parent / "server" / "data" / "questions" / "geodatabases"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def tf(id, question, correct, topic):
    return {"id": id, "type": "true_false", "question": question, "correct": correct, "topic": topic}


def write_topic(filename, questions):
    path = OUTPUT_DIR / f"{filename}.json"
    path.write_text(json.dumps(questions, indent=2))
    print(f"  {filename}: {len(questions)} questions")


# ============================================================
# TOPIC: introduction
# ============================================================
introduction = [
    create_mc_question(
        id="intro_001", topic="dbms_properties",
        question="A Database Management System (DBMS) guarantees three fundamental properties for the data it manages. Which of the following is NOT one of these three properties?",
        correct="Scalability",
        distractors=["Persistency", "Consistency", "Central management"]
    ),
    create_mc_question(
        id="intro_002", topic="acid",
        question="The ACID paradigm describes desirable properties of database transactions. What does the 'I' in ACID stand for?",
        correct="Isolation",
        distractors=["Integrity", "Immutability", "Independence"]
    ),
    create_mc_question(
        id="intro_003", topic="acid",
        question="In the ACID paradigm, 'Atomicity' means that a transaction is a non-separable unit. What happens if a system failure occurs partway through a transaction?",
        correct="All changes made by the transaction are rolled back",
        distractors=[
            "Only the last operation is rolled back",
            "The partial changes are committed",
            "The transaction is paused and resumed later"
        ]
    ),
    create_mc_question(
        id="intro_004", topic="data_independence",
        question="Data independence in a DBMS means that the technical and logical implementation of data storage is hidden from the user. What key benefit does this provide?",
        correct="The underlying implementation can change without affecting how users access data",
        distractors=[
            "Users can directly modify the storage engine",
            "Data is always stored in the same format",
            "Users must learn new query syntax when the storage changes"
        ]
    ),
    create_mc_question(
        id="intro_005", topic="redundancy",
        question="Disjunctive (separate) data storage, where each user works with their own copy of data, leads to problems. Which of the following is the primary concern?",
        correct="Data inconsistencies that are difficult to resolve",
        distractors=[
            "Data is stored more efficiently",
            "Users cannot access each other's data",
            "The data is automatically backed up"
        ]
    ),
    create_mc_question(
        id="intro_006", topic="relational_model",
        question="The relational database model, first proposed by Edgar F. Codd in 1969, is based on which mathematical foundation?",
        correct="Set theory and relational algebra",
        distractors=[
            "Graph theory",
            "Linear algebra",
            "Calculus and differential equations"
        ]
    ),
    create_mc_question(
        id="intro_007", topic="relational_model",
        question="In the relational model, data is stored in relations (tables). Which of the following correctly describes the structure of a relation?",
        correct="Fixed number of attributes (columns) and variable number of tuples (rows)",
        distractors=[
            "Variable number of columns and fixed number of rows",
            "Both columns and rows are fixed at creation time",
            "Columns can have values from different domains"
        ]
    ),
    create_mc_question(
        id="intro_008", topic="sql_sublanguages",
        question="SQL is divided into several sublanguages. Which sublanguage contains the SELECT, INSERT, DELETE, and UPDATE statements?",
        correct="Data Manipulation Language (DML)",
        distractors=[
            "Data Definition Language (DDL)",
            "Data Control Language (DCL)",
            "Transaction Control Language (TCL)"
        ]
    ),
    create_mc_question(
        id="intro_009", topic="sql_sublanguages",
        question="The CREATE, ALTER, and DROP statements in SQL belong to which sublanguage?",
        correct="Data Definition Language (DDL)",
        distractors=[
            "Data Manipulation Language (DML)",
            "Data Control Language (DCL)",
            "Transaction Control Language (TCL)"
        ]
    ),
    create_mc_question(
        id="intro_010", topic="geodatabase",
        question="A geodatabase extends a standard object-relational DBMS. Which of the following is NOT a feature provided by a geodatabase extension?",
        correct="Automatic 3D rendering of spatial data",
        distractors=[
            "Abstract data types for spatial data",
            "Spatial indexing for efficient queries",
            "Domain-specific rules for query optimization"
        ]
    ),
    create_mc_question(
        id="intro_011", topic="transactions",
        question="A bank transfer of €100 from Alice to Bob requires two UPDATE operations. If these are NOT wrapped in a transaction and a system failure occurs after the first UPDATE, what happens?",
        correct="Alice loses €100 but Bob does not receive it — the money is lost",
        distractors=[
            "Both accounts remain unchanged",
            "The transfer completes successfully on system recovery",
            "Bob receives €100 but Alice's balance is unchanged"
        ]
    ),
    create_mc_question(
        id="intro_012", topic="relational_operations",
        question="In the relational model, there are three fundamental operations. Which of the following is one of them?",
        correct="Projection onto certain columns of a table",
        distractors=[
            "Sorting rows by primary key",
            "Encrypting column values",
            "Duplicating rows across tables"
        ]
    ),
    tf(
        id="intro_013", topic="consistency",
        question="In a DBMS, consistency means that change requests by the user that violate the data model are still executed, but flagged with a warning.",
        correct=False
    ),
    tf(
        id="intro_014", topic="sql_declarative",
        question="SQL is a declarative language, meaning the user specifies what the result should be, not how it is obtained.",
        correct=True
    ),
    create_mc_question(
        id="intro_015", topic="data_types",
        question="In PostgreSQL, which data type would you use to store a currency amount with fixed fractional precision?",
        correct="money",
        distractors=["real", "integer", "numeric"]
    ),
]

# ============================================================
# TOPIC: uml_modeling
# ============================================================
uml_modeling = [
    create_mc_question(
        id="uml_001", topic="classes_objects",
        question="In UML, what is the relationship between a class and an object?",
        correct="An object is an instance of a class",
        distractors=[
            "A class is an instance of an object",
            "A class and an object are the same thing",
            "An object defines the template for a class"
        ]
    ),
    create_mc_question(
        id="uml_002", topic="encapsulation",
        question="In UML, encapsulation means that attributes and methods are captured in a class. What is the typical visibility convention?",
        correct="Attributes are private (-) and methods are public (+)",
        distractors=[
            "Both attributes and methods are public (+)",
            "Attributes are public (+) and methods are private (-)",
            "Both attributes and methods are protected (#)"
        ]
    ),
    create_mc_question(
        id="uml_003", topic="visibility",
        question="In UML class diagrams, the notation '#' before an attribute or method indicates which visibility level?",
        correct="Protected — visible within the class and its subclasses",
        distractors=[
            "Private — visible only within the class",
            "Public — visible to all classes",
            "Package — visible within the same package"
        ]
    ),
    create_mc_question(
        id="uml_004", topic="inheritance",
        question="When a subclass inherits from a superclass in UML, which of the following is true?",
        correct="The subclass automatically inherits all attributes and methods of the superclass without repeating them",
        distractors=[
            "The subclass must redefine all attributes of the superclass",
            "Only methods are inherited, not attributes",
            "The superclass loses its attributes when a subclass is created"
        ]
    ),
    create_mc_question(
        id="uml_005", topic="abstract_classes",
        question="In a UML class diagram, how is an abstract class visually distinguished from a concrete class?",
        correct="The class name is shown in italics",
        distractors=[
            "The class name is shown in bold",
            "The class rectangle has dashed borders",
            "The class name is underlined"
        ]
    ),
    create_mc_question(
        id="uml_006", topic="associations",
        question="In UML, a multiplicity of '0..*' on one end of an association means:",
        correct="Zero or many instances",
        distractors=[
            "Exactly zero instances",
            "At least one instance",
            "Exactly one instance"
        ]
    ),
    create_mc_question(
        id="uml_007", topic="aggregation_composition",
        question="What is the key difference between aggregation and composition in UML?",
        correct="In composition, parts are deleted when the whole is deleted; in aggregation, parts can exist independently",
        distractors=[
            "Aggregation is stricter than composition",
            "Composition allows parts to belong to multiple wholes; aggregation does not",
            "There is no difference; the terms are interchangeable"
        ]
    ),
    create_mc_question(
        id="uml_008", topic="aggregation_generalization",
        question="Both aggregation and generalization create hierarchies in UML. What is the fundamental difference?",
        correct="Aggregation relates objects (has-a), while generalization relates classes (is-a)",
        distractors=[
            "Aggregation relates classes, while generalization relates objects",
            "Aggregation is used for inheritance, generalization for containment",
            "There is no difference; both model the same relationship"
        ]
    ),
    create_mc_question(
        id="uml_009", topic="polymorphism",
        question="In object-oriented modeling, polymorphism means that methods with the same name can behave differently depending on the object's class. What is the main advantage?",
        correct="Specific objects can be referenced in a general way while behaving individually",
        distractors=[
            "It eliminates the need for inheritance",
            "It allows objects to change their class at runtime",
            "It forces all subclasses to have identical behavior"
        ]
    ),
    create_mc_question(
        id="uml_010", topic="class_naming",
        question="According to UML naming conventions, class names should follow which format?",
        correct="PascalCase and singular form (e.g., ShoppingCart)",
        distractors=[
            "camelCase and plural form (e.g., shoppingCarts)",
            "UPPER_CASE with underscores (e.g., SHOPPING_CART)",
            "lowercase with hyphens (e.g., shopping-cart)"
        ]
    ),
    create_mc_question(
        id="uml_011", topic="class_attributes",
        question="In UML, a class attribute (also called a static attribute) is distinguished from a regular instance attribute by which property?",
        correct="Only one value exists for all instances of the class, and it is underlined in the diagram",
        distractors=[
            "It is shown in italics in the diagram",
            "Each instance has its own copy of the value",
            "It can only be accessed by the constructor method"
        ]
    ),
    create_mc_question(
        id="uml_012", topic="overriding",
        question="In UML modeling, when a subclass provides its own implementation of a method defined in the superclass, this is called:",
        correct="Overriding",
        distractors=["Overloading", "Encapsulation", "Abstraction"]
    ),
    tf(
        id="uml_013", topic="composition",
        question="In a UML composition relationship, the multiplicity on the 'whole' side is always exactly 1, because a part can only belong to one whole.",
        correct=True
    ),
    tf(
        id="uml_014", topic="abstract_classes",
        question="An abstract class in UML can be directly instantiated to create objects.",
        correct=False
    ),
    create_mc_question(
        id="uml_015", topic="data_types",
        question="In UML, the generic notation List<Integer> means:",
        correct="A list collection that may only contain integer values",
        distractors=[
            "A list that is indexed by integers but may contain any type",
            "An integer variable named List",
            "A list of exactly one integer element"
        ]
    ),
    create_mc_question(
        id="uml_016", topic="associations",
        question="A UML class diagram shows a directed association with an arrowhead. What does the arrowhead indicate?",
        correct="The direction of navigability — which class knows about the other",
        distractors=[
            "The direction of data flow",
            "That the relationship is one-to-one",
            "That the association is an aggregation"
        ]
    ),
    create_mc_question(
        id="uml_017", topic="mapping_to_tables",
        question="When mapping a UML class diagram to a relational database, a 1:n association between two classes can be handled by:",
        correct="Adding the key of the '1-side' class as a foreign key in the 'n-side' table, eliminating the need for a separate association table",
        distractors=[
            "Always creating a separate association table",
            "Merging both classes into a single table",
            "Adding the key of the 'n-side' class to the '1-side' table"
        ]
    ),
    create_mc_question(
        id="uml_018", topic="mapping_to_tables",
        question="When mapping an n:m association between two UML classes to a relational schema, what is required?",
        correct="A separate association table containing the foreign keys of both classes",
        distractors=[
            "Adding a foreign key to one of the two tables is sufficient",
            "Both tables are merged into one",
            "No additional table or column is needed"
        ]
    ),
    create_mc_question(
        id="uml_019", topic="inheritance_mapping",
        question="When mapping an inheritance hierarchy to a relational database, Alternative I (one table per class) requires joining tables to query across the hierarchy. Alternative II (single table for the entire hierarchy) avoids joins but has what drawback?",
        correct="Large tuple size with many NULL values for attributes not applicable to certain subclasses",
        distractors=[
            "It cannot represent any subclass-specific attributes",
            "It requires more tables than Alternative I",
            "It breaks referential integrity constraints"
        ]
    ),
    create_mc_question(
        id="uml_020", topic="inheritance_mapping",
        question="In PostgreSQL (an object-relational DBMS), tables can inherit from other tables using the INHERITS keyword. What happens when you query the parent table?",
        correct="Records from both the parent and all child tables are returned",
        distractors=[
            "Only records stored directly in the parent table are returned",
            "An error occurs because parent tables cannot be queried",
            "Only child table records are returned, not the parent's own records"
        ]
    ),
    tf(
        id="uml_021", topic="recursive_association",
        question="A recursive association in UML connects a class to itself, with the class serving in two different roles (e.g., a book referencing other books).",
        correct=True
    ),
    create_mc_question(
        id="uml_022", topic="property_string",
        question="In UML, the property string {ordered} on an association end means:",
        correct="The elements of the collection are maintained in a specific order",
        distractors=[
            "The elements must be sorted alphabetically",
            "The association is read-only",
            "Duplicate elements are not allowed"
        ]
    ),
]

# ============================================================
# TOPIC: simple_features
# ============================================================
simple_features = [
    create_mc_question(
        id="sf_001", topic="adt",
        question="An Abstract Data Type (ADT) in the context of geodatabases provides an implementation-independent representation of value domains and operations. What key characteristic does an ADT have?",
        correct="Its internal data structure is hidden from the user (encapsulation), and access is limited to predefined operations",
        distractors=[
            "The user must understand the internal storage format to use it",
            "It can only store primitive data types like integers and strings",
            "It requires a separate software installation outside the DBMS"
        ]
    ),
    create_mc_question(
        id="sf_002", topic="ogc",
        question="The Simple Feature Access standard is maintained by the Open Geospatial Consortium (OGC) and specifies storage and access of 2D geodata. It consists of two parts. What does Part 2 (ISO 19125-2) define?",
        correct="An SQL implementation for storing and querying simple features",
        distractors=[
            "A common architecture for all geometry types",
            "A 3D extension for volumetric features",
            "A network protocol for transferring spatial data"
        ]
    ),
    create_mc_question(
        id="sf_003", topic="geometry_hierarchy",
        question="In the OGC Simple Feature geometry model, which class is the root of the geometry hierarchy?",
        correct="Geometry",
        distractors=["Point", "Surface", "GeometryCollection"]
    ),
    create_mc_question(
        id="sf_004", topic="curves",
        question="In the Simple Feature model, a LinearRing is a special type of LineString. What two properties must a LinearRing satisfy?",
        correct="It must be both closed (start = end point) and simple (no self-intersection)",
        distractors=[
            "It must have exactly 3 points and be simple",
            "It must be closed and have at least 10 points",
            "It must be open and have no repeated points"
        ]
    ),
    create_mc_question(
        id="sf_005", topic="polygons",
        question="A valid polygon in the Simple Feature model is bounded by an exterior ring and zero or more interior rings. When viewed from above, what is the orientation convention?",
        correct="Exterior ring is counterclockwise, interior rings are clockwise",
        distractors=[
            "Both exterior and interior rings are counterclockwise",
            "Exterior ring is clockwise, interior rings are counterclockwise",
            "The orientation does not matter"
        ]
    ),
    create_mc_question(
        id="sf_006", topic="wkt",
        question="Which of the following is a valid Well-Known Text (WKT) representation of a polygon with one hole?",
        correct="POLYGON((0 0, 0 20, 20 20, 20 0, 0 0),(5 5, 5 15, 15 15, 15 5, 5 5))",
        distractors=[
            "POLYGON(0 0, 0 20, 20 20, 20 0, 0 0)",
            "MULTIPOLYGON((0 0, 0 20, 20 20, 20 0, 0 0),(5 5, 5 15, 15 15, 15 5, 5 5))",
            "POLYGON((0 0, 0 20, 20 20, 20 0))"
        ]
    ),
    create_mc_question(
        id="sf_007", topic="geometry_methods",
        question="The ST_SRID() method returns the Spatial Reference System Identifier of a geometry. For WGS84 coordinates, what is the standard SRID?",
        correct="4326",
        distractors=["4269", "3857", "32632"]
    ),
    create_mc_question(
        id="sf_008", topic="dimension",
        question="In the Simple Feature model, what is the geometric dimension of a Point, a LineString, and a Polygon respectively?",
        correct="0, 1, 2",
        distractors=["1, 2, 3", "0, 1, 3", "1, 1, 2"]
    ),
    create_mc_question(
        id="sf_009", topic="geometry_methods",
        question="The envelope() method returns the minimum bounding rectangle of a geometry. How is this rectangle represented?",
        correct="As a polygon with 5 points: (MinX,MinY), (MaxX,MinY), (MaxX,MaxY), (MinX,MaxY), (MinX,MinY)",
        distractors=[
            "As two points: the lower-left and upper-right corners",
            "As a circle enclosing the geometry",
            "As four separate line segments"
        ]
    ),
    create_mc_question(
        id="sf_010", topic="inserting_geometry",
        question="To insert a polygon geometry into a PostGIS table, which function translates WKT text into the internal polygon representation?",
        correct="ST_PolygonFromText()",
        distractors=["ST_AsText()", "ST_MakePolygon()", "ST_GeomFromGML()"]
    ),
    create_mc_question(
        id="sf_011", topic="m_coordinate",
        question="In the Simple Feature model, some geometries include an 'm' coordinate. What does the 'm' coordinate represent?",
        correct="An additional measurement value (e.g., distance, time, temperature) stored per point",
        distractors=[
            "The magnitude of the coordinate vector",
            "The map scale factor at that point",
            "The elevation above mean sea level"
        ]
    ),
    create_mc_question(
        id="sf_012", topic="geometry_collections",
        question="What constraint must all geometries within a GeometryCollection share?",
        correct="They must have a common spatial reference system",
        distractors=[
            "They must all be the same geometry type",
            "They must all have the same number of points",
            "They must not overlap each other"
        ]
    ),
    tf(
        id="sf_013", topic="curves",
        question="A curve in the Simple Feature model is 'simple' if it passes through each point exactly once, with the possible exception of the start and end points being the same.",
        correct=True
    ),
    tf(
        id="sf_014", topic="valid_polygons",
        question="In the Simple Feature model, two rings of a polygon boundary are allowed to cross each other as long as they share at most two points.",
        correct=False
    ),
    create_mc_question(
        id="sf_015", topic="sql_mm",
        question="The ISO SQL/MM Spatial standard extends the Simple Feature model with additional geometry types. What is one key difference from the Simple Feature model?",
        correct="It includes support for curved geometry segments (e.g., circular arcs) via additional subclasses of ST_Curve",
        distractors=[
            "It removes support for MultiPolygon types",
            "It only supports 3D geometries",
            "It replaces WKT with a binary-only format"
        ]
    ),
]

# ============================================================
# TOPIC: topological_relations
# ============================================================
topological_relations = [
    create_mc_question(
        id="topo_001", topic="point_sets",
        question="In the point set model used for topological relations, the interior of a point set A is denoted A°. What defines a point as being in the interior?",
        correct="All points in its neighborhood are also completely inside the point set",
        distractors=[
            "The point lies on the boundary of the set",
            "The point is the centroid of the set",
            "The point has the maximum distance to any boundary point"
        ]
    ),
    create_mc_question(
        id="topo_002", topic="9im",
        question="The 9-Intersection Model (9IM) classifies topological relationships between two spatial objects X and Y by examining intersections between which components?",
        correct="Interior, boundary, and exterior of both X and Y (forming a 3×3 matrix)",
        distractors=[
            "Only the interiors and boundaries of X and Y (a 2×2 matrix)",
            "The centroids and envelopes of X and Y",
            "The vertices and edges of X and Y"
        ]
    ),
    create_mc_question(
        id="topo_003", topic="de9im",
        question="The Dimension-Extended 9-Intersection Model (DE-9IM) extends the basic 9IM. Instead of just recording whether an intersection is empty or not, what additional information does it record?",
        correct="The dimension of the intersection (-1 for empty, 0 for points, 1 for lines, 2 for areas)",
        distractors=[
            "The number of intersection points",
            "The area of the intersection",
            "The perimeter of the intersection"
        ]
    ),
    create_mc_question(
        id="topo_004", topic="topological_predicates",
        question="Two polygons share a common boundary segment but their interiors do not intersect. Which topological relation describes this?",
        correct="Touches",
        distractors=["Overlaps", "Crosses", "Contains"]
    ),
    create_mc_question(
        id="topo_005", topic="topological_predicates",
        question="ST_Contains(A, B) returns true when which condition is met?",
        correct="No points of B lie in the exterior of A, and at least one point of the interior of B lies in the interior of A",
        distractors=[
            "A and B share at least one boundary point",
            "The interiors of A and B are disjoint",
            "B completely surrounds A"
        ]
    ),
    create_mc_question(
        id="topo_006", topic="de9im_matrix",
        question="In a DE-9IM matrix pattern, 'T' denotes a non-empty set, 'F' denotes an empty set, and '*' means the value is irrelevant. The pattern for ST_Disjoint(A,B) is 'FF*FF****'. What does this mean?",
        correct="The interiors do not intersect, the interior of A does not intersect the boundary of B, and the boundary of A does not intersect the interior of B",
        distractors=[
            "A and B share at least one boundary point",
            "The interiors of A and B completely overlap",
            "A is completely inside B"
        ]
    ),
    create_mc_question(
        id="topo_007", topic="topological_predicates",
        question="Which PostGIS function would you use to find all cities that a river passes through?",
        correct="ST_Crosses",
        distractors=["ST_Within", "ST_Touches", "ST_Equals"]
    ),
    tf(
        id="topo_008", topic="topological_predicates",
        question="ST_Within(A, B) and ST_Contains(B, A) always return the same result — they are inverse relations.",
        correct=True
    ),
    create_mc_question(
        id="topo_009", topic="point_sets",
        question="In point set topology, the closure of a set A consists of:",
        correct="The interior and the boundary of A",
        distractors=[
            "Only the interior of A",
            "The interior and the exterior of A",
            "Only the boundary of A"
        ]
    ),
    tf(
        id="topo_010", topic="de9im",
        question="In the DE-9IM, the dimension value returned is always the highest dimension among all geometries resulting from the intersection.",
        correct=True
    ),
    create_mc_question(
        id="topo_011", topic="topological_predicates",
        question="ST_Overlaps returns true when two geometries share space and are of the same dimension, but are not completely contained by each other. For two polygons (dimension 2), which DE-9IM pattern applies?",
        correct="T*T / ***: / T**",
        distractors=[
            "T*F / ***: / ***",
            "FFF / FF*: / ***",
            "T** / *T*: / **T"
        ]
    ),
    create_mc_question(
        id="topo_012", topic="topological_predicates",
        question="Two geometries are considered 'equal' (ST_Equals) when:",
        correct="They are topologically equal — same dimension, type, and all coordinates identical",
        distractors=[
            "They have the same bounding box",
            "They share at least one interior point",
            "They have the same area"
        ]
    ),
]

# ============================================================
# TOPIC: normalization
# ============================================================
normalization = [
    create_mc_question(
        id="norm_001", topic="anomalies",
        question="If a table stores both book titles and publisher information, and you update the publisher's city in only one row but not others, this causes which type of anomaly?",
        correct="Update anomaly",
        distractors=["Insertion anomaly", "Deletion anomaly", "Transitive anomaly"]
    ),
    create_mc_question(
        id="norm_002", topic="anomalies",
        question="If deleting a book from a table also deletes the only record of its publisher's information, this is an example of:",
        correct="Deletion anomaly",
        distractors=["Update anomaly", "Insertion anomaly", "Referential anomaly"]
    ),
    create_mc_question(
        id="norm_003", topic="anomalies",
        question="If you cannot add a new book to a table because the publisher information is unknown (and those columns don't allow NULL), this is an example of:",
        correct="Insertion anomaly",
        distractors=["Update anomaly", "Deletion anomaly", "Normalization anomaly"]
    ),
    create_mc_question(
        id="norm_004", topic="1nf",
        question="A relation is in First Normal Form (1NF) if:",
        correct="All attributes have atomic (indivisible) values",
        distractors=[
            "There are no redundant rows",
            "Every attribute depends on the full candidate key",
            "There are no transitive dependencies"
        ]
    ),
    create_mc_question(
        id="norm_005", topic="1nf",
        question="A table has an 'Authors' column that contains values like 'Garcia-Molina, Ullman, Widom' in a single cell. This violates which normal form?",
        correct="First Normal Form (1NF), because the Authors attribute is not atomic",
        distractors=[
            "Second Normal Form, because of partial dependency",
            "Third Normal Form, because of transitive dependency",
            "BCNF, because of a non-superkey determinant"
        ]
    ),
    create_mc_question(
        id="norm_006", topic="functional_dependency",
        question="In a relation with attributes {Matriculation No., Semester, Lecture, Teaching Assistant}, the functional dependency 'Matriculation No. → Semester' means:",
        correct="Each matriculation number is associated with precisely one semester value",
        distractors=[
            "Each semester has exactly one student",
            "The semester determines the matriculation number",
            "Semester and Matriculation No. are interchangeable"
        ]
    ),
    create_mc_question(
        id="norm_007", topic="2nf",
        question="A relation is in Second Normal Form (2NF) if it is in 1NF and:",
        correct="Every non-prime attribute is functionally dependent on the whole candidate key, not just part of it",
        distractors=[
            "All attributes have atomic values",
            "There are no transitive dependencies",
            "Every determinant is a superkey"
        ]
    ),
    create_mc_question(
        id="norm_008", topic="2nf",
        question="A table has the candidate key {Manufacturer, Model} and a non-prime attribute 'Country' that depends only on 'Manufacturer'. This violates which normal form?",
        correct="Second Normal Form (2NF), because Country has a partial dependency on the candidate key",
        distractors=[
            "First Normal Form (1NF)",
            "Third Normal Form (3NF)",
            "Boyce-Codd Normal Form (BCNF)"
        ]
    ),
    create_mc_question(
        id="norm_009", topic="3nf",
        question="A relation is in Third Normal Form (3NF) if it is in 2NF and:",
        correct="No non-prime attribute is transitively dependent on any candidate key",
        distractors=[
            "All attributes have atomic values",
            "No attribute depends on part of a candidate key",
            "Every determinant is a superkey"
        ]
    ),
    create_mc_question(
        id="norm_010", topic="transitive_dependency",
        question="In a table with attributes {ID, Title, Publisher, Place, Year}, the dependency ID → Publisher → Place is an example of:",
        correct="A transitive dependency, because Place depends on Publisher, which depends on ID",
        distractors=[
            "A partial dependency",
            "A trivial dependency",
            "A multi-valued dependency"
        ]
    ),
    create_mc_question(
        id="norm_011", topic="3nf_mnemonic",
        question="The informal definition of 3NF states that each non-key attribute should depend on 'the key, the whole key, and nothing but the key.' What does 'nothing but the key' specifically prohibit?",
        correct="Transitive dependencies — non-key attributes depending on other non-key attributes",
        distractors=[
            "Partial dependencies on composite keys",
            "Atomic values in all columns",
            "Using artificial integer keys"
        ]
    ),
    create_mc_question(
        id="norm_012", topic="keys",
        question="What is the difference between a superkey and a candidate key?",
        correct="A candidate key is a minimal superkey — no attribute can be removed without losing the unique identification property",
        distractors=[
            "A superkey is always a single attribute; a candidate key can be composite",
            "A candidate key allows NULL values; a superkey does not",
            "There is no difference; the terms are synonymous"
        ]
    ),
    create_mc_question(
        id="norm_013", topic="keys",
        question="Attributes that are part of any candidate key are called:",
        correct="Prime attributes",
        distractors=["Non-prime attributes", "Foreign attributes", "Surrogate attributes"]
    ),
    create_mc_question(
        id="norm_014", topic="bcnf",
        question="A relation is in Boyce-Codd Normal Form (BCNF) if for every non-trivial functional dependency X → Y:",
        correct="X is a superkey",
        distractors=[
            "Y is a superkey",
            "X contains only prime attributes",
            "Y contains only non-prime attributes"
        ]
    ),
    create_mc_question(
        id="norm_015", topic="bcnf",
        question="A table is in 3NF but not in BCNF. This can happen when:",
        correct="All attributes are prime (part of some candidate key), but a functional dependency exists where the determinant is not a superkey",
        distractors=[
            "The table has non-atomic values",
            "There is a partial dependency on the primary key",
            "There are no candidate keys"
        ]
    ),
    create_mc_question(
        id="norm_016", topic="2nf_fix",
        question="To convert a relation from 1NF to 2NF, you need to:",
        correct="Remove partially dependent attributes and place them in a new table with the part of the key they depend on",
        distractors=[
            "Combine all tables into one",
            "Add an artificial primary key",
            "Remove all NULL values"
        ]
    ),
    create_mc_question(
        id="norm_017", topic="3nf_fix",
        question="To convert a relation from 2NF to 3NF, you need to:",
        correct="Remove transitively dependent attributes and place them in a new table with the non-key attribute they depend on",
        distractors=[
            "Split multi-valued attributes into separate columns",
            "Remove all partial dependencies",
            "Merge related tables to eliminate joins"
        ]
    ),
    create_mc_question(
        id="norm_018", topic="denormalization",
        question="Denormalization — intentionally not normalizing tables — may be appropriate when:",
        correct="Performance optimization is needed to avoid expensive joins, or the dependency may change with future application rules",
        distractors=[
            "The database has no redundancy at all",
            "All tables are already in BCNF",
            "The application only performs INSERT operations"
        ]
    ),
    tf(
        id="norm_019", topic="functional_dependency",
        question="The functional dependency {Matriculation No., Lecture} → Lecture is a trivial dependency because the dependent attribute (Lecture) is a subset of the determinant.",
        correct=True
    ),
    tf(
        id="norm_020", topic="keys",
        question="If no candidate key exists for a relation and duplicate tuples could occur, an artificial key (typically an auto-incrementing integer) should be introduced as the primary key.",
        correct=True
    ),
    create_mc_question(
        id="norm_021", topic="functional_dependency",
        question="In a relation, the functional dependency Lecture → Professor holds if there is one professor per lecture. Functional dependencies should be determined based on:",
        correct="The semantics (meaning) of the data, not just the current data instances",
        distractors=[
            "Only the currently stored data rows",
            "The number of rows in the table",
            "The data types of the attributes"
        ]
    ),
    create_mc_question(
        id="norm_022", topic="normalization_summary",
        question="Put the normal forms in order from weakest to strongest requirement:",
        correct="1NF → 2NF → 3NF → BCNF",
        distractors=[
            "BCNF → 3NF → 2NF → 1NF",
            "1NF → 3NF → 2NF → BCNF",
            "2NF → 1NF → BCNF → 3NF"
        ]
    ),
    tf(
        id="norm_023", topic="2nf",
        question="A relation in 1NF with a single-attribute candidate key is automatically in 2NF, because partial dependencies are impossible when the key has only one attribute.",
        correct=True
    ),
    create_mc_question(
        id="norm_024", topic="anomalies",
        question="Database normalization aims to eliminate redundancy to protect against anomalies. Which of the following is NOT a type of anomaly addressed by normalization?",
        correct="Query anomaly",
        distractors=["Insertion anomaly", "Update anomaly", "Deletion anomaly"]
    ),
]

# ============================================================
# TOPIC: geo_data_infrastructure
# ============================================================
geo_data_infrastructure = [
    create_mc_question(
        id="gdi_001", topic="interoperability",
        question="In the context of Geo Data Infrastructures, 'syntactic interoperability' means:",
        correct="Applications and services can work with the same data exchange formats",
        distractors=[
            "Users share the same understanding of terminology",
            "All data is stored in the same database",
            "Users speak the same language"
        ]
    ),
    create_mc_question(
        id="gdi_002", topic="interoperability",
        question="'Semantic interoperability' in Geo Data Infrastructures refers to:",
        correct="Users having a common understanding of the terminology and spatial extent of the data",
        distractors=[
            "Data exchange using the same file formats",
            "Using the same DBMS software",
            "Storing data in the same coordinate system"
        ]
    ),
    create_mc_question(
        id="gdi_003", topic="ogc_services",
        question="The OGC Web Map Service (WMS) allows clients to request maps from a server. In which format is the map returned?",
        correct="As a rendered image (e.g., PNG, JPEG)",
        distractors=[
            "As raw vector data in GML format",
            "As a database table",
            "As a PDF document"
        ]
    ),
    create_mc_question(
        id="gdi_004", topic="ogc_services",
        question="Unlike WMS which returns rendered images, the OGC Web Feature Service (WFS) returns:",
        correct="The actual geographic feature data (vector data) that clients can analyze and process",
        distractors=[
            "Raster images of the features",
            "Only metadata about the features",
            "Pre-computed statistics about the features"
        ]
    ),
    create_mc_question(
        id="gdi_005", topic="ogc_services",
        question="All OGC web services support a 'GetCapabilities' request. What does this request return?",
        correct="An XML document describing the service's capabilities, available layers, supported formats, etc.",
        distractors=[
            "The actual map or feature data",
            "The service's usage statistics",
            "A list of all registered users"
        ]
    ),
    create_mc_question(
        id="gdi_006", topic="ogc_services",
        question="OGC web service requests are typically made via URL. Parameters are included after a '?' and separated by '&'. What HTTP method is most commonly used?",
        correct="GET",
        distractors=["POST", "PUT", "DELETE"]
    ),
    create_mc_question(
        id="gdi_007", topic="standards",
        question="What is the primary goal of standardization in the context of Geographic Information Systems?",
        correct="To enable complete, interoperable exchange of geodata without information loss",
        distractors=[
            "To ensure all GIS software looks the same",
            "To restrict geodata to a single file format",
            "To make all geodata freely available"
        ]
    ),
    tf(
        id="gdi_008", topic="ogc_services",
        question="The OGC Web Coverage Service (WCS) is designed to provide access to raster/coverage data (e.g., satellite imagery, DEMs), unlike WFS which provides vector feature data.",
        correct=True
    ),
    create_mc_question(
        id="gdi_009", topic="inspire",
        question="INSPIRE is a European Union directive related to spatial data. What is its primary purpose?",
        correct="To create a spatial data infrastructure across EU member states for environmental policies",
        distractors=[
            "To standardize all European map projections",
            "To replace national mapping agencies",
            "To provide free GPS services across Europe"
        ]
    ),
    create_mc_question(
        id="gdi_010", topic="ogc_services",
        question="The Catalogue Service for the Web (CSW) allows users to:",
        correct="Search for and discover geospatial datasets and services through metadata",
        distractors=[
            "Download large raster datasets efficiently",
            "Convert between coordinate reference systems",
            "Edit feature geometries directly on the server"
        ]
    ),
]

# ============================================================
# TOPIC: spatial_indexing
# ============================================================
spatial_indexing = [
    create_mc_question(
        id="rtree_001", topic="spatial_queries",
        question="A window query in spatial databases identifies all geo-objects that:",
        correct="Overlap a given axis-aligned rectangle",
        distractors=[
            "Contain a specific point",
            "Are visible on the current screen",
            "Have the largest area"
        ]
    ),
    create_mc_question(
        id="rtree_002", topic="filter_refine",
        question="The filter-and-refine strategy for spatial queries consists of two steps. What happens in the filter step?",
        correct="The spatial index is queried using bounding boxes, producing a set of candidate objects",
        distractors=[
            "Exact geometric predicates are evaluated on all objects",
            "Objects are sorted by their area",
            "The query geometry is simplified"
        ]
    ),
    create_mc_question(
        id="rtree_003", topic="filter_refine",
        question="Why is the refine step necessary after the filter step in spatial query processing?",
        correct="Because bounding boxes may produce false positives — objects whose bounding box intersects the query but whose actual geometry does not",
        distractors=[
            "Because the filter step may miss valid results",
            "Because bounding boxes are always exact",
            "Because the spatial index is approximate and may contain errors"
        ]
    ),
    create_mc_question(
        id="rtree_004", topic="rtree_structure",
        question="An R-Tree is a balanced search tree for spatial indexing. Each node has a minimum of m and maximum of M entries. What constraint relates m and M?",
        correct="m ≤ (M+1)/2, ensuring a node can always be split into two valid nodes",
        distractors=[
            "m = M/3",
            "m = M - 1",
            "m must equal M"
        ]
    ),
    create_mc_question(
        id="rtree_005", topic="rtree_structure",
        question="In an R-Tree, what does each non-leaf node entry contain?",
        correct="A minimum bounding box that encloses all entries in its child node, plus a pointer to that child",
        distractors=[
            "The exact geometry of one spatial object",
            "A sorted list of all object IDs in its subtree",
            "The centroid coordinates of its child objects"
        ]
    ),
    create_mc_question(
        id="rtree_006", topic="rtree_operations",
        question="When inserting a new entry into an R-Tree and the target leaf node is full (has M entries), what happens?",
        correct="The node is split into two nodes, and the split may propagate up the tree",
        distractors=[
            "The oldest entry is removed to make room",
            "The entry is stored in a separate overflow table",
            "The tree is completely rebuilt"
        ]
    ),
    create_mc_question(
        id="rtree_007", topic="spatial_join",
        question="A spatial join combines two sets of spatial objects using a spatial predicate. To find which cities a river flows through, you would use:",
        correct="SELECT cities.name FROM cities JOIN rivers ON ST_Crosses(cities.geometry, rivers.geometry)",
        distractors=[
            "SELECT cities.name FROM cities WHERE rivers.geometry IS NOT NULL",
            "SELECT cities.name FROM cities, rivers WHERE cities.id = rivers.id",
            "SELECT cities.name FROM cities INNER JOIN rivers ON cities.name = rivers.name"
        ]
    ),
    create_mc_question(
        id="rtree_008", topic="brute_force",
        question="Without spatial indexing, a brute-force spatial query tests all objects sequentially. If there are p polygons with up to n edges each, what is the time complexity of checking one query against all polygons?",
        correct="O(p · n) in the worst case, making it infeasible for large datasets",
        distractors=[
            "O(log p), which is efficient",
            "O(1), because geometric predicates are constant time",
            "O(p²), due to all-pairs comparison"
        ]
    ),
    create_mc_question(
        id="rtree_009", topic="rtree_structure",
        question="An R-Tree groups spatial objects by their bounding boxes. Why might bounding boxes of sibling nodes overlap?",
        correct="Unlike B-trees which partition 1D space cleanly, 2D bounding boxes of irregularly distributed objects cannot always be separated without overlap",
        distractors=[
            "Because the R-Tree implementation is incorrect",
            "Because all bounding boxes must be the same size",
            "Overlapping is prevented by the R-Tree algorithm"
        ]
    ),
    tf(
        id="rtree_010", topic="rtree_structure",
        question="An R-Tree is a balanced tree, meaning all leaf nodes are at the same depth.",
        correct=True
    ),
    create_mc_question(
        id="rtree_011", topic="rtree_operations",
        question="When deleting an entry from an R-Tree and the resulting node has fewer than m entries (underflow), what happens?",
        correct="The underfull node is dissolved and its remaining entries are reinserted into the tree",
        distractors=[
            "The node is simply left with fewer than m entries",
            "Adjacent nodes are merged regardless of their size",
            "The entire tree is rebuilt from scratch"
        ]
    ),
    create_mc_question(
        id="rtree_012", topic="mbb",
        question="Using minimum bounding boxes (MBBs) as an approximation for spatial objects provides a key performance benefit. What is it?",
        correct="Testing intersection of two axis-aligned rectangles is very fast compared to testing complex polygon geometries",
        distractors=[
            "MBBs always perfectly represent the shape of the object",
            "MBBs eliminate the need for a refine step",
            "MBBs reduce the storage size of the geometry"
        ]
    ),
]

# ============================================================
# TOPIC: sql_basics (from labs 1b-5)
# ============================================================
sql_basics = [
    create_mc_question(
        id="sql_001", topic="create_table",
        question="Which SQL statement creates a new table called 'student' with an integer column 'id' and a text column 'name'?",
        correct="CREATE TABLE student (id INTEGER, name VARCHAR(50));",
        distractors=[
            "NEW TABLE student (id INTEGER, name VARCHAR(50));",
            "CREATE student TABLE (id INTEGER, name VARCHAR(50));",
            "INSERT TABLE student (id INTEGER, name VARCHAR(50));"
        ]
    ),
    create_mc_question(
        id="sql_002", topic="primary_key",
        question="A primary key constraint in SQL ensures that:",
        correct="The column(s) uniquely identify each row and cannot contain NULL values",
        distractors=[
            "The column can contain duplicate values",
            "The column is automatically indexed but may contain NULLs",
            "The column must contain sequential integer values"
        ]
    ),
    create_mc_question(
        id="sql_003", topic="foreign_key",
        question="A FOREIGN KEY constraint in SQL establishes a link between two tables. If you define FOREIGN KEY (dept_id) REFERENCES department(id), what does this enforce?",
        correct="Every value in dept_id must exist as a value in the id column of the department table",
        distractors=[
            "The dept_id column must have the same name as the referenced column",
            "The department table must have fewer rows than the current table",
            "Values are automatically copied from the department table"
        ]
    ),
    create_mc_question(
        id="sql_004", topic="select",
        question="What does the SQL statement SELECT DISTINCT city FROM student; return?",
        correct="A list of unique city values from the student table, with duplicates removed",
        distractors=[
            "All rows from the student table",
            "Only the first occurrence of each city",
            "An error, because DISTINCT requires a WHERE clause"
        ]
    ),
    create_mc_question(
        id="sql_005", topic="where",
        question="Which SQL clause filters rows based on a condition?",
        correct="WHERE",
        distractors=["HAVING", "ORDER BY", "GROUP BY"]
    ),
    create_mc_question(
        id="sql_006", topic="joins",
        question="An INNER JOIN between two tables returns:",
        correct="Only the rows where the join condition is satisfied in both tables",
        distractors=[
            "All rows from both tables, with NULLs where there is no match",
            "All rows from the left table, plus matching rows from the right",
            "The Cartesian product of both tables"
        ]
    ),
    create_mc_question(
        id="sql_007", topic="joins",
        question="A LEFT JOIN (LEFT OUTER JOIN) between table A and table B returns:",
        correct="All rows from A, plus matching rows from B; if no match exists in B, the B columns contain NULL",
        distractors=[
            "Only rows that exist in both A and B",
            "All rows from B, plus matching rows from A",
            "Only rows from A that have no match in B"
        ]
    ),
    create_mc_question(
        id="sql_008", topic="aggregate",
        question="Which SQL statement counts the number of students in each city?",
        correct="SELECT city, COUNT(*) FROM student GROUP BY city;",
        distractors=[
            "SELECT city, COUNT(*) FROM student;",
            "SELECT city, SUM(*) FROM student GROUP BY city;",
            "SELECT city, COUNT(*) FROM student ORDER BY city;"
        ]
    ),
    create_mc_question(
        id="sql_009", topic="drop",
        question="The SQL statement DROP TABLE student; will:",
        correct="Permanently and irreversibly delete the entire student table and all its data",
        distractors=[
            "Delete all rows but keep the table structure",
            "Move the table to a recycle bin for later recovery",
            "Only work if the table is empty"
        ]
    ),
    create_mc_question(
        id="sql_010", topic="data_types",
        question="In PostgreSQL, what is the difference between CHAR(10) and VARCHAR(10)?",
        correct="CHAR(10) is fixed-length (always padded to 10 characters), while VARCHAR(10) is variable-length (up to 10 characters)",
        distractors=[
            "CHAR allows numbers only, VARCHAR allows letters only",
            "They are identical in behavior",
            "VARCHAR(10) requires at least 10 characters, CHAR(10) does not"
        ]
    ),
    create_mc_question(
        id="sql_011", topic="insert",
        question="Which SQL statement correctly inserts a row into the student table?",
        correct="INSERT INTO student (id, name, city) VALUES (1, 'Alice', 'Berlin');",
        distractors=[
            "INSERT student VALUES (1, 'Alice', 'Berlin');",
            "ADD INTO student (id, name, city) VALUES (1, 'Alice', 'Berlin');",
            "INSERT INTO student SET id=1, name='Alice', city='Berlin';"
        ]
    ),
    create_mc_question(
        id="sql_012", topic="order_by",
        question="SELECT name, age FROM student ORDER BY age DESC; will return results:",
        correct="Sorted by age in descending order (highest age first)",
        distractors=[
            "Sorted by age in ascending order (lowest age first)",
            "Sorted alphabetically by name",
            "In the order rows were inserted"
        ]
    ),
    create_mc_question(
        id="sql_013", topic="like",
        question="In SQL, the LIKE operator with '%' as a wildcard matches any sequence of characters. What does SELECT * FROM student WHERE name LIKE 'M%'; return?",
        correct="All students whose name starts with 'M'",
        distractors=[
            "All students whose name contains 'M' anywhere",
            "All students whose name is exactly 'M'",
            "All students whose name ends with 'M'"
        ]
    ),
    create_mc_question(
        id="sql_014", topic="null",
        question="In SQL, how do you check if a column value is NULL?",
        correct="Using IS NULL (e.g., WHERE city IS NULL)",
        distractors=[
            "Using = NULL (e.g., WHERE city = NULL)",
            "Using == NULL",
            "Using EQUALS NULL"
        ]
    ),
    create_mc_question(
        id="sql_015", topic="update",
        question="Which SQL statement changes the city of the student with id 5 to 'Munich'?",
        correct="UPDATE student SET city = 'Munich' WHERE id = 5;",
        distractors=[
            "MODIFY student SET city = 'Munich' WHERE id = 5;",
            "UPDATE student WHERE id = 5 SET city = 'Munich';",
            "SET student.city = 'Munich' WHERE student.id = 5;"
        ]
    ),
    create_mc_question(
        id="sql_016", topic="cross_join",
        question="A CROSS JOIN between two tables produces:",
        correct="The Cartesian product — every row from the first table combined with every row from the second",
        distractors=[
            "Only rows where the primary keys match",
            "The union of both tables",
            "Only rows that exist in both tables"
        ]
    ),
    create_mc_question(
        id="sql_017", topic="constraints",
        question="The NOT NULL constraint on a column means:",
        correct="The column must always have a value; NULL is not allowed",
        distractors=[
            "The column must contain the value 'NOT NULL'",
            "The column cannot contain the number zero",
            "The column is optional but recommended"
        ]
    ),
    create_mc_question(
        id="sql_018", topic="bigserial",
        question="In PostgreSQL, the BIGSERIAL data type is used for:",
        correct="Auto-incrementing integer primary keys",
        distractors=[
            "Storing large text strings",
            "Storing binary data",
            "Storing timestamps with timezone"
        ]
    ),
    tf(
        id="sql_019", topic="case_sensitivity",
        question="In PostgreSQL, unquoted table and column names are automatically converted to lowercase. For example, CREATE TABLE MyTable creates a table named 'mytable'.",
        correct=True
    ),
    create_mc_question(
        id="sql_020", topic="delete_vs_drop",
        question="What is the difference between DELETE FROM student; and DROP TABLE student;?",
        correct="DELETE removes all rows but keeps the table structure; DROP removes the entire table including its structure",
        distractors=[
            "They are identical in effect",
            "DELETE removes the table; DROP removes only the rows",
            "DELETE can be rolled back; DROP removes only one row"
        ]
    ),
]

# ============================================================
# TOPIC: postgis (from labs 7-10)
# ============================================================
postgis = [
    create_mc_question(
        id="pgis_001", topic="create_extension",
        question="To enable PostGIS in a PostgreSQL database, which SQL command do you use?",
        correct="CREATE EXTENSION postgis;",
        distractors=[
            "INSTALL postgis;",
            "ENABLE EXTENSION postgis;",
            "ADD EXTENSION postgis;"
        ]
    ),
    create_mc_question(
        id="pgis_002", topic="geometry_column",
        question="When creating a table with a geometry column in PostGIS, how is the geometry column typically defined?",
        correct="As a column with the data type GEOMETRY (e.g., geom GEOMETRY)",
        distractors=[
            "As a VARCHAR column containing coordinate strings",
            "As two separate columns for X and Y coordinates",
            "As a BLOB column containing binary shape data"
        ]
    ),
    create_mc_question(
        id="pgis_003", topic="st_geomfromtext",
        question="Which PostGIS function creates a geometry from Well-Known Text with a specified SRID?",
        correct="ST_GeomFromText('POINT(13.4 52.5)', 4326)",
        distractors=[
            "ST_MakePoint('POINT(13.4 52.5)', 4326)",
            "ST_CreateGeom('POINT(13.4 52.5)', 4326)",
            "ST_WKTToGeom('POINT(13.4 52.5)', 4326)"
        ]
    ),
    create_mc_question(
        id="pgis_004", topic="st_astext",
        question="To output a geometry column as human-readable WKT in a SELECT query, you use:",
        correct="ST_AsText(geom)",
        distractors=["ST_Print(geom)", "CAST(geom AS TEXT)", "ST_Describe(geom)"]
    ),
    create_mc_question(
        id="pgis_005", topic="st_area",
        question="ST_Area(geom) in PostGIS returns the area of a polygon geometry. If the geometry uses SRID 4326 (WGS84 geographic coordinates), the result is in:",
        correct="Square degrees, which is generally not useful — you should transform to a projected CRS first",
        distractors=[
            "Square meters",
            "Square kilometers",
            "Hectares"
        ]
    ),
    create_mc_question(
        id="pgis_006", topic="st_transform",
        question="To convert a geometry from one coordinate reference system to another in PostGIS, you use:",
        correct="ST_Transform(geom, target_srid)",
        distractors=[
            "ST_SetSRID(geom, target_srid)",
            "ST_Reproject(geom, target_srid)",
            "ST_ConvertCRS(geom, target_srid)"
        ]
    ),
    create_mc_question(
        id="pgis_007", topic="st_setsrid",
        question="ST_SetSRID(geom, 4326) does what to the geometry?",
        correct="Sets the SRID metadata to 4326 without transforming the coordinates — it only labels the geometry",
        distractors=[
            "Transforms the coordinates to WGS84",
            "Creates a new geometry in SRID 4326",
            "Validates that the geometry is in SRID 4326"
        ]
    ),
    create_mc_question(
        id="pgis_008", topic="st_distance",
        question="ST_Distance(geom_a, geom_b) returns the shortest distance between two geometries. For geometries in SRID 4326 (degrees), how can you get the distance in meters?",
        correct="Use ST_Distance with geography type: ST_Distance(geom_a::geography, geom_b::geography)",
        distractors=[
            "Multiply the result by 111000",
            "Use ST_Distance_Meters(geom_a, geom_b)",
            "The result is always in meters regardless of SRID"
        ]
    ),
    create_mc_question(
        id="pgis_009", topic="st_buffer",
        question="ST_Buffer(geom, distance) creates a buffer polygon around a geometry. What does the distance parameter represent?",
        correct="The buffer distance in the units of the geometry's coordinate reference system",
        distractors=[
            "Always in meters",
            "Always in degrees",
            "A percentage of the geometry's extent"
        ]
    ),
    create_mc_question(
        id="pgis_010", topic="st_intersection",
        question="ST_Intersection(geom_a, geom_b) returns:",
        correct="A geometry representing the shared area (or shared portion) of the two input geometries",
        distractors=[
            "TRUE if the geometries intersect, FALSE otherwise",
            "The geometry of geom_a minus the overlap with geom_b",
            "The union of both geometries"
        ]
    ),
    create_mc_question(
        id="pgis_011", topic="spatial_ref_sys",
        question="After installing PostGIS, the table spatial_ref_sys is automatically created. What does it contain?",
        correct="Definitions of coordinate reference systems (SRID, authority, projection parameters) used for spatial data",
        distractors=[
            "A log of all spatial queries executed",
            "Metadata about all geometry columns in the database",
            "The spatial index configuration"
        ]
    ),
    create_mc_question(
        id="pgis_012", topic="importing_data",
        question="Which tool or command can be used to import a Shapefile into a PostGIS database?",
        correct="shp2pgsql (command-line) or shp2pgsql-gui (graphical)",
        distractors=[
            "pg_dump",
            "ST_ImportShape()",
            "COPY FROM 'file.shp'"
        ]
    ),
    create_mc_question(
        id="pgis_013", topic="st_union",
        question="ST_Union(geom_a, geom_b) returns:",
        correct="A geometry representing the combined area of both input geometries",
        distractors=[
            "Only the overlapping portion of the two geometries",
            "TRUE if the geometries can be merged",
            "The larger of the two geometries"
        ]
    ),
    create_mc_question(
        id="pgis_014", topic="geometry_type",
        question="To determine the geometry type of a column in PostGIS, you can use:",
        correct="ST_GeometryType(geom)",
        distractors=["ST_Type(geom)", "GeomType(geom)", "ST_Describe(geom)"]
    ),
    create_mc_question(
        id="pgis_015", topic="st_centroid",
        question="ST_Centroid(geom) returns the geometric center of a geometry. Is the centroid guaranteed to be inside the geometry?",
        correct="No — for concave polygons or multipolygons, the centroid may fall outside the geometry; use ST_PointOnSurface for a guaranteed interior point",
        distractors=[
            "Yes — the centroid is always inside the geometry",
            "Only for polygons, not for lines or points",
            "Only if the geometry has been validated with ST_IsValid"
        ]
    ),
    create_mc_question(
        id="pgis_016", topic="views",
        question="In PostgreSQL, a VIEW is:",
        correct="A stored query that acts like a virtual table — it does not store data itself but runs the query each time it is accessed",
        distractors=[
            "A physical copy of a table's data",
            "A temporary table that is deleted on session end",
            "An index on a table for faster queries"
        ]
    ),
    create_mc_question(
        id="pgis_017", topic="st_length",
        question="ST_Length(geom) returns the length of a linestring. For a polygon, what does it return?",
        correct="0 — ST_Length is designed for lines; use ST_Perimeter for polygon boundaries",
        distractors=[
            "The perimeter of the polygon",
            "The area of the polygon",
            "An error"
        ]
    ),
    tf(
        id="pgis_018", topic="st_intersects",
        question="ST_Intersects(A, B) returns TRUE if the two geometries share any space at all — including if they merely touch at a boundary point.",
        correct=True
    ),
    create_mc_question(
        id="pgis_019", topic="st_difference",
        question="ST_Difference(geom_a, geom_b) returns:",
        correct="The part of geom_a that does not intersect with geom_b",
        distractors=[
            "The absolute distance between the two geometries",
            "The symmetric difference (parts in A or B but not both)",
            "TRUE if the geometries are different"
        ]
    ),
    create_mc_question(
        id="pgis_020", topic="pgrouting",
        question="The pgRouting extension for PostGIS provides what functionality?",
        correct="Network routing and graph analysis capabilities (e.g., shortest path, traveling salesman) on spatial networks",
        distractors=[
            "Raster data processing and analysis",
            "3D visualization of spatial data",
            "Automated data backup and replication"
        ]
    ),
]

# ============================================================
# Write all topics
# ============================================================
print("Generating geodatabases quiz files:")
write_topic("introduction", introduction)
write_topic("uml_modeling", uml_modeling)
write_topic("simple_features", simple_features)
write_topic("topological_relations", topological_relations)
write_topic("normalization", normalization)
write_topic("geo_data_infrastructure", geo_data_infrastructure)
write_topic("spatial_indexing", spatial_indexing)
write_topic("sql_basics", sql_basics)
write_topic("postgis", postgis)

total = sum(len(q) for q in [introduction, uml_modeling, simple_features, topological_relations, normalization, geo_data_infrastructure, spatial_indexing, sql_basics, postgis])
print(f"\nTotal: {total} questions across 9 topics")
