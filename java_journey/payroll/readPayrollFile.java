import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class readPayrollFile {
    public static void main(String[] args) {
        // Open a file, iterate the file, and calculate pay
        Scanner payrollFile = scanFile();
        String[] iteratedFile = iterateFile(payrollFile);
        payrollFile.close();
        int finalPay = calculatePay(iteratedFile);
        System.out.println(String.format("The final pay for " + iteratedFile[0] + " was $" + finalPay));
    }

    public static Scanner scanFile() {
        // Open and scan a file to memory
        Scanner payrollFileScanner = null;
        try {
            File payrollFile = new File("payrollFile.txt");
            payrollFileScanner = new Scanner(payrollFile);
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
            e.printStackTrace();
        }
        return payrollFileScanner;
    }

    public static String[] iterateFile(Scanner grossFileScanner) {
        // Iterate the file contents and create arrays for each line
        // Arrays contain [0] = name, [1] = pay, [2] = hours

        // This has only been tested with a single employee record but
        // be possible with multiple with some tweaks
        String[] array = new String[3];
        while (grossFileScanner.hasNextLine()) {
            int i = 0;
            Scanner grossFileScanner2 = new Scanner(grossFileScanner.nextLine());
            while (grossFileScanner2.hasNext()) {
                String singleRecord = grossFileScanner2.next();
                array[i] = singleRecord;
                i++;
            }
        }
        return array;
    }

    public static int calculatePay(String[] iteratedFile) {
        // Calculate the pay by multiplying the indexes together
        // Alter for your needs to calculate other items
        double payDouble = Double.parseDouble(iteratedFile[1]);
        double hoursDouble = Double.parseDouble(iteratedFile[2]);
        int pay = (int) payDouble;
        int hours = (int) hoursDouble;
        int finalPay = pay * hours;
        return finalPay;
    }
}
