```python
from appwrite.client import Client
from appwrite.services.waf import Waf
from appwrite.models import WafRuleBypass
from appwrite.models import WafRuleDeny
from appwrite.models import WafRuleChallenge
from appwrite.models import WafRuleRateLimit
from appwrite.models import WafRuleRedirect
from typing import Union

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

waf = Waf(client)

result: Union[WafRuleBypass, WafRuleDeny, WafRuleChallenge, WafRuleRateLimit, WafRuleRedirect] = waf.get_rule(
    rule_id = '<RULE_ID>'
)

print(result.model_dump())
```
