from İletisim import İletisim
from Kullanici import Kullanici

class Mail(İletisim):
    
    def MailGönder(self,mail, mesaj):
        print(f"{mail} adresine  {mesaj} mesajı gönderildi")
        
    def BilgiGönder(self,kullanici,mesaj):
        self.MailGönder(kullanici.getMail(),mesaj)
