# Appwrite Python SDK

![License](https://img.shields.io/github/license/appwrite/sdk-for-python.svg?style=flat-square)
![Version](https://img.shields.io/badge/api%20version-1.9.1-blue.svg?style=flat-square)
[![Build Status](https://img.shields.io/travis/com/appwrite/sdk-generator?style=flat-square)](https://travis-ci.com/appwrite/sdk-generator)
[![Twitter Account](https://img.shields.io/twitter/follow/appwrite?color=00acee&label=twitter&style=flat-square)](https://twitter.com/appwrite)
[![Discord](https://img.shields.io/discord/564160730845151244?label=discord&style=flat-square)](https://appwrite.io/discord)

**This SDK is compatible with Appwrite server version 1.9.x. For older versions, please check [previous releases](https://github.com/appwrite/sdk-for-python/releases).**

Appwrite is an open-source backend as a service server that abstracts and simplifies complex and repetitive development tasks behind a very simple to use REST API. Appwrite aims to help you develop your apps faster and in a more secure way. Use the Python SDK to integrate your app with the Appwrite server to easily start interacting with all of Appwrite backend APIs and tools. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

![Appwrite](https://github.com/appwrite/appwrite/raw/main/public/images/github.png)

## Installation

To install via [PyPI](https://pypi.org/):

```bash
pip install appwrite
```

Or with `uv`:

```bash
uv add appwrite
```


## Getting Started

### Init your SDK
Initialize your SDK with your Appwrite server API endpoint and project ID which can be found on your project settings page and your new API secret Key from project's API keys section.

```python
from appwrite.client import Client
from appwrite.services.users import Users

client = Client()

(client
  .set_endpoint('https://[HOSTNAME_OR_IP]/v1') # Your API Endpoint
  .set_project('5df5acd0d48c2') # Your project ID
  .set_key('919c2d18fb5d4...a2ae413da83346ad2') # Your secret API key
  .set_self_signed() # Use only on dev mode with a self-signed SSL cert
)
```

### Make Your First Request
Once your SDK object is set, create any of the Appwrite service objects and choose any request to send. Full documentation for any service method you would like to use can be found in your SDK documentation or in the [API References](https://appwrite.io/docs) section.

All service methods return typed Pydantic models, so you can access response fields as attributes:

```python
users = Users(client)

user = users.create(ID.unique(), email = "email@example.com", phone = "+123456789", password = "password", name = "Walter O'Brien")

print(user.name)   # "Walter O'Brien"
print(user.email)  # "email@example.com"
print(user.id)     # The generated user ID
```

### Full Example
```python
from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.id import ID

client = Client()

(client
  .set_endpoint('https://[HOSTNAME_OR_IP]/v1') # Your API Endpoint
  .set_project('5df5acd0d48c2') # Your project ID
  .set_key('919c2d18fb5d4...a2ae413da83346ad2') # Your secret API key
  .set_self_signed() # Use only on dev mode with a self-signed SSL cert
)

users = Users(client)

user = users.create(ID.unique(), email = "email@example.com", phone = "+123456789", password = "password", name = "Walter O'Brien")

print(user.name)       # Access fields as attributes
print(user.to_dict())  # Convert to dictionary if needed
```

### Type Safety with Models

The Appwrite Python SDK provides type safety when working with database rows through generic methods. Methods like `get_row`, `list_rows`, and others accept a `model_type` parameter that allows you to specify your custom Pydantic model for full type safety.

```python
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from appwrite.client import Client
from appwrite.services.tables_db import TablesDB

# Define your custom model matching your table schema
class Post(BaseModel):
    postId: int
    authorId: int
    title: str
    content: str
    createdAt: datetime
    updatedAt: datetime
    isPublished: bool
    excerpt: Optional[str] = None

client = Client()
# ... configure your client ...

tables_db = TablesDB(client)

# Fetch a single row with type safety
row = tables_db.get_row(
    database_id="your-database-id",
    table_id="your-table-id",
    row_id="your-row-id",
    model_type=Post  # Pass your custom model type
)

print(row.data.title)     # Fully typed - IDE autocomplete works
print(row.data.postId)    # int type, not Any
print(row.data.createdAt) # datetime type

# Fetch multiple rows with type safety
result = tables_db.list_rows(
    database_id="your-database-id",
    table_id="your-table-id",
    model_type=Post
)

for row in result.rows:
    print(f"{row.data.title} by {row.data.authorId}")
```

### Error Handling
The Appwrite Python SDK raises `AppwriteException` object with `message`, `code` and `response` properties. You can handle any errors by catching `AppwriteException` and present the `message` to the user or handle it yourself based on the provided error information. Below is an example.

```python
users = Users(client)
try:
  user = users.create(ID.unique(), email = "email@example.com", phone = "+123456789", password = "password", name = "Walter O'Brien")
  print(user.name)
except AppwriteException as e:
  print(e.message)
```

### Learn more
You can use the following resources to learn more and get help
- 🚀 [Getting Started Tutorial](https://appwrite.io/docs/getting-started-for-server)
- 📜 [Appwrite Docs](https://appwrite.io/docs)
- 💬 [Discord Community](https://appwrite.io/discord)
- 🚂 [Appwrite Python Playground](https://github.com/appwrite/playground-for-python)


## Contribution

This library is auto-generated by Appwrite custom [SDK Generator](https://github.com/appwrite/sdk-generator). To learn more about how you can help us improve this SDK, please check the [contribution guide](https://github.com/appwrite/sdk-generator/blob/master/CONTRIBUTING.md) before sending a pull-request.

## License

Please see the [BSD-3-Clause license](https://raw.githubusercontent.com/appwrite/appwrite/master/LICENSE) file for more information.
