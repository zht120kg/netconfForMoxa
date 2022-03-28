!/bin/sh

user="admin"
password="private"
ip="192.168.0.7"
sshpass -p $password ssh $user@$ip  <<remotessh  

enbale
configure

interface 1/1
tsn delete all
tsn gates operation enable
tsn cycle-time 22400000
tsn gcl add id 1 gate-states 1,2,3,4,5,6,7 interval 29000
tsn gcl add id 2 gate-states 0 interval 28000
tsn gcl add id 3 gate-states 1,2,3,4,5,6,7 interval 22343000
tsn commit
exit
interface 1/2
tsn delete all
tsn gates operation enable
tsn cycle-time 22400000
tsn gcl add id 1 gate-states 1,2,3,4,5,6,7 interval 29000
tsn gcl add id 2 gate-states 0 interval 28000
tsn gcl add id 3 gate-states 1,2,3,4,5,6,7 interval 22343000
tsn commit
exit

exit
save
exit
logout
y

remotessh
