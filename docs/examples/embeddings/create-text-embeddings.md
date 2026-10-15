```python
from appwrite.client import Client
from appwrite.services.embeddings import Embeddings
from appwrite.models import EmbeddingList
from appwrite.enums.embedding_model import EmbeddingModel

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

embeddings = Embeddings(client)

result: EmbeddingList = embeddings.create_text_embeddings(
    texts = ["Appwrite helps developers build applications.", "Find documents with semantic search."],
    model = EmbeddingModel.NOMIC_EMBED_TEXT # optional
)

print(result.model_dump())
```
