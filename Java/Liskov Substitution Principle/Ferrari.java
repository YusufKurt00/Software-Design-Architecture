public class Ferrari extends Car implements BoostCar, AirCondition {

    @Override
    public void power() {
        this.acceleration = 10;
    }

    @Override
    public void boost() {
        this.acceleration *= 2;
    }

    @Override
    public void open() {
        this.acceleration *= 0.9;
    }
}