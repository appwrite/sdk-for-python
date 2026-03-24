from enum import Enum

class VectorsDBIndexType(Enum):
    HNSW_EUCLIDEAN = "hnsw_euclidean"
    HNSW_DOT = "hnsw_dot"
    HNSW_COSINE = "hnsw_cosine"
    OBJECT = "object"
    KEY = "key"
    UNIQUE = "unique"
