resource "azurerm_storage_account" "filestorage" {
  name                     = "thhofilestorage"
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
  storage_account_name = azurerm_storage_account.filestorage.name
  quota                = 100
}

resource "azurerm_storage_share" "airflowlogs" {
  name                 = "airflow-logs"
  storage_account_name = azurerm_storage_account.filestorage.name
  quota                = 100
}

resource "azurerm_storage_share" "airflowdags" {
  name                 = "airflow-dags"
  storage_account_name = azurerm_storage_account.filestorage.name
  quota                = 50
}