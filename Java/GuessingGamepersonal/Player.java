package GuessingGamepersonal;

public class Player {
    int number;
    String name;
    
    public Player (String name) {
        this.name = name;
    }
    public void Guess() {
        int guess = (int) (Math.random() * 10);
        this.number = guess;
    }
    //public static void main(String[] args){
        //Player p1 = new Player("Jeff");
        //p1.Guess();
       // System.out.println(p1.name);
        //System.out.println(p1.number);
    //}
}
