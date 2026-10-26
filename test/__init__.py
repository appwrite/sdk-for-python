import httpx2

# Point `import httpx` at httpx2 so respx patches the transport the SDK actually uses.
httpx2.alias_httpx()
