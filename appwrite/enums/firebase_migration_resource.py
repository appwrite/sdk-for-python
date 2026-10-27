from enum import Enum


class FirebaseMigrationResource(Enum):
    USER = "user"
    DATABASE = "database"
    TABLE = "table"
    COLUMN = "column"
    ROW = "row"
    DOCUMENT = "document"
    ATTRIBUTE = "attribute"
    COLLECTION = "collection"
    BUCKET = "bucket"
    FILE = "file"
