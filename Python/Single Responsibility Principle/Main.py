from Kullanici import Kullanici 
from Adres import Adres 

kullanici = Kullanici()
kullanici.setisim("Yusuf KURT")
kullanici.setmail("yusuf_kurt23@hotmail.com")

adres = Adres()
adres.setulke("Türkiye")
adres.setil("Erzurum")
adres.setilce("Olur")

kullanici.adresguncelle(adres)

print(kullanici)
print()

adres.setpostkodu(25000)
kullanici.adresguncelle(adres)

print(kullanici)
