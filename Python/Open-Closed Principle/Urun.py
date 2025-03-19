class Urun:
    
    def __init__(self, isim, fiyat):
        self.id = None  
        self.isim = isim
        self.fiyat = fiyat

    def getfiyat(self):
        return self.fiyat