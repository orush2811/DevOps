variable "aws_region" {
  description = "The AWS region to deploy resources in."
  type        = string
  default     = "eu-north-1"
}

variable "owner_tag_value" {
  description = "The value for the owner tag."
  type        = string
  default     = "Or Itach" 
}

variable "bucket_name" {
  description = "Unique S3 bucket name."
  type        = string
  default     = "ors-bucket-cp-cg"
}