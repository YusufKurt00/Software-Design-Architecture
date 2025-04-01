import java.util.ArrayList;
import java.util.List;

public class DB {
    private List<String> list;
    private boolean check;

    public DB() {
        this.list = new ArrayList<>();
        this.check = false;
    }

    public List<String> getList() {
        return list;
    }

    public void addLog(String message) {
        if (check) {
            list.add(message);
        }
    }

    public void openDB() {
        System.out.println("DB ile bağlantı kuruldu");
        check = true;
    }

    public void closeDB() {
        System.out.println("DB ile bağlantı kapatıldı");
        check = false;
    }
}