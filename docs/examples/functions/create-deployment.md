from appwrite.client import Client
from appwrite.payload import Payload

client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

functions = Functions(client)

result = functions.create_deployment(
    function_id = '<FUNCTION_ID>',
    code = Payload.from_file('/path/to/file.png'),
    activate = False,
    entrypoint = '<ENTRYPOINT>', # optional
    commands = '<COMMANDS>' # optional
)
