terraform {
  required_providers {
    openstack = {
      source = "terraform-provider-openstack/openstack"
    }
  }
}

# Configure the OpenStack Provider (use only defaults, as that takes from your personal openrc file)
provider "openstack" {
}

resource "openstack_compute_secgroup_v2" "public" {
  name = "public_secgroup"
  description = "my security group"
  rule {
    from_port = 22
    to_port = 22
    ip_protocol = "tcp"
    cidr = "0.0.0.0/0"
  }
  rule {
    from_port = 8000
    to_port = 8000
    ip_protocol = "tcp"
    cidr = "0.0.0.0/0"
  }
  rule {
    from_port = 22
    to_port = 22
    ip_protocol = "tcp"
    cidr = "::/0"
  }
  rule {
    from_port = 8000
    to_port = 8000
    ip_protocol = "tcp"
    cidr = "::/0"
  }
}

resource "openstack_compute_instance_v2" "main_instance" {
  name = "main_instance"
  image_name = "Ubuntu 18.04"
  flavor_name = "m1.small"
  security_groups = [ openstack_compute_secgroup_v2.public.name ]
  user_data = file("bootstrap.sh")
  key_pair = "KP1"
}