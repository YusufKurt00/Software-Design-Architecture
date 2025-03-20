public class Adres {
    private String Ulke;
    private String il;
    private String ilce;
    private int postaKodu;

    public Adres(String Ulke, String il, String ilce,int postaKodu){
        this.Ulke=Ulke;
        this.il=il;
        this.ilce=ilce;
        this.postaKodu=postaKodu;

    }
    @Override
    //string ifadeyi ekrana yazdırma amacıyla
    public String toString(){
        return (Ulke+" "+il+" "+ilce+" "+postaKodu);
    }
    //set fonk eklenecek
    public String getulke(){
        return Ulke;
    }

    public String getil(){
        return il;
    }

    public String getilce(){
        return ilce;
    }

    public int getpostaKodu(){
        return postaKodu;
    }
}   
