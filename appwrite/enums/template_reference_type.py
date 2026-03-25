from enum import Enum

class TemplateReferenceType(Enum):
    COMMIT = "commit"
    BRANCH = "branch"
    TAG = "tag"
