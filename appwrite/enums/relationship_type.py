from enum import Enum

class RelationshipType(Enum):
    ONETOONE = "oneToOne"
    MANYTOONE = "manyToOne"
    MANYTOMANY = "manyToMany"
    ONETOMANY = "oneToMany"
