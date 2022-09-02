import java.util.Scanner;

// Sums individual ints from a longer integer based on user input

public class sumInteger {
    public static void main(String[] args) {
        final int baseTen = 10;
        int mySum = 0;

        System.out.println("Input an integer to sum:");
        Scanner myScanner = new Scanner(System.in);
        int userInput = Integer.parseInt(myScanner.nextLine());
        myScanner.close();

        while (userInput > 0) {
            int individualInt = userInput % baseTen; // Pull out the base 10 number one at a time
            mySum += individualInt;
            userInput = userInput / baseTen; // Remove the number from the long user input int
        }

        System.out.println(mySum);
    }
}
