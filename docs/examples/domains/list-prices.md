```python
from appwrite.client import Client
from appwrite.services.domains import Domains
from appwrite.models import DomainPricesList
from appwrite.enums.domain_registration_type import DomainRegistrationType

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

domains = Domains(client)

result: DomainPricesList = domains.list_prices(
    domains = [],
    period_years = None, # optional
    registration_type = DomainRegistrationType.NEW # optional
)

print(result.model_dump())
```
