from enum import Enum

class TablesDBIndexType(Enum):
    KEY = "key"
    FULLTEXT = "fulltext"
    UNIQUE = "unique"
    SPATIAL = "spatial"
