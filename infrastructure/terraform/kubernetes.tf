resource "azurerm_kubernetes_cluster" "thhocomputecluster" {
  name                            = "thhocomputecluster"
  location                        = azurerm_resource_group.resourcegroup.location
  resource_group_name             = azurerm_resource_group.resourcegroup.name
  dns_prefix                      = "thhocomputecluster-dns"
  kubernetes_version              = "1.22.2"
  api_server_authorized_ip_ranges = ["103.143.91.0/24", "188.95.246.0/24"]
  tags                            = {
    intilityImplementationGuid = "notSet",
    intilityManaged            = "FALSE"
  }

  default_node_pool {
    name                = "default"
    vm_size             = "Standard_D2s_v4"
    vnet_subnet_id      = azurerm_subnet.vnsubnet1.id
    enable_auto_scaling = true
    max_count           = 15
    min_count           = 1
    node_labels         = {
      nodePool = "default"
    }
  }

  role_based_access_control {
    enabled = true
    azure_active_directory {
      admin_group_object_ids = [azuread_group.ThomasADGroup.object_id]
      managed = true
      tenant_id = data.azurerm_client_config.current.tenant_id
    }
  }

  service_principal {
    client_id = azuread_application.thhok8clusterapp.application_id
    client_secret = azuread_service_principal_password.thhok8clusterappsppw.value
  }

  addon_profile {
    azure_policy {
      enabled = true
    }

    aci_connector_linux {
      enabled = false
    }

    http_application_routing {
      enabled = false
    }

    kube_dashboard {
      enabled = false
    }

    oms_agent {
      enabled = false
    }
  }
}