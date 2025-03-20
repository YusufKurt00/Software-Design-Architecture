public class Kullanici{
    private  String isim;
    private  String mail;
    private  Adres adres;

    public Kullanici(String isim, String mail, Adres adres){
        this.isim=isim;
        this.mail=mail;
        this.adres=adres;
    }


    public void girisYap(String isim, String mail){
        System.out.println("Kullanıcı Giriş Yaptı!");
    }
    @Override
    public String toString(){
        return (isim+" "+mail+" "+adres);
    }
   
    public String getIsim(){
        return isim;
    }

    public String getmail(){
        return mail;
    }

    public Adres getadres(){
        return adres;
    }
}