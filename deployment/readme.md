# Deploying this app

Warning: Work in progress, there is more work that needs to be done

The terraform script currently does not use the ami created from packer
The packer file needs to use cron instead of /etc/init.d
The provisioned instance needs a way to know its own host name so that it can be added to ALLOWED_HOSTS


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