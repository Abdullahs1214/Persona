package Guessgame;

public class GameLauncher {
        boolean p1wins;
        boolean p2wins;
        boolean p3wins;   
    public GameLauncher(){

    }
    public void launch() {
        p1wins = false;
        p2wins = false;
        p3wins = false;
        GuessGame game = new GuessGame();
        game.startGame();
        p1wins = game.p1isRight;
        p2wins = game.p2isRight;
        p3wins = game.p3isRight;
    }
    public static void main(String[] args){
        GameLauncher launcher = new GameLauncher();
        launcher.launch();
    }
}
