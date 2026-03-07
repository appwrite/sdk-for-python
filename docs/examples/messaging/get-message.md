```python
from appwrite.client import Client
from appwrite.services.messaging import Messaging
from appwrite.models import Message

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

messaging = Messaging(client)

result: Message = messaging.get_message(
    message_id = '<MESSAGE_ID>'
)

print(result.model_dump())
```
