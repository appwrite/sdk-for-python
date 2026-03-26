from enum import Enum

class DatabaseType(Enum):
    LEGACY = "legacy"
    TABLESDB = "tablesdb"
    DOCUMENTSDB = "documentsdb"
    VECTORSDB = "vectorsdb"
