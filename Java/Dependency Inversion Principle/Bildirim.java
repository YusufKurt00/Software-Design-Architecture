public class Bildirim implements  İletisim {

    public void bildirimGonder(String ip, String mesaj) {

        System.out.println(ip + " adresine " + mesaj + " mesajı gönderildi");
    }

    @Override
    public void bilgiGonder(Kullanici kullanici, String mesaj) {
        
        bildirimGonder(kullanici.getIp(), mesaj);
    }
}