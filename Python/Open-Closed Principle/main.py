from StandartKullanici import StandartKullanici
from PremiumKullanici import PremiumKullanici
from Urun import Urun
from Siparis import Siparis


ali = StandartKullanici()
veli = PremiumKullanici()

telefon = Urun("telefon", 3000)
bilgisayar = Urun("bilgisayar", 5000)

ali.addurun(telefon)
ali.addurun(bilgisayar)

veli.addurun(telefon)
veli.addurun(bilgisayar)

Siparis.odemeyap(ali)
Siparis.odemeyap(veli)