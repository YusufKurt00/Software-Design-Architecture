from İletisim import İletisim
from Kullanici import Kullanici

class Bildirim(İletisim):
    
    def BildirimGönder(self,ip,mesaj):
        print(f"{ip} adresine {mesaj} mesajı gönderildi")
        
    def Bilgilendir(self,kullanici,mesaj):
        self.BildirimGönder(kullanici.getİp(),mesaj)
        
    
