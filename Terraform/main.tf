module "apim" {
  source      = "./modules//apim"
  rg_name     = var.rg_name
  location    = var.location
  apim_name   = var.apim_name
}

module "functions" {
  source                  = "./modules/functionapp"
  rg_name                 = var.rg_name
  location                = var.location
  storage_account_name    = "functiontriggerhttpxxx"
  service_plan_name       = "svcplanhttp"
  function_name           = var.function_name
}
