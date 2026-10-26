```python
import asyncio

from appwrite.client import Client
from appwrite.services.advisor import Advisor
from appwrite.models import Report


async def main():
    client = Client()
    client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
    client.set_project('<YOUR_PROJECT_ID>') # Your project ID
    client.set_key('<YOUR_API_KEY>') # Your secret API key

    advisor = Advisor(client)

    result: Report = await advisor.get_report(
        report_id = '<REPORT_ID>'
    )

    print(result.model_dump())


asyncio.run(main())
```
