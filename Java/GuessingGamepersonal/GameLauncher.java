package GuessingGamepersonal;

import Guessgame.GuessGame;

public class GameLauncher {
    boolean p1wins;
    boolean p2wins;
    boolean p3wins;
 

    
    public void launcher(){
        GuessingGame game = new GuessingGame();
        game.gameStart();
        p1wins  = game.p1isRight;
        p2wins = game.p2isRight;
        p3wins = game.p3isRight;
    }
    public static void main(String[] args){
        GameLauncher gamelaunch = new GameLauncher();
        gamelaunch.launcher();
    }
}
