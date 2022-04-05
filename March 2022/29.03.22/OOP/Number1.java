import java.util.Scanner;

public class Number1 {
    public static void main(String[] args){
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Enter amount of items");

            int NUM_ITEMS = scanner.nextInt(); 
            int items[] = new int[NUM_ITEMS]; 
            
            System.out.println("Enter values (Space to seperate): ");
            for (int i = 0; i < items.length; i++) { 
                items[i] = scanner.nextInt(); 
            }

            System.out.println("The Values are: [");
            for (int i= 0; i < NUM_ITEMS ; i++) {
                if (i == NUM_ITEMS - 1){
                    System.out.print(items[i] + "]");
                }
                else {
                    System.out.print(items[i]+ ", ");
                }
             }
        }
    }
}