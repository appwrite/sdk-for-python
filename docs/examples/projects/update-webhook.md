from appwrite.client import Client
from appwrite.services.projects import Projects

client = Client()

(client
  .set_project('')
  .set_key('')
)

projects = Projects(client)

result = projects.update_webhook('[PROJECT_ID]', '[WEBHOOK_ID]', '[NAME]', {}, '[URL]', 0)
