public class Car{
    int maxspeed;

    public Car(){
        maxspeed = 200;
    }
    public int getmaxspeed(){
        return maxspeed;
    }
    
    public static void main(String[] args){
        Car car = new Car();
        System.out.println(car.getmaxspeed());
    }
}
public class Racecar extends Car {
    public racecar(){
        maxspeed = 370;
    }
}
/*
public class Minivan extends Car {
    public minivan(){
        maxspeed = 150;
    }
}

Car car = new Racecar()
    car.getmaxspeed();

    */