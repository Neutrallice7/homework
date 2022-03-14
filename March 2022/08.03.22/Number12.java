public class Number12 {
    public static void main(String[] args){
        System.out.println("number\tsquare\tcube");

        for(int i = 0; i < 11; i++){
            System.out.println("\t" + i + "\t" + Math.round(Math.pow(i,2)) + "\t\t" + Math.round(Math.pow(i,3)));
        }
    }
}
