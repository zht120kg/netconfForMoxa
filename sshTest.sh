#!/bin/bash  

user="admin"
password="private"
ip="192.168.0.6"

sshpass -p $password ssh $user@$ip  <<remotessh

enable
configure
show tsn configuration

interface 1/1
tsn delete all
tsn gates operation enable
tsn cycle-time xxxx


remotessh