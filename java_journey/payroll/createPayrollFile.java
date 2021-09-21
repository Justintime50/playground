import java.io.*;
import javax.swing.JOptionPane;

public class createPayrollFile {
    public static void main(String[] args) {
        try {
            FileWriter payrollFileWriter = new FileWriter("payrollFile.txt");
            String name;
            String pay;
            String hours;
            String answer;

            JOptionPane.showMessageDialog(null, "Welcome to your Company Payroll!");
            do {
                name = JOptionPane.showInputDialog(null, "Please enter the employee's name!");
                String formattedName = String.format("\"%s\"", name);
                payrollFileWriter.write(formattedName);

                pay = JOptionPane.showInputDialog(null, "Please enter " + name + "'s hourly pay!");
                Double payDouble = Double.parseDouble(pay);
                payrollFileWriter.write(String.valueOf(" " + payDouble + " "));

                hours = JOptionPane.showInputDialog(null,
                        "Please enter " + name + "'s hours they worked the previous week!");
                Double hoursDouble = Double.parseDouble(hours);
                payrollFileWriter.write(String.valueOf(hoursDouble + "\n"));

                answer = JOptionPane.showInputDialog(null, "Do you wish to add another employee? yes/no");
            } while (answer.equals("yes"));
            payrollFileWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
