import java.util.Scanner; //Imports scanner for inputs


public class Number9 {
    public static void main(String[] args){
        try (Scanner input = new Scanner(System.in)) {
            System.out.println("Enter number: ");

            double Celsius = input.nextDouble(); 
            System.out.println("You have entered " + Celsius);

            double Fahrenheit;

            Fahrenheit = ((9 * Celsius)/5) + 32;

            System.out.println("The converted amount is " + Fahrenheit);

            input.close();
        }
    }
}
