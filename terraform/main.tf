terraform {
  backend "s3" {
    bucket         = "ors-bucket-cp-cg-state"
    key            = "front-infra-for-cg/terraform.tfstate"
    region         = "eu-north-1"
    encrypt        = true
  }

  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "6.27.0"
    }
  }
}
provider "aws"{
  region = "eu-north-1"
}

module "front-infra-for-cg" {
  source = "./front-infra-for-cg"

  region          = var.aws_region
  owner_tag_value = var.owner_tag_value
  bucket_name     = var.bucket_name
}
