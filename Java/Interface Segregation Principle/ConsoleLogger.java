public class ConsoleLogger extends Logger {
    @Override
    public void write(String message) {
        System.out.println(message);
    }
}