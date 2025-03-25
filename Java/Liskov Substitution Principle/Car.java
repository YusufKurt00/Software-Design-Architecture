public abstract class Car {
    
    protected int acceleration; 
    protected int velocity; 

    public Car() {
        this.acceleration = 0;
        this.velocity = 0;
    }

    public abstract void power();

    public void run() {
        this.velocity += this.acceleration;
    }

    public int getVelocity() {
        return this.velocity;
    }

    public int getAcceleration() {
        return this.acceleration;
    }
}
