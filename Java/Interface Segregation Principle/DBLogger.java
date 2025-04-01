public class DBLogger extends Logger implements Connection {
    private DB data;

    public DBLogger() {
        this.data = new DB();
    }

    @Override
    public void write(String message) {
        data.addLog(message);
    }

    @Override
    public void openConnection() {
        data.openDB();
    }

    @Override
    public void closeConnection() {
        data.closeDB();
    }

    public DB getData() {
        return data;
    }
}