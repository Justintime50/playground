import java.io.*;
import java.util.*;
import javax.swing.JOptionPane;


public class nationalParks {
    public static void main(String[] args) {
        // Ask the user for input and build an array of parks
        ArrayList<String> parks = promptUser();

        // Iterate over each location in the array of user data and send that string to the `fixString` function
        ArrayList<String> fixedParkList = new ArrayList<String>();
        for (String park : parks) {
            fixedParkList.add(fixString(park));
        }

        // Build the final string
        String finalString = buildString(fixedParkList);

        // Print the final result
        System.out.println(finalString);
    }

    // Prompts the user for a list of national parks and builds an array
    public static ArrayList<String> promptUser() {
        String answer;
        ArrayList<String> parks = new ArrayList<String>();
        do {
            answer = JOptionPane.showInputDialog(null, "Enter a name of a national park. Type \"done\" when finished.");
            if (!answer.equals("done") && !answer.isEmpty() && answer != null) {
                parks.add(answer);
            }
        } while(!answer.equals("done"));
        return parks;
    }

    // Attribution: https://www.programiz.com/java-programming/examples/capitalize-first-character-of-string
    public static String fixString(String park) {
        // stores each characters to a char array
        char[] charArray = park.toCharArray();
        boolean foundSpace = true;

        // For every character in the park name string, capitalize the first letter, lowercase the rest
        for(int i = 0; i < charArray.length; i++) {
            // if the array element is a letter
            if(Character.isLetter(charArray[i])) {
                // check space is present before the letter
                if(foundSpace) {
                    // change the letter into uppercase
                    charArray[i] = Character.toUpperCase(charArray[i]);
                    foundSpace = false;
                } else {
                    charArray[i] = Character.toLowerCase(charArray[i]);
                }
            } else {
                // if the new character is not character
                foundSpace = true;
            }
            // convert the char array to the string
            park = String.valueOf(charArray);
        }
        return park;
    }

    // Build the final string
    public static String buildString(ArrayList<String> parks) {
        String finalString = "Favorite National Parks: ";
        for(int i = 0; i < parks.size(); i++) {
            if (parks.size() - 1 == i) {
                finalString = finalString + parks.get(i);
            } else {
                finalString = finalString + parks.get(i) + " | ";
            }
        }
        return finalString;
    }
}
