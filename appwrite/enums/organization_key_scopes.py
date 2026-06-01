from enum import Enum

class OrganizationKeyScopes(Enum):
    PROJECTS_READ = "projects.read"
    PROJECTS_WRITE = "projects.write"
    DEVKEYS_READ = "devKeys.read"
    DEVKEYS_WRITE = "devKeys.write"
    ORGANIZATION_KEYS_READ = "organization.keys.read"
    ORGANIZATION_KEYS_WRITE = "organization.keys.write"
    DOMAINS_READ = "domains.read"
    DOMAINS_WRITE = "domains.write"
    KEYS_READ = "keys.read"
    KEYS_WRITE = "keys.write"
