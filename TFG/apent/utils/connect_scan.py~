import logging
logging.getLogger("scapy.runtime").setLevel("ERROR")
from scapy.all import *

if len(sys.argv) != 3:
    print "usage: Python connect_scan.py <ip_address> <list of ports separated by colon>"
    exit()

src_port = RandShort()
dst_ip = sys.argv[1]
ports = sys.argv[2]

ports.replace(" ", "")
scanPorts = ports.strip().split(":")
for port in scanPorts:
    response = sr1( IP(dst=dst_ip) / TCP(sport=src_port, dport=int(port), flags="S"))
    
    response = sr1( IP(dst="192.168.1.37") IP(dst="216.58.210.131") / TCP(sport=RandShort(), dport=int(40), flags="S"))
    
    if(str(type(response)) == "<type 'NoneType'>"):
        print port + ": Port Closed"
    elif (response.getlayer(TCP).flags == 0x12):
        send_rst = sr1(IP(dst=dst_ip) / TCP(sport=src_port, dport=int(port), flags="AR"))
        print port + ": Port Open"
    elif (response.getlayer(TCP).flags == 0x14):
        print port + ": Port Closed"
