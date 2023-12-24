data "azurerm_resource_group" "rg" {
  name     = var.rg_name
}

resource "azurerm_storage_account" "storage" {
  name                     = "httptrigger2023"
  resource_group_name      = data.azurerm_resource_group.rg.name
  location                 = data.azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_service_plan" "svcplan" {
  name                = "svcplanhttp"
  resource_group_name = data.azurerm_resource_group.rg.name
  location            = data.azurerm_resource_group.rg.location
  os_type             = "Linux"
  sku_name            = "Y1"
}

resource "azurerm_linux_function_app" "function" {
  name                = var.function_name
  resource_group_name = data.azurerm_resource_group.rg.name
  location            = data.azurerm_resource_group.rg.location

  storage_account_name       = resource.azurerm_storage_account.storage.name
  storage_account_access_key = resource.azurerm_storage_account.storage.primary_access_key
  service_plan_id            = resource.azurerm_service_plan.svcplan.id

  site_config {
    application_stack {
        python_version = "3.11"      
    }
  }
}
