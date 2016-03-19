
class Network:
    __slots__=['__hostsList']
    
    def __init__(self):
        self.__hostsList = "hola desde el constructor de Network"
    
    def getHost(self):
        return self.__hostsList
