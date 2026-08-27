```python
from appwrite.client import Client
from appwrite.services.sites import Sites
from appwrite.models import Site
from appwrite.enums import Framework
from appwrite.enums import BuildRuntime
from appwrite.enums import Adapter
from appwrite.enums import ProjectKeyScopes

client = Client()
client.set_endpoint('https://<REGION>.cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

sites = Sites(client)

result: Site = sites.update(
    site_id = '<SITE_ID>',
    name = '<NAME>',
    framework = Framework.ANALOG,
    enabled = False, # optional
    logging = False, # optional
    timeout = 1, # optional
    install_command = '<INSTALL_COMMAND>', # optional
    build_command = '<BUILD_COMMAND>', # optional
    start_command = '<START_COMMAND>', # optional
    output_directory = '<OUTPUT_DIRECTORY>', # optional
    build_runtime = BuildRuntime.NODE_14_5, # optional
    adapter = Adapter.STATIC, # optional
    fallback_file = '<FALLBACK_FILE>', # optional
    installation_id = '<INSTALLATION_ID>', # optional
    provider_repository_id = '<PROVIDER_REPOSITORY_ID>', # optional
    provider_branch = '<PROVIDER_BRANCH>', # optional
    provider_silent_mode = False, # optional
    provider_root_directory = '<PROVIDER_ROOT_DIRECTORY>', # optional
    provider_branches = [], # optional
    provider_paths = [], # optional
    build_specification = 's-1vcpu-512mb', # optional
    runtime_specification = 's-1vcpu-512mb', # optional
    deployment_retention = 0, # optional
    scopes = [ProjectKeyScopes.PROJECT_READ] # optional
)

print(result.model_dump())
```
