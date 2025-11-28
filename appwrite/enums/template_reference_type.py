from enum import Enum

class TemplateReferenceType(Enum):
    BRANCH = "branch"
    COMMIT = "commit"
    TAG = "tag"
