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
  access_key = "AKIAT5RWLVEMHYY6WNYX"
  secret_key = "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"
}
