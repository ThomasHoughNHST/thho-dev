terraform {
  backend "azurerm" {
    resource_group_name = "tfstateresourcegroup"
    storage_account_name = "thhotfstatesa"
    container_name = "thhotfstateblob"
    key = "terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
}

provider "random" {
}

data "azurerm_client_config" "current" {}

resource "random_password" "thhopwd" {
  length  = 24
  special = false
}

resource "random_password" "sqlserverpw" {
  length  = 24
  special = false
}

resource "azurerm_resource_group" "resourcegroup" {
  name          = "thho_resourcegroup"
  location      = "West Europe"
  tags = {
    intilityImplementationGuid = "notSet",
    intilityManaged = "FALSE"
  }
}

# Virtual network
resource "azurerm_virtual_network" "virtualnetwork" {
  name                = "thho_vnet1"
  location            = azurerm_resource_group.resourcegroup.location
  resource_group_name = azurerm_resource_group.resourcegroup.name
  address_space       = ["10.1.0.0/24"]
  tags = {
    intilityImplementationGuid = "notSet",
    intilityManaged = "FALSE"
  }
}

resource "azurerm_subnet" "vnsubnet1" {
  address_prefixes          = ["10.1.0.0/24"]
  name                      = "thho_subnet1"
  resource_group_name       = azurerm_resource_group.resourcegroup.name
  virtual_network_name      = azurerm_virtual_network.virtualnetwork.name
  service_endpoints         = ["Microsoft.KeyVault", "Microsoft.Sql", "Microsoft.Storage"]
}

# Storage Account and file storage
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
}

resource "azurerm_storage_share" "inputs" {
  name                 = "input-files"
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

# Key vault
resource "azurerm_key_vault" "keyvault" {
  name                        = "thhokeyvault2"
  location                    = azurerm_resource_group.resourcegroup.location
  resource_group_name         = azurerm_resource_group.resourcegroup.name
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  soft_delete_retention_days  = 7
  sku_name = "standard"
  tags = {
    intilityImplementationGuid = "notSet",
    intilityManaged = "FALSE"
  }
  access_policy {
  tenant_id = data.azurerm_client_config.current.tenant_id
  object_id = "c8c603f5-95a2-4d06-8bc9-6d00c4dc325c"

    key_permissions = [
      "Get",
      "List",
      "Update",
      "Create",
      "Import",
      "Delete",
      "Recover",
      "Backup",
      "Restore",
      "Purge"
    ]

    secret_permissions = [
      "Get",
      "List",
      "Set",
      "Delete",
      "Recover",
      "Backup",
      "Restore",
      "Purge"
    ]

    certificate_permissions = [
      "Get",
      "List",
      "Update",
      "Create",
      "Import",
      "Delete",
      "Recover",
      "Backup",
      "Restore",
      "ManageContacts",
      "ManageIssuers",
      "GetIssuers",
      "ListIssuers",
      "SetIssuers",
      "DeleteIssuers",
      "Purge"
    ]
  }
  access_policy {
  tenant_id = data.azurerm_client_config.current.tenant_id
  object_id = "198361a5-f57e-45d4-b4e8-13cd19df09b6"

    key_permissions = [
      "Get",
      "List",
      "Create"
    ]

    secret_permissions = [
      "Get",
      "List",
      "Set"
    ]

    certificate_permissions = [
      "Get",
      "List",
      "Create"
    ]
  }
}

resource "azurerm_key_vault_secret" "thhoconstr" {
  name         = "thho-sql-db-connection-string"
  value        = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:${azurerm_mssql_server.server.fully_qualified_domain_name},1433;Database=${azurerm_mssql_database.db.name};Uid=${azurerm_mssql_server.server.administrator_login};Pwd=${random_password.sqlserverpw.result};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
  key_vault_id = azurerm_key_vault.keyvault.id
}

resource "azurerm_key_vault_secret" "thhosecret" {
  key_vault_id = azurerm_key_vault.keyvault.id
  name         = "PWD"
  value        = random_password.thhopwd.result
}

# Database
resource "azurerm_mssql_server" "server" {
  name                         = "thhoserver"
  location                     = azurerm_resource_group.resourcegroup.location
  resource_group_name          = azurerm_resource_group.resourcegroup.name
  administrator_login          = "thomasadmin"
  administrator_login_password = random_password.sqlserverpw.result
  version                      = "12.0"
  tags = {
    intilityImplementationGuid = "notSet",
    intilityManaged = "FALSE"
  }
}

resource "azurerm_sql_active_directory_administrator" "server_add" {
  server_name         = azurerm_mssql_server.server.name
  resource_group_name = azurerm_resource_group.resourcegroup.name
  login               = "S_Azure_NHST_Owner"
  tenant_id           = data.azurerm_client_config.current.tenant_id
  object_id           = data.azurerm_client_config.current.object_id
}

resource "azurerm_mssql_database" "db" {
  name      = "thhosqldatabase"
  server_id = azurerm_mssql_server.server.id
  max_size_gb = 1
  tags = {
    intilityImplementationGuid = "notSet",
    intilityManaged = "FALSE"
  }
}


