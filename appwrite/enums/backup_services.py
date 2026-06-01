from enum import Enum

class BackupServices(Enum):
    DATABASES = "databases"
    TABLESDB = "tablesdb"
    DOCUMENTSDB = "documentsdb"
    VECTORSDB = "vectorsdb"
    DEDICATEDDATABASES = "dedicatedDatabases"
    FUNCTIONS = "functions"
    STORAGE = "storage"
