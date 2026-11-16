```python
from appwrite.client import Client
from appwrite.services.project import Project
from appwrite.models import Project as ProjectModel
from appwrite.enums.project_ldap_encryption import ProjectLDAPEncryption

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

project = Project(client)

result: ProjectModel = project.update_ldap(
    enabled = False, # optional
    hosts = ["ldap.example.com"], # optional
    port = 636, # optional
    encryption = ProjectLDAPEncryption.NONE, # optional
    verification = False, # optional
    certificate = '<CERTIFICATE>', # optional
    timeout = 10, # optional
    base_dn = 'ou=people,dc=example,dc=com', # optional
    bind_dn = 'cn=appwrite,ou=services,dc=example,dc=com', # optional
    bind_password = 'password', # optional
    user_filter = '(uid={username})', # optional
    required_group_dn = 'cn=staff,ou=groups,dc=example,dc=com', # optional
    id_attribute = 'entryUUID', # optional
    email_attribute = 'mail', # optional
    name_attribute = 'cn', # optional
    phone_attribute = 'mobile' # optional
)

print(result.model_dump())
```
