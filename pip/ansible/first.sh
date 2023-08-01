#!/bin/bash


##
ansible all --list-hosts
ansible all -m ping 

##
ansible-inventory -i inventory.yaml --list
ansible vms -i inventory.yaml -m ping
