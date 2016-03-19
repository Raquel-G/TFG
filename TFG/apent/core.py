#! /usr/bin/python

import xml.etree.ElementTree
from apent.utils.Network import Network

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="RaquelG"
__date__ ="$13-mar-2016 12:01:55$"

class Core:
    __slots__=['__network']

    def __init__(self):
        self.__network = Network()

    def mapInternalNetwork(self, __network):
        return 0;

    def getNetwork(self):
        return self.__network
    
    def test(self):
        # 1. Map Internal Network
        
        # Extraer este codigo en otro fichero/clase de manera que dandole un input reciba el output con el nombre de la funcion 

        e = xml.etree.ElementTree.parse('xml/proc.xml').getroot()

        function = ""
        rootf = ""
        for atype in e.findall('type'):
            modname = atype.get('tname') 
            if (modname == "nessus"):
                for aroot in atype.findall('root'):
                    rootf = aroot.get('rname') 
                    for aproc in aroot.findall('proc'): 
                        function = rootf + "_" + aproc.get('pname')
                        print function  
                        mod = __import__ (modname)
                        func = getattr(mod,function)
                        func()
                        # Usar una clase para verificar si es suficiente la informacion introducida o es necesario seguir ejecutando metodos
                        print "------------------"

def main():
    tm = Core()    
    print tm.getNetwork().getHost()

if __name__ == "__main__":
    main()               

