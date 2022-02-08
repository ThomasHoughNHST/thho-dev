#resource "azurerm_mssql_server" "houghserver" {
#  name                         = "houghserver"
#  location                     = azurerm_resource_group.resourcegroup.location
#  resource_group_name          = azurerm_resource_group.resourcegroup.name
#  administrator_login          = "houghadmin"
#  administrator_login_password = random_password.sqlserverpw.result
#  version                      = "12.0"
#  tags = {
#    intilityImplementationGuid = "notSet",
#    intilityManaged = "FALSE"
#  }
#}
#
#resource "azurerm_sql_active_directory_administrator" "server_add" {
#  server_name         = azurerm_mssql_server.houghserver.name
#  resource_group_name = azurerm_resource_group.resourcegroup.name
#  login               = "S_Azure_NHST_Contributor"
#  tenant_id           = data.azurerm_client_config.current.tenant_id
#  object_id           = var.nhst_owner_group_object_id
#}
#
#resource "azurerm_mssql_database" "houghdb" {
#  name      = "houghdb"
#  server_id = azurerm_mssql_server.houghserver.id
#  max_size_gb = 1
#  tags = {
#    intilityImplementationGuid = "notSet",
#    intilityManaged = "FALSE"
#  }
#}