from abc import ABC, abstractmethod

class Kullanici(ABC):
    
    def __init__(self):
        self.id = None
        self.ad = None
        self.mail = None
        self.urunler = []

    @abstractmethod
    def gettoplamtutar(self, fiyat):
        pass

    def getad(self):
        return self.ad

    def geturunler(self):
        return self.urunler

    def addurun(self, urun):
        self.geturunler().append(urun)
