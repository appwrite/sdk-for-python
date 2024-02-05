from enum import Enum

class RelationMutate(Enum):
    CASCADE = "cascade"
    RESTRICT = "restrict"
    SETNULL = "setNull"
