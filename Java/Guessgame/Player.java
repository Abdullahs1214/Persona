package Guessgame;

public class Player {
    int number;
    String name;

    public Player(String name) {
        this.name = name;
    }
    public void Guess() {
        int guess = (int) (Math.random() *10);
        this.number = guess;
    }
    }