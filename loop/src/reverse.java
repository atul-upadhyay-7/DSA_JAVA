import java.util.*;
public class reverse {
    public static void main(String[] args) {
//    int n = 298398;
//    while(n > 0){
//        int lastDigit = n % 10;
//        System.out.print(lastDigit+" ");
//        n = n/10;
//    }
//    System.out.println();
//}
//}

////using the reverse variable
//        int n = 3289;
//        int rev = 0;
//        {
//            while (n > 0) {
//                int lastDigit = n % 10;
//                rev = (rev * 10) + lastDigit;
//                n = n / 10;
//            }
//            System.out.println(rev);
//        }
//    }
//}

//break statement
//        for (int i = 1; i <= 5; i++) {
//            if (i == 3) {
//                break;
//            }
//            System.out.println(i);
//        }
//        System.out.println("I am out of the loop");
//    }
//}

Scanner sc = new Scanner(System.in);
do{
    System.out.println("Enter your Number:");
    int n = sc.nextInt();
    if(n%10==0){
        break;
    }
    System.out.println(n);
}while (true);
}
    }