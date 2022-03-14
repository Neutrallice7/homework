import java.util.Scanner;

public class Number10 {
    public static void main(String[] args) {
        Scanner input1 = new Scanner(System.in);
        Scanner input2 = new Scanner(System.in);
        Scanner input3 = new Scanner(System.in);

        System.out.println("Enter numbers: ");
        Double num1 = input1.nextDouble();
        Double num2 = input2.nextDouble();
        Double num3 = input3.nextDouble();

        Double mean = (num1+num2+num3) / 3;
        Double variance = ((Math.pow((num1 - mean),2) + Math.pow((num2 - mean),2) + Math.pow((num3 - mean),2)) / 3);
        Double deviation = Math.sqrt(variance);

        System.out.println("The mean is  "+ mean + " The variance is " + variance + " And the deviation is " + deviation);
        
    }
}
