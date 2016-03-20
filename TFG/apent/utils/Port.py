
class Port:
    
    __slots__=['__nport', '__state', '__tProtocol', '__service']
    
    def __init__(self, nport):
        self.__nport = nport
        
        self.__tProtocol['tcp'] = False
        self.__tProtocol['udp'] = False

    def getService(self):
        return self.__service

    def setService(self, name):
        self.__service = Service(name)

    def getServiceVersion(self):
        return self.__service.getVersion()

    def setServiceVersion(self, version)
        self.__service.setVersion(version)

    def isTCP(self):
        return self.__tProtocol['tcp']

    def isUDP(self):
        return self.__tProtocol['udp']

