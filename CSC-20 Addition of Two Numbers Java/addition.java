import java.util.Scanner;

public class addition {
    public static void main(String[] args) {

        // Scanner reads text and numbers entered by the user in the console.
        Scanner scanner = new Scanner(System.in);

        // Ask for the first number and store it in num1.
        System.out.println("Please input the first digit: ");
        int num1 = scanner.nextInt();

        // Ask for the second number and store it in num2.
        System.out.println("Please input the second digit: ");
        int num2 = scanner.nextInt();

        // Ask the user to choose an operation using an lowercase word.
        System.out.println("Please input the operation you want to perform (add, subtract, multiply, divide): ");
        String chosenOperation = scanner.next();

        // Check which operation the user entered and call the matching method.
        if (chosenOperation.equals("add")) {
            int sum = add(num1, num2);
            System.out.println("The sum is: " + sum);
        } else if (chosenOperation.equals("subtract")) {
            int difference = substract(num1, num2);
            System.out.println("The difference is: " + difference);
        } else if (chosenOperation.equals("multiply")) {
            int product = multiply(num1, num2);
            System.out.println("The product is: " + product);
        } else if (chosenOperation.equals("divide")) {
            int quotient = divide(num1, num2);
            System.out.println("The quotient is: " + quotient);
        }

        // Close the Scanner after all input has been read.
        scanner.close();
    }

    // Add two integers and return their sum.
    public static int add(int num1, int num2) {

        int sum = num1 + num2;

        return sum;
    }

    // Subtract num2 from num1 and return the difference.
    public static int substract(int num1, int num2) {

        int sum = num1 - num2;

        return sum;
    }

    // Multiply two integers and return their product.
    public static int multiply(int num1, int num2) {

        int sum = num1 * num2;

        return sum;
    }

    // Divide num1 by num2 and return the integer quotient.
    public static int divide(int num1, int num2) {

        int sum = num1 / num2;

        return sum;
    }
}