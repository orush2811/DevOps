terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "4.57.0"
    }
  }
}
 module "vgw" {
  source  = "./modules/terraform-azure-vpn-gateway"
  version = "0.1.8"
  location                            = "westeurope"
  name                                = "vgw-azure-gw"
  sku                                 = "VpnGw1"
  subnet_address_prefix               = "192.168.1.0/24"
  type                                = "Vpn"
  virtual_network_name                = azurerm_virtual_network.vnet.name
  virtual_network_resource_group_name = azurerm_virtual_network.vnet.resource_group_name
}

resource "azurerm_virtual_network" "vnet" {
  name                = "vnet-gw-azure"
  address_space       = ["192.168.0.0/16"]
    location            = "westeurope"
    resource_group_name = azurerm_resource_group.rg.name
} 

resource "azurerm_resource_group" "rg" {
  name     = "rg-azure-gw"
  location = "westeurope"
}
