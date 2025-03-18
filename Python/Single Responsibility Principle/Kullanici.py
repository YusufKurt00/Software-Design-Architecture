class Kullanici():
    def __init__(self):
        self.isim = None
        self.mail = None
        self.adres = None

    def setisim(self, isim):
        self.isim = isim

    def getisim(self):
        return self.isim

    def setmail(self, mail):
        self.mail = mail

    def getmail(self):
        return self.mail

    def adresguncelle(self, adres):
        self.adres = adres

    def getadres(self):
        return str(self.adres)

    def __str__(self):
        return f"{self.getisim()} {self.getmail()} {self.getadres()}"

    def giris_yap(self, mail, sifre):
        print("Giriş yapıldı.")