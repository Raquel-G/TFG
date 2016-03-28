from multiprocessing import Pool, Manager
from subprocess import Popen, PIPE
from netaddr import *
import logging
logging.getLogger("scapy.runtime").setLevel("ERROR")
from scapy.all import *
import socket
from Host import Host
from Port import Port
from threading import Thread
from Queue import *
from collections  import defaultdict
from Portscanner import Portscanner

manager = Manager()
reached_ips = manager.list([])

n_threads = 255
threads = []

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

def net_ping(addr):
    p = Pool(n_threads)
    p.map(ping, addr.iter_hosts())
    p.close()
    p.join()	

def ping(ip):    
    map_network = Popen(['ping', '-c 1', str(ip)], stdin=PIPE, stdout=PIPE)
    stdout, stderrdata = map_network.communicate(input=None)

    if "Destination Host Unreachable" not in stdout:
        reached_ips.append(ip)

def getLiveHosts():
    global reached_ips
    reached_ips = sorted(reached_ips)
    return reached_ips

def statePortsDetection(nethostlist):
    for host in nethostlist:        
        ps = Portscanner(str(host))
        (openports, filteredports) = ps.run()
        
        print "IPAddress: " + str(host)
        
        for port in openports:
            print str(port) + "|" + str(port.getProtocol()) + " Port OPEN"
        
        if len(filteredports) < 21:
            for port in filteredports:
                print str(port) + "|" + str(port.getProtocol()) + " Port FILTERED"
        else:
            print "Found " + str(len(filteredports)) + " filtered ports."

        print "\n"


