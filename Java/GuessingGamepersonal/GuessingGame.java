package GuessingGamepersonal;



public class GuessingGame {
    boolean p1isRight;
    boolean p2isRight;
    boolean p3isRight;
    int Target;


    public void gameStart (){
        Player p1 = new Player("CP");
        Player p2 = new Player("Bob");
        Player p3 = new Player("Alice");
        int p1guess = 0; int p2guess = 0; int p3guess = 0;
        System.out.println("Our players are" + p1.name + ", " + p2.name + " and " + p3.name);
        System.out.println("Im thinking of a number between 0 and 9");
        int Target = (int) (Math.random() * 10);
        while (true){
            p1.Guess(); p2.Guess(); p3.Guess();
            p1guess = p1.number; p2guess = p2.number; p3guess = p3.number;
            System.out.println( p1.name + " guessed: " + p1guess);
            System.out.println( p2.name + " guessed: " + p2guess);
            System.out.println( p3.name + " guessed: " + p3guess);
            
            if (p1guess == Target) {
                p1isRight = true;
            }
            if (p2guess == Target) {
                p2isRight = true;
            }
            if (p3guess == Target) {
                p3isRight = true;
            }
            if (p1isRight || p2isRight || p3isRight){
                System.out.println(p1isRight);
                System.out.println(p2isRight);
                System.out.println(p3isRight);
                break;
            }
            else{
                System.out.println("go again");
            
            }
        }

    }
   /* public static void main(String[] args){
        GuessingGame game = new GuessingGame();
        game.GameLauncher();
    }
}
*/
}