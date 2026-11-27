```python
from appwrite.client import Client
from appwrite.services.analytics import Analytics
from appwrite.models import AnalyticsMetricList
from appwrite.enums.analytics_interval import AnalyticsInterval
from appwrite.enums.analytics_dimension import AnalyticsDimension

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

analytics = Analytics(client)

result: AnalyticsMetricList = analytics.list_metrics(
    property_id = '<PROPERTY_ID>',
    queries = [], # optional
    interval = AnalyticsInterval.ONE_HOUR, # optional
    dimensions = [AnalyticsDimension.COUNTRY], # optional
    prop_key = '<PROP_KEY>', # optional
    date_range = '<DATE_RANGE>', # optional
    start_at = '2020-10-15T06:38:00.000+00:00', # optional
    end_at = '2020-10-15T06:38:00.000+00:00', # optional
    limit = 1, # optional
    total = False # optional
)

print(result.model_dump())
```
