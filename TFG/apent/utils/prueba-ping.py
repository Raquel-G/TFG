from multiprocessing import Pool, Manager
from subprocess import Popen, PIPE
from netaddr import *
import socket

def findNetAddr():
    import subprocess
 
    proc = subprocess.Popen(["ip r s | awk '{{if(NR==1)print $3}}'"], stdout=subprocess.PIPE, shell=True)
    gw_ip = IPAddress(proc.communicate()[0][:-1])
    
    ipFound = False
    index = 2
    while (not ipFound):
        proc = subprocess.Popen(["ip r s | awk '{{if(NR=='" + str(index) + "')print $1}}'"], stdout=subprocess.PIPE, shell=True)
        net_addr = IPNetwork(proc.communicate()[0][:-1])
        
        if (gw_ip in net_addr):
            ipFound = True
        
        index = index + 1

    return net_addr


#ip = getNetAddr()
#ip -->  IPNetwork('10.10.0.0/16')
#ip.ip --> IPAddress('10.10.0.0')
#ip.broadcast --> IPAddress('10.10.255.255')
#ip.hostmask --> IPAddress('0.0.255.255')
#ip.netmask --> IPAddress('255.255.0.0')
#ip.prefixlen --> 16
#ip.size --> 65536
#ip.cidr --> IPNetwork('10.10.0.0/16')

manager = Manager()

reached_ips = manager.list([])
threads = []

ntwkaddr = findNetAddr()
cidr = "/" + str(ntwkaddr.prefixlen)

n_threads = 255

def net_ping():
    p = Pool(n_threads)
    p.map(ping, ntwkaddr.iter_hosts())
    p.close()
    p.join()	

def ping(ip):    
    map_network = Popen(['ping', '-c 1', str(ip)], stdin=PIPE, stdout=PIPE)
    stdout, stderrdata = map_network.communicate(input=None)

    if "Destination Host Unreachable" not in stdout:
        reached_ips.append(ip)

net_ping()

print "IPLIST: " + str(len(reached_ips))
for a in reached_ips:
   print a





