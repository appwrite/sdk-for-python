from enum import Enum

class DocumentsDBIndexType(Enum):
    KEY = "key"
    FULLTEXT = "fulltext"
    UNIQUE = "unique"
    SPATIAL = "spatial"
