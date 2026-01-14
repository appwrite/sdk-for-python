from appwrite.client import Client
from appwrite.services.organizations import Organizations

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

organizations = Organizations(client)

result = organizations.estimation_delete_organization(
    organization_id = '<ORGANIZATION_ID>'
)
