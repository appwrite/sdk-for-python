from enum import Enum


class SupabaseMigrationResource(Enum):
    USER = "user"
    DATABASE = "database"
    TABLE = "table"
    COLUMN = "column"
    INDEX = "index"
    ROW = "row"
    DOCUMENT = "document"
    ATTRIBUTE = "attribute"
    COLLECTION = "collection"
    BUCKET = "bucket"
    FILE = "file"
