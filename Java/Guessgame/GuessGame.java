package Guessgame;

public class GuessGame {
    Player p1;
    Player p2;
    Player p3;

    boolean p1isRight;
    boolean p2isRight;
    boolean p3isRight;
    
    public void startGame(){
        p1 = new Player("CP"); p2 = new Player("Bob"); p3 = new Player("Alice");
        int guessP1 = 0; int guessP2 = 0; int guessP3 = 0;
        p1isRight = false; p2isRight = false; p3isRight = false;
        System.out.println("Our players are " + p1.name + ", " + p2.name + " and " + p3.name);
        int Target = (int)(Math.random() * 10);
        System.out.println("I am thinking of a number between 0 and 9");
        
        while(true){
            p1.Guess();
            guessP1 = p1.number;
            System.out.println(p1.name + " guessed: " + p1.number);
            p2.Guess();
            guessP2 = p2.number;
            System.out.println(p2.name + " guessed: " + p2.number);
            p3.Guess();
            guessP3 = p3.number;
            System.out.println(p3.name + " guessed: " + p3.number);
            if (guessP1 == Target){
                p1isRight = true;
            }
            if (guessP2 == Target){
                p2isRight = true;
            }
            if (guessP3 == Target){
                p3isRight = true;
            }
            if (p1isRight || p2isRight || p3isRight){
                System.out.println("We have a winner");
                System.out.println(p1.name + ": " + p1isRight + ", " + p2.name + ": " + p2isRight + ", " + p3.name + ": " + p3isRight);
                System.out.println("Game Over");
                break;
            }else{
                System.out.println("lets play again");
            }
            
        }
        
    
    }
}

