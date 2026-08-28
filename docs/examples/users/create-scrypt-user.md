```python
from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.models import User

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

users = Users(client)

result: User = users.create_scrypt_user(
    user_id = '<USER_ID>',
    email = 'email@example.com',
    password = 'password',
    password_salt = '<PASSWORD_SALT>',
    password_cpu = 8,
    password_memory = 65536,
    password_parallel = 1,
    password_length = 64,
    name = '<NAME>' # optional
)

print(result.model_dump())
```
