locals {
  tags = {
    Name      = "State bucket"
    Owner     = var.owner_tag_value
    Terraform = "True"
  }
}

module "state_bucket" {
 source = "../../terraform-aws-s3-bucket"
}

module "cg-host-ec2-machine" {
source = "../../terraform-aws-ec2-instance"
}

module "cg-cp-aws"{
source = "../../terraform-aws-cloudguard-network-security"
}

module "cg-vpc-aws"{
  source = "../../terraform-aws-vpc"
}
