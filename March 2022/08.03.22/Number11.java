public class Number11 {
    public static void main(String[] args){
        int x,y,z;
        x = 10;
        y = 5;

        System.out.println("The initial values of x = "+ x + " and y = "+ y);

        z = x;
        x = y;
        y = z;

        System.out.println("The values after the exchange are x = "+ x +" and y = "+ y);
    }
}
