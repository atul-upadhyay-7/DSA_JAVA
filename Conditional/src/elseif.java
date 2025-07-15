import java.util.*;
public class elseif{
    public static void main(String[] args){
//        int age =22;
//        if(age >= 18){
//            System.out.println("eligible to drive");
//        }
//        else if(age >13 && age<18){
//            System.out.println("teenager");
//        }
//        else{
//            System.out.println("Not eligible  to vote");

//        Income tax calculator
        Scanner sc= new Scanner(System.in);
        int income = sc.nextInt();
        int tax;

        if(income <500000){
            tax=0;
        }
        else if(income >=500000 && income<100000){
            tax =(int)(income*0.2);
        }
        else {
            tax=(int)(income*0.3);
        }
        System.out.println("Your tax is"+tax);
    }
}