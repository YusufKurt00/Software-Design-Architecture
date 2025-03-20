public class Main {
    public static void main(String[] args) {

        Adres adres1=new Adres("Türkiye","Erzurum","Olur",25000);
        Kullanici kullanıcı1=new Kullanici("Yusuf","yusuf_kurt23@hotmail.com",adres1);
        System.out.println("Kullanıcı Bilgileri: "+ kullanıcı1.getIsim()+"\n"+"Mail: "+kullanıcı1.getmail());
        System.out.println("Adres Bilgileri:"+ adres1.getulke()+" "+ adres1.getil()+" "+ adres1.getilce()+" "+ adres1.getpostaKodu());

    }
}
