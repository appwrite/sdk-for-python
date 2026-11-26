from enum import Enum


class MonitorResourceType(Enum):
    PROJECT = "project"
    DATABASE = "database"
    BUCKET = "bucket"
    FUNCTION = "function"
    SITE = "site"
    DEDICATEDDATABASE = "dedicatedDatabase"
    ORGANIZATION = "organization"
