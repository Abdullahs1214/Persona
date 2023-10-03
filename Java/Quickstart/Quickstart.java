package Quickstart;
public class Quickstart{
    public static boolean isEven(int i) { 
    return (i % 2) == 1;
}
public static void main(String[] args) {
// The following prints all even numbers between 1 and 10 
for(int i = 1; i < 100 && isEven(i); i++)

    System.out.println(i);
}

    
}
