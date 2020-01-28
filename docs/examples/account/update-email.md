from appwrite.client import Client
from appwrite.services.account import Account

client = Client()

(client
  .set_project('')
  .set_key('')
)

account = Account(client)

result = account.update_email('email@example.com', 'password')
