module "apim" {
  source      = "./modules/apim"
  rg_name     = var.rg_name
  apim_name   = var.apim_name
}

module "functions" {
  source                  = "./modules/functionapp"
  rg_name                 = var.rg_name
  function_name           = var.function_name
}
