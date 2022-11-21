# Terraform Settings Block
terraform {
  required_version = "~> 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }
}

# Provider Block
provider "aws" {
  region     = "us-east-2"
  access_key = ""
  secret_key = ""
}
