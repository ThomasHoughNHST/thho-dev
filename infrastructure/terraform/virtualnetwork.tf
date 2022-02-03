resource "azurerm_virtual_network" "thhovn" {
  name                = "thho_vnet1"
  location            = azurerm_resource_group.resourcegroup.location
  resource_group_name = azurerm_resource_group.resourcegroup.name
  address_space       = ["10.1.0.0/24"]
  tags = {
    intilityImplementationGuid = "notSet",
    intilityManaged = "FALSE"
  }
}

resource "azurerm_subnet" "thhosubnet1" {
  address_prefixes          = ["10.1.0.0/24"]
  name                      = "thho_subnet1"
  resource_group_name       = azurerm_resource_group.resourcegroup.name
  virtual_network_name      = azurerm_virtual_network.thhovn.name
  service_endpoints         = ["Microsoft.KeyVault", "Microsoft.Sql", "Microsoft.Storage"]
}