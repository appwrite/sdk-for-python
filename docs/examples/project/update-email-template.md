```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import EmailTemplate
from appwrite.enums import ProjectEmailTemplateId
from appwrite.enums import ProjectEmailTemplateLocale

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: EmailTemplate = project.update_email_template(
    template_id = ProjectEmailTemplateId.VERIFICATION,
    locale = ProjectEmailTemplateLocale.AF, # optional
    subject = '<SUBJECT>', # optional
    message = '<MESSAGE>', # optional
    sender_name = '<SENDER_NAME>', # optional
    sender_email = 'email@example.com', # optional
    reply_to_email = 'email@example.com', # optional
    reply_to_name = '<REPLY_TO_NAME>' # optional
)

print(result.model_dump())
```
