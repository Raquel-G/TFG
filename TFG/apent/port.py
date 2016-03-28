#!/usr/bin/env python
#this is the multithreaded port scanner

import socket, threading, thread

def run():
    while True:            
        for port in range(20,80):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            status = sock.connect_ex(("192.168.1.1",port))

            if status == 0:
                #print "from thread %s"%str(threading.current_thread().name)
                print "Port open: " + str(port)
                #PortScanner.openportcount+=1
                sock.close()
            else:
                pass
        
        thread.exit()
            
def main():
    print "[*] Starting Port Scanner....\n"
    hostname = "192.168.1.1" 
 
    n_threads = 255
 
    threads = []
    for i in range(1,n_threads):
        thread = run()
        thread.start()
        threads.append(thread)
    
    for t in threads:
        t.join()

        
        
if __name__ == "__main__":
    main()
