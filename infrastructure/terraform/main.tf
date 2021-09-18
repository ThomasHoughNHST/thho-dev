provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "resourcegroup" {
  name          = "thho_resourcegroup"
  location      = "West Europe"
}

resource "azurerm_virtual_network" "virtualnetwork" {
  name                = "thho_vnet1"
  location            = azurerm_resource_group.resourcegroup.location
  resource_group_name = azurerm_resource_group.resourcegroup.name
  address_space       = ["10.1.0.0/16"]
}

resource "azurerm_subnet" "vnsubnet1" {
  address_prefixes          = ["10.1.0.0/16"]
  name                      = "thho_subnet1"
  resource_group_name       = azurerm_resource_group.resourcegroup.name
  virtual_network_name      = azurerm_virtual_network.virtualnetwork.name
  service_endpoints         = ["Microsoft.KeyVault", "Microsoft.Sql", "Microsoft.Storage"]
}