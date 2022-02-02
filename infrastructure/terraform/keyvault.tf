resource "azurerm_key_vault" "keyvault" {
  name                        = "thhokeyvault"
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
  object_id = var.nhst_owner_group_object_id

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