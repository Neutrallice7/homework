public class Account {
    private int balance;

    public Account(){
        this.balance = 0;
    }

    public Account (int init_balance){
        this.balance = init_balance;
    }

    public int getBalance(){
        return this.balance;
    }
    public boolean deposit(int amt){
        boolean check = true;
        if(amt >= 0){
            this.balance +=  amt;
        }else{
            check = false;
        }
        return check;
    }

    public boolean withdraw(int amt){
        boolean check = true;
        if(amt >= 0 && this.balance >= amt){
            this.balance -= amt;
        }else{
            check = false;
        }
        return check;
    }
}