```python
from appwrite.client import Client
from appwrite.services.waf import Waf
from appwrite.models import WafRuleRateLimit

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

waf = Waf(client)

result: WafRuleRateLimit = waf.update_rate_limit_rule(
    rule_id = '<RULE_ID>',
    resource_type = 'api', # optional
    resource_id = '<RESOURCE_ID>', # optional
    name = '<NAME>', # optional
    description = '<DESCRIPTION>', # optional
    limit = 1, # optional
    interval = 1, # optional
    key = 'ip', # optional
    max_bucket_size = 1, # optional
    priority = -100000, # optional
    enabled = False, # optional
    conditions = [] # optional
)

print(result.model_dump())
```
