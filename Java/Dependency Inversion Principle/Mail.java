public class Mail implements  İletisim {

    public void mailGonder(String mail, String mesaj) {

        System.out.println(mail + " adresine " + mesaj + " mesajı gönderildi");
    }

    @Override
    public void bilgiGonder(Kullanici kullanici, String mesaj) {
        
        mailGonder(kullanici.getMail(), mesaj);
    }
}