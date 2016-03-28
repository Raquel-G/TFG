import socket, threading, time
from scapy.all import *
from Queue import Queue
from Port import Port


class Portscanner():
    
    __slots__=['__host', '__queue', '__opened_ports', '__filtered_ports', '__print_lock']

    def __init__(self, host):
        self.__host = host
        self.__queue = Queue()
        self.__opened_ports = []
        self.__filtered_ports = []
        self.__print_lock = threading.Lock()
        
    def run(self):
        threads = []
        
        for nport in range(1, 1001):
            self.__queue.put(Port(nport))
            
        for i in range(255):
            t = threading.Thread(target=self.start)
            t.daemon = True
            threads.append(t)
            t.start()
        
        '''for t in threads:
            print str(t)
            t.join()'''

        for t in threading.enumerate():
            print str(t)
            t.join()
            
        self.__queue.join()
        
        return (self.__opened_ports, self.__filtered_ports)

    def tcp_scan(self, port):
        src_port = RandShort()
        
        tcp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_s.settimeout(1)
        
        try:
            tcp_conn = tcp_s.connect_ex((self.__host, int(port)))
            
            if tcp_conn == 0:
                port.setProtocol("tcp")            
                    
                self.__opened_ports.append(port)
            else:
                tcp_ack = sr1( IP(dst=self.__host) / TCP(sport=src_port, dport=int(port), flags="A"), timeout=1, verbose=0)
                
                if tcp_ack == None:
                    port.setProtocol("tcp")
                    
                self.__filtered_ports.append(port)
        except:
            pass
        
        tcp_s.close()

    def udp_scan(self, port):
        udp_conn = sr1( IP(dst=self.__host) / UDP(dport=int(port) / ICMP()), timeout=1, verbose=0)
        
        if udp_conn == None:
            udp_conn = sr1( IP(dst=self.__host) / UDP(dport=int(port)), timeout=1, verbose=0)
            if udp_conn.haslayer(UDP):
                print "Port " + str(port) + " is open."
            elif udp_conn.haslayer(ICMP):
                print "Port " + str(port) + " is filtered."
            
            #port.setProtocol("udp")
            
            ''' 
            retrans = []
            
            for count in range(0, 3):
                retrans.append(sr1(IP(dst=self.__host) / UDP(dport=int(port)), timeout=1, verbose=0))
                
                for item in retrans:
                    if item.haslayer(UDP):
                        print "Port " + str(port) + " is open."
                    elif item.haslayer(ICMP):
                        print "Port " + str(port) + " is filtered."
        
        dest_addr = self.__host
        port = int(port)
        
        icmp = socket.getprotobyname('icmp')
        udp = socket.getprotobyname('udp')

        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)

        recv_socket.settimeout(1)
        send_socket.settimeout(1)

        recv_socket.bind(("", port))
        send_socket.sendto("", (dest_addr, port))
        
        try:
            if recv_socket.recvfrom(512) != None:
                print "UDP Port " + str(port) + " is open."
        except socket.error:
            pass
        finally:
            send_socket.close()
            recv_socket.close()'''
    
    def start(self):
        while not self.__queue.empty():
            port = self.__queue.get()
            self.tcp_scan(port)
            #self.udp_scan(port)
            self.__queue.task_done()




