# Deploying this app

## What you need
Terraform
An openstack cloud account of some sort, with the openrc file from that account.
 - include a keypair named KP1
Packer

## Steps

```sh
packer build django_image.json
terraform init
terraform apply
```