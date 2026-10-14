```python
from appwrite.client import Client
from appwrite.services.domains import Domains
from appwrite.models import DnsRecordsList

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

domains = Domains(client)

result: DnsRecordsList = domains.create_preset_proton_mail(
    domain_id = '<DOMAIN_ID>'
)

print(result.model_dump())
```
