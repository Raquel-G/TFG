#!/usr/bin/env python
from subprocess import Popen, PIPE

#INTERN NETWORK MAP

ipaddr = "192.168.1.24"
netmask = "255.255.255.0"

ip_list = []

def cidr32(ip):
    map_network = Popen(['ping', '-c 1', ip])
    stdoutdata, stderrdata = map_network.communicate()

def cidr24(ip):
    for fourth_octet in range(1,254):
        iploop = ip + str(fourth_octet)
        map_network = Popen(['ping', '-c 1', iploop], stdin=PIPE, stdout=PIPE)
        
        stdout, stderrdata = map_network.communicate(input=None)
        #print iploop
        if "Host de destino inaccesible." not in stdout:
            ip_list.append(iploop) 
         
def cidr16(ip):
    for third_octet in range(0,254):
        for fourth_octet in range(0,254):
            iploop = ip + str(third_octet) + str(fourth_octet)
            map_network = Popen(['ping', '-c 1', iploop])
            stdoutdata, stderrdata = map_network.communicate()
             
def cidr8(ip):
    for second_octet in range(0,254):
        for third_octet in range(0,254):
            for fourth_octet in range(0,254):
                iploop = ip + str(second_octet) + str(third_octet) + str(fourth_octet)
                map_network = Popen(['ping', '-c 1', iploop])
                stdoutdata, stderrdata = map_network.communicate()
                
cidr = {0 : cidr32, 1 : cidr24, 2 : cidr16, 3 : cidr8}

num_octets = netmask.count('0')

if (netmask != "255.255.255.255"):
    ip = ipaddr.split('.')
    del ip[-num_octets:]
    ip = '.'.join(ip) + "."
else:
    ip = ipaddr

cidr[num_octets](ip)

print ip_list
int(input("Digite:"))
