public class Mercedes extends Car implements BoostCar {

    @Override
    public void power() {
        this.acceleration = 10;
    }

    @Override
    public void boost() {
        this.acceleration *= 2;
    }
}