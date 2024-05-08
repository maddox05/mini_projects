import java.util.Scanner;
import java.util.Random;
public class gamestart
{
    private int maxnumber;
    private int enterednumber;
    Random rand = new Random();
    private int randomnumber;
    Scanner myObj = new Scanner(System.in);

    public gamestart(int max, int usernum)
    {
        maxnumber = max;
        enterednumber = usernum;
        int randomnumber = rand.nextInt(maxnumber+1);
    }
    public void gameisgoing(){
        if (enterednumber <= maxnumber){

            if(randomnumber == enterednumber){
                System.out.println("you guessed correctly! The Random Number was: " + randomnumber);
            }
            else{
                if(enterednumber < randomnumber){
                    System.out.println("the Random Number is greater than what you guessed, please guess again");
                    System.out.println("Enter your New guess: ");
                    enterednumber = Integer.parseInt(myObj.nextLine());
                    gameisgoing();
                }
                else{
                    System.out.println("the Random Number is less than what you guessed, please guess again");
                    System.out.println("Enter your New guess: ");
                    enterednumber = Integer.parseInt(myObj.nextLine());
                    gameisgoing();
                }
            }

        }
        else{
            System.out.println("you must guess equal to or lower than you max number");
        }
    }

}
