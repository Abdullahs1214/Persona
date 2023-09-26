package Car;
public class Car{
    int maxspeed;

    public Car(){
        maxspeed = 200;
    }
    public int getmaxspeed(){
        return maxspeed;
    }
    
    public static void main(String[] args){
        Car car = new Minivan();
        System.out.println(car.getmaxspeed());
    }
}
