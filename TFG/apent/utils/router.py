import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

response = sr1( IP(dst="192.168.1.37") / IP(dst="216.58.210.131") / TCP(sport=RandShort(), dport=int(40), flags="S"), timeout=1)

'''   
if(str(type(response)) == "<type 'NoneType'>"):
    print port + ": Port Closed"
elif (response.getlayer(TCP).flags == 0x12):
    send_rst = sr1(IP(dst=dst_ip) / TCP(sport=src_port, dport=int(port), flags="AR"))
    print port + ": Port Open"
elif (response.getlayer(TCP).flags == 0x14):
    print port + ": Port Closed" '''
