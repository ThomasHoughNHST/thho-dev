from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient


class KeyVault:

    def __init__(self, client_id, client_secret, tenant_id, vault_uri):
        self.__client = SecretClient(vault_url=vault_uri,
                                     credential=ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret))

    def get_secret(self, secret_key):
        secret = self.__client.get_secret(secret_key)
        return secret.value

    def add_secret(self, key, value):
        self.__client.set_secret(key, value)