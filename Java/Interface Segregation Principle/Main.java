public class Main {
    public static void main(String[] args) {
        DBLogger dbLogger = new DBLogger();
        ConsoleLogger consoleLogger = new ConsoleLogger();

        dbLogger.write("Log 1");
        dbLogger.openConnection();
        dbLogger.write("Log 2");

        consoleLogger.write("Log 3");
        dbLogger.write("Log 4");
        dbLogger.closeConnection();
        dbLogger.write("Log 5");

        for (String message : dbLogger.getData().getList()) {
            System.out.println(message);
        }
    }
}