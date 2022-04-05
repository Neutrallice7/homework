import java.util.Scanner;

public class Number2 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in); 
        System.out.print("Enter amount of items: ");

        int NUM_ITEMS = input.nextInt(); 
        int [] items = new int[NUM_ITEMS];

        System.out.println("Enter values (Space to seperate) ");
        for(int i = 0; i < items.length; i++){ 
            items[i] = input.nextInt(); 
        }
        for(int i = 0; i < items.length; i++){ 
            System.out.print(i + ": ");
            for(int j = 0; j < items[i]; j++){
                System.out.print('*');
            }
            System.out.println("("+ items[i] + ")");
        }}
}
