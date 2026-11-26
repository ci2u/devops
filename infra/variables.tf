variable "prefix" {
  description = "Short prefix in front of each resource name"
  type        = string
  default     = "devopslab"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "swedencentral"
}

variable "tags" {
  description = "Tags added to every resource"
  type        = map(string)
  default = {
    project     = "aks-devops-lab"
    environment = "lab"
    managed_by  = "terraform"
  }
}