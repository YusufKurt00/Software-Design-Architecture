import java.util.ArrayList;
import java.util.List;

public class Haber {
    private List<İletisim> iletisimListesi;
    private Mail mail;
    private Bildirim bildirim;

    public Haber() {
        iletisimListesi = new ArrayList<>();
        mail = new Mail();
        bildirim = new Bildirim();
        iletisimListesi.add(mail);
        iletisimListesi.add(bildirim);
    }

    public void bilgilendir(Kullanici kullanici, String mesaj) {
        for (İletisim iletisim : iletisimListesi) {
            iletisim.bilgiGonder(kullanici, mesaj);
        }
    }
}