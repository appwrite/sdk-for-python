from appwrite.client import Client
from appwrite.enums import AuthenticatorType
from appwrite.services.account import Account


client = Client()

client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint

client.set_project('5df5acd0d48c2') # Your project ID

client.set_session('') # The user session to authenticate with

account = Account(client)

result = account.create_mfa_authenticator(
    type = AuthenticatorType.TOTP
)
