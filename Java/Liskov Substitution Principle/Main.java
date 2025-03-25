public class Main {
    public static void main(String[] args) {

        Ferrari ferrari = new Ferrari();
        Mercedes mercedes = new Mercedes();
        Tofas tofas = new Tofas();


        ferrari.power();
        mercedes.power();
        tofas.power();

        System.out.println("\n****** Ferrari ******");
        System.out.println("İlk Hız: " + ferrari.getVelocity());
        ferrari.run();
        System.out.println("Hızlandıktan sonra: " + ferrari.getVelocity());
        ferrari.boost();
        ferrari.run();
        System.out.println("Turbodan sonra: " + ferrari.getVelocity());
        ferrari.open();
        ferrari.run();
        System.out.println("Klimadan sonra: " + ferrari.getVelocity());

        System.out.println("\n****** Mercedes ******");
        System.out.println("İlk Hız: " + mercedes.getVelocity());
        mercedes.run();
        System.out.println("Hızlandıktan sonra: " + mercedes.getVelocity());
        mercedes.boost();
        mercedes.run();
        System.out.println("Turbodan sonra: " + mercedes.getVelocity());

        System.out.println("\n****** Tofas ******");
        System.out.println("İlk Hız: " + tofas.getVelocity());
        tofas.run();
        System.out.println("Hızlandıktan sonra: " + tofas.getVelocity());
        tofas.open();
        tofas.run();
        System.out.println("Klimadan sonra: " + tofas.getVelocity());

    }
}