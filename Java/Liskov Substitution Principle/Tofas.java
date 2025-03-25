public class Tofas extends Car implements AirCondition {

    @Override
    public void power() {
        this.acceleration = 5;
    }

    @Override
    public void open() {
        this.acceleration *= 0.9;
    }
}