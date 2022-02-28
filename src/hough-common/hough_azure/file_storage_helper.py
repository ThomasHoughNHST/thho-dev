import os
from hough_azure.keyvault import KeyVault


def get_file_storage_helper():
    return FileStorageHelper(os.getenv("NHST_ENVIRONMENT", default="hough_azure"))


class FileStorageHelper:
    def __init__(self, environment=None):
        self._environment = environment
        self.client_id = os.getenv('NHST_SP_CLIENT_ID', "Variable not defined")
        self.client_secret = os.getenv('NHST_SP_SECRET', "Variable not defined")
        self.tenant_id = os.getenv('NHST_TENANT', "Variable not defined")
        self.keyvault_uri = os.getenv('NHST_KEYVAULT_URI', "Variable not defined")

    def get_keyvault(self):
        print(f'environment: {self._environment}')
        print(f'client_id: {self.client_id}')
        print(f'client_secret: {self.client_secret}')
        print(f'tenant_id: {self.tenant_id}')
        print(f'keyvault_uri: {self.keyvault_uri}')
        return KeyVault(self.client_id,
                        self.client_secret,
                        self.tenant_id,
                        self.keyvault_uri)
