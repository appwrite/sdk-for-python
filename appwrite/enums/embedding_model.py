from enum import Enum

class EmbeddingModel(Enum):
    NOMIC_EMBED_TEXT = "nomic-embed-text"
    EMBEDDING_GEMMA = "embedding-gemma"
    ALL_MINILM = "all-minilm"
    BGE_SMALL = "bge-small"
