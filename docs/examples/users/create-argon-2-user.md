```python
from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.models import User

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

users = Users(client)

result: User = users.create_argon2_user(
    user_id = '<USER_ID>',
    email = 'email@example.com',
    password = '$argon2id$v=19$m=65536,t=4,p=1$NC8xaW1CVXlIZXFSQi9FRg$0bd4pLo1ytyqvCwl5NSijpm5OIe8J6CjZ1vFemKAg+o',
    name = '<NAME>' # optional
)

print(result.model_dump())
```
