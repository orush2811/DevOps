terraform {
  required_providers {
     aws = {
      source  = "hashicorp/aws"
      version = "6.27.0"
    }
  }
}

module "vpn_gw"{
  source = "./modules/terraform-aws-vpn-gateway"
  vpc_id                  = module.vpc.vpc_id
  vpn_gateway_id          = module.vpc.vgw_id
  customer_gateway_id     = module.vpc.cgw_ids[0]
  depends_on = [module.vpc]
  vpc_subnet_route_table_count = 3
  vpc_subnet_route_table_ids   = module.vpc.private_route_table_ids
  create_vpn_connection = true
  vpn_connection_static_routes_only = true
  vpn_connection_static_routes_destinations = ["172.30.113.0/24"]
  local_ipv4_network_cidr = "172.30.113.0/24"
  remote_ipv4_network_cidr = "10.0.0.0/16"
  tunnel1_ike_versions = ["ikev1", "ikev2"]
  tunnel1_phase1_dh_group_numbers = [14]
  tunnel1_phase1_encryption_algorithms = ["AES256"]
  tunnel1_phase1_integrity_algorithms = ["SHA2-256"]
  tunnel1_phase1_lifetime_seconds = 28800
  tunnel1_phase2_dh_group_numbers = [14]
  tunnel1_phase2_encryption_algorithms = ["AES256"]
  tunnel1_phase2_integrity_algorithms = ["SHA2-256"]
  tunnel1_phase2_lifetime_seconds = 3600
  tunnel1_preshared_key = "TheSecretisnone"
}

module "vpc" {
  source          = "./modules/terraform-aws-vpc"
  name            = "my-vpc-1"
  cidr            = "10.0.0.0/16"
  azs             = ["eu-west-1a", "eu-west-1b", "eu-west-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
  enable_nat_gateway = false
  enable_vpn_gateway = true

customer_gateways = {
    IP1 = {
      ip_address = "194.29.43.78"
    }
  }

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}
