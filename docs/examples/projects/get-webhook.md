from appwrite.client import Client
from appwrite.services.projects import Projects

client = Client()

(client
  .set_project('')
  .set_key('')
)

projects = Projects(client)

result = projects.get_webhook('[PROJECT_ID]', '[WEBHOOK_ID]')
