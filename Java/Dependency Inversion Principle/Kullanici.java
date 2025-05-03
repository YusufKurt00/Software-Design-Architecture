public class Kullanici {
    private String isim;
    private String mail;
    private String ip;
    private String tel;

    public Kullanici(String isim, String mail, String ip, String tel) {
        this.isim = isim;
        this.mail = mail;
        this.ip = ip;
        this.tel = tel;
    }

    public String getIsim() {return isim;}

    public void setIsim(String isim) {
        this.isim = isim;
    }

    public String getMail() {return mail;}

    public void setMail(String mail) {
        this.mail = mail;
    }

    public String getIp() {return ip;}

    public void setIp(String ip) {
        this.ip = ip;
    }

    public String getTel() {return tel;}

    public void setTel(String tel) {
        this.tel = tel;
    }
}