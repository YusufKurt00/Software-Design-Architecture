public class Main {
    public static void main(String[] args) {

        Kullanici kullanici = new Kullanici("Yusuf", "yusuf@gmail.com", "192.1.1.1", "0");
        Haber haber = new Haber();
        
        haber.bilgilendir(kullanici, "Deneme mesaj");
    }
}