#resource "azurerm_postgresql_server" "houghposgres" {
#  name                = "houghposgres"
#  location            = azurerm_resource_group.resourcegroup.location
#  resource_group_name = azurerm_resource_group.resourcegroup.name
#  sku_name = "GP_Gen5_2"
#  storage_mb                   = 5120
#  backup_retention_days        = 7
#  geo_redundant_backup_enabled = false
#  administrator_login          = "psqladminun"
#  administrator_login_password = random_password.posgrespwd.result
#  version                      = "11"
#  ssl_enforcement_enabled      = true
#  tags = {
#    intilityImplementationGuid = "notSet",
#    intilityManaged = "FALSE"
#  }
#}
#
#resource "azurerm_postgresql_firewall_rule" "nhstofficefw" {
#  name                = "nhst-office"
#  resource_group_name = azurerm_resource_group.resourcegroup.name
#  server_name         = azurerm_postgresql_server.houghposgres.name
#  start_ip_address    = "31.45.107.203"
#  end_ip_address      = "31.45.107.203"
#}
#
#resource "azurerm_postgresql_virtual_network_rule" "networkrule" {
#  name                                 = "postgresql-vnet-rule"
#  resource_group_name                  = azurerm_resource_group.resourcegroup.name
#  server_name                          = azurerm_postgresql_server.houghposgres.name
#  subnet_id                            = azurerm_subnet.houghsubnet1.id
#  ignore_missing_vnet_service_endpoint = true
#}