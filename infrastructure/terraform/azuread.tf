resource "azuread_group" "HoughADGroup" {
  display_name     = "HoughADGroup"
  mail_enabled     = true
  mail_nickname    = "HoughADGroup"
  security_enabled = true
  types            = ["Unified"]
  owners = [
    data.azuread_client_config.current.object_id
  ]
  members = [
    data.azuread_client_config.current.object_id
  ]
}

resource "azuread_application" "houghk8app" {
  display_name = "houghk8app"
  owners = [data.azuread_client_config.current.object_id]
}

resource "azuread_service_principal" "houghk8appsp" {
  application_id = azuread_application.houghk8app.application_id
  owners = [data.azuread_client_config.current.object_id]
}

resource "azuread_service_principal_password" "houghk8appsppw" {
  service_principal_id = azuread_service_principal.houghk8appsp.id
}