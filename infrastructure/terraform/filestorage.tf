resource "azurerm_storage_account" "houghsa" {
  name                     = "houghsa"
  resource_group_name      = azurerm_resource_group.resourcegroup.name
  location                 = azurerm_resource_group.resourcegroup.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  tags = {
    intilityImplementationGuid = "notSet",
    intilityManaged = "FALSE"
  }
  allow_blob_public_access = true
}

resource "azurerm_storage_share" "mongodbfiles" {
  name                 = "mongodb"
  storage_account_name = azurerm_storage_account.houghsa.name
  quota                = 100
  acl {
    id = "mongodbacl"
    access_policy {
      permissions = "rwdl"
      start       = "2022-02-10T00:00:00.0000000Z"
      expiry      = "2023-02-10T00:00:00.0000000Z"
    }
  }
  acl {
    id = azuread_service_principal.houghk8appsp.id
    access_policy {
      permissions = "rwdl"
      start       = "2022-02-10T00:00:00.0000000Z"
      expiry      = "2023-02-10T00:00:00.0000000Z"
    }
  }
}

resource "azurerm_key_vault_secret" "storageaccountname" {
  name         = "houghsa-storage-account-name"
  value        = azurerm_storage_account.houghsa.name
  key_vault_id = azurerm_key_vault.houghkeyvault.id
}

resource "azurerm_key_vault_secret" "storageaccountkey" {
  name         = "houghsa-storage-account-access-key"
  value        = azurerm_storage_account.houghsa.primary_access_key
  key_vault_id = azurerm_key_vault.houghkeyvault.id
}

resource "azurerm_storage_account_network_rules" "mongonr" {
  storage_account_id = azurerm_storage_account.houghsa.id
  default_action             = "Allow"
  ip_rules                   = ["127.0.0.1"]
  virtual_network_subnet_ids = [azurerm_subnet.houghsubnet1.id]
  bypass                     = ["Metrics"]
}

resource "azurerm_storage_share_directory" "data" {
  name                 = "data"
  share_name           = azurerm_storage_share.mongodbfiles.name
  storage_account_name = azurerm_storage_account.houghsa.name
}

resource "azurerm_storage_share_directory" "db" {
  name                 = "${azurerm_storage_share_directory.data.name}/db"
  share_name           = azurerm_storage_share.mongodbfiles.name
  storage_account_name = azurerm_storage_account.houghsa.name
}

resource "azurerm_storage_share" "airflowlogs" {
  name                 = "airflow-logs"
  storage_account_name = azurerm_storage_account.houghsa.name
  quota                = 100
}

resource "azurerm_storage_share" "airflowdags" {
  name                 = "airflow-dags"
  storage_account_name = azurerm_storage_account.houghsa.name
  quota                = 50
}