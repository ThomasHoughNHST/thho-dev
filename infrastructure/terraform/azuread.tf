resource "azuread_group" "ThomasADGroup" {
  display_name     = "ThomasADGroup"
  mail_enabled     = true
  mail_nickname    = "ThomasADGroup"
  security_enabled = true
  types            = ["Unified"]
  owners = [
    data.azuread_client_config.current.object_id
  ]
  members = [
    data.azuread_client_config.current.object_id
  ]
}

resource "azuread_application" "thhok8clusterapp" {
  display_name = "thhok8clusterapp"
  owners = [data.azuread_client_config.current.object_id]
}

resource "azuread_service_principal" "thhok8clusterappsp" {
  application_id = azuread_application.thhok8clusterapp.application_id
  owners = [data.azuread_client_config.current.object_id]
}

resource "azuread_service_principal_password" "thhok8clusterappsppw" {
  service_principal_id = azuread_service_principal.thhok8clusterappsp.id
}