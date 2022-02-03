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

provider "azuread" {
}

provider "random" {
}

data "azurerm_client_config" "current" {}

data "azuread_client_config" "current" {}

resource "random_password" "thhopwd" {
  length  = 24
  special = false
}

resource "random_password" "sqlserverpw" {
  length  = 24
  special = false
}

resource "random_password" "k8pw" {
  length = 24
  special = true
}

resource "random_password" "posgrespwd" {
  length  = 24
  special = true
}

resource "azurerm_resource_group" "resourcegroup" {
  name          = "thhoresourcegroup"
  location      = "West Europe"
  tags = {
    intilityImplementationGuid = "notSet",
    intilityManaged = "FALSE"
  }
}







