from appwrite.client import Client
from appwrite.services.backups import Backups

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

backups = Backups(client)

result = backups.update_policy(
    policy_id = '<POLICY_ID>',
    name = '<NAME>', # optional
    retention = 1, # optional
    schedule = '', # optional
    enabled = False # optional
)
