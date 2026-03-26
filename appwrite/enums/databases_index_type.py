from enum import Enum

class DatabasesIndexType(Enum):
    KEY = "key"
    FULLTEXT = "fulltext"
    UNIQUE = "unique"
    SPATIAL = "spatial"
