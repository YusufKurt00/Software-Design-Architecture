from Haber import Haber 
from Kullanici import Kullanici
from Mail import Mail

def main():
    
    kullanici = Kullanici("Yusuf","yusuf@gmail.com","192.1.1.1","0")
    haber = Haber()
    haber.Bilgilendir(kullanici,"Deneme mesaj")
    
main()