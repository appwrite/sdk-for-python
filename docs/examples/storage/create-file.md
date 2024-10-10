from appwrite.client import Client
from appwrite.payload import Payload

client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

storage = Storage(client)

result = storage.create_file(
    bucket_id = '<BUCKET_ID>',
    file_id = '<FILE_ID>',
    file = Payload.from_file('/path/to/file.png'),
    permissions = ["read("any")"] # optional
)
