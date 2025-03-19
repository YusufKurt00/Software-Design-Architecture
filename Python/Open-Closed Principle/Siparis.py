class Siparis:
    def odemeyap(kullanici):
        toplamtutar = 0

        for urun in kullanici.geturunler():
            toplamtutar += urun.getfiyat()

        toplamtutar = kullanici.gettoplamtutar(toplamtutar)

        print(f"{type(kullanici).__name__} toplam tutar = {toplamtutar}")
