from Mail import Mail
from Bildirim import Bildirim

class Haber:
    
    def __init__(self):
        self.iletisimListesi=[]
        self.mail=Mail()
        self.bildirim=Bildirim()
        self.iletisimListesi.append(self.mail)
        self.iletisimListesi.append(self.bildirim)
        
    def Bilgilendir(self,kullanici,mesaj):
        
        for iletisim in self.iletisimListesi:
            iletisim.BilgiGönder(kullanici,mesaj)
    
    
    