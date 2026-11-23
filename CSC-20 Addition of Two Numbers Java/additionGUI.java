// Imported libraries for the GUI and button/text layout.
import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

public class additionGUI {
    public additionGUI() {
        // Create the text fields and controls the user interacts with.
        JTextField firstNumberField = new JTextField();
        JTextField secondNumberField = new JTextField();
        JComboBox<String> operationBox = new JComboBox<>(
                new String[] { "Add", "Subtract", "Multiply", "Divide" });
        JLabel resultLabel = new JLabel("Result:");
        JButton calculateButton = new JButton("Calculate");

        // Create the window and make it close the program when the X is clicked.
        JFrame frame = new JFrame("Addition Calculator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Arrange the labels and controls in five rows and two columns.
        frame.setLayout(new GridLayout(5, 2, 8, 8));

        // Add the input fields and operation selector to the window.
        frame.add(new JLabel("First number"));
        frame.add(firstNumberField);
        frame.add(new JLabel("Second number"));
        frame.add(secondNumberField);
        frame.add(new JLabel("Operation"));
        frame.add(operationBox);

        // Add the calculate button and the area that displays the answer.
        frame.add(new JLabel());
        frame.add(calculateButton);
        frame.add(new JLabel("Answer"));
        frame.add(resultLabel);

        // Run this code when the Calculate button is clicked.
        calculateButton.addActionListener(event -> {
            try {
                // Convert the text entered in both fields into integers.
                int firstNumber = Integer.parseInt(firstNumberField.getText().trim());
                int secondNumber = Integer.parseInt(secondNumberField.getText().trim());
                String operation = (String) operationBox.getSelectedItem();

                // Choose the matching calculation based on the selected operation.
                int result;
                if (operation.equals("Add")) {
                    result = addition.add(firstNumber, secondNumber);
                } else if (operation.equals("Subtract")) {
                    result = addition.substract(firstNumber, secondNumber);
                } else if (operation.equals("Multiply")) {
                    result = addition.multiply(firstNumber, secondNumber);
                } else {
                    // Division is not allowed when the second number is zero.
                    if (secondNumber == 0) {
                        resultLabel.setText("Cannot divide by zero");
                        return;
                    }
                    result = addition.divide(firstNumber, secondNumber);
                }

                // Display the calculated answer in the result label.
                resultLabel.setText(String.valueOf(result));
            } catch (NumberFormatException exception) {
                // This runs when the entered text is not a valid integer.
                resultLabel.setText("Enter valid integers");
            }
        });

        // Size the window to fit its controls and center it on the screen.
        frame.pack();
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(additionGUI::new);
    }
}