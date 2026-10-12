```python
from appwrite.client import Client
from appwrite.services.waf import Waf
from appwrite.models import WafRuleChallenge

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

waf = Waf(client)

result: WafRuleChallenge = waf.update_challenge_rule(
    rule_id = '<RULE_ID>',
    resource_type = 'api', # optional
    resource_id = '<RESOURCE_ID>', # optional
    name = '<NAME>', # optional
    description = '<DESCRIPTION>', # optional
    challenge_type = 'compute', # optional
    priority = -100000, # optional
    enabled = False, # optional
    conditions = [], # optional
    difficulty = 1, # optional
    ttl = 900 # optional
)

print(result.model_dump())
```
