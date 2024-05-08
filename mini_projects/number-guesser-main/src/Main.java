import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        System.out.println("Number Guessing Game");
        Scanner myObj = new Scanner(System.in);
        System.out.println("Enter the Highest Number Possible: ");
        int maxnumber = Integer.parseInt(myObj.nextLine());
        System.out.println("You Have entered: " + maxnumber);
        System.out.println("Cool! Now enter your guess: ");
        int guessnum = Integer.parseInt(myObj.nextLine());
        System.out.println("You Have guessed: " + guessnum);

        gamestart game1 = new gamestart(maxnumber, guessnum);
        game1.gameisgoing();



    }
}
