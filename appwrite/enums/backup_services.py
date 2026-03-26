from enum import Enum

class BackupServices(Enum):
    DATABASES = "databases"
    TABLESDB = "tablesdb"
    DOCUMENTSDB = "documentsdb"
    VECTORSDB = "vectorsdb"
    FUNCTIONS = "functions"
    STORAGE = "storage"
