!/bin/sh

user="admin"
password="private"
ip="192.168.0.7"
        
{
sleep 1
echo "$user";     // 登录用户名
sleep 1
echo "$password";     // 登录密码
enbale
configure

interface 1/1
tsn gcl add id 1 gate-states 1,2,3,4,5,6,7 interval 29000
tsn gcl add id 2 gate-states 0 interval 28000
tsn gcl add id 3 gate-states 1,2,3,4,5,6,7 interval 22343000
tsn commit
exit
interface 1/2
tsn gcl add id 1 gate-states 1,2,3,4,5,6,7 interval 29000
tsn gcl add id 2 gate-states 0 interval 28000
tsn gcl add id 3 gate-states 1,2,3,4,5,6,7 interval 22343000
tsn commit
exit

exit
exit
logout
y         
}|telnet $ip
