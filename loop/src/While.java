import java.util.*;
public class While {
    public static void main(String args[]) {
//        int counter=0;
////        While loop
//        while(counter <10){
//            System.out.println("Hello");
////            print number from 0 to 9
//            System.out.print(counter+ " ");
//            counter ++;
//
//        }
//        System.out.println("printer hello 10 times");
//    }
//}


//        //            print number from 1 to n
//        Scanner sc = new Scanner(System.in);
//        int range = sc.nextInt();
//            int counter = 1;
//        while (counter <= range) {
//            System.out.println(counter + "");
//            counter++;
//        }
//        System.out.println();
//
//    }
//}

//    Sum of first N natural numbers
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0;
        int i = 1;
        while (i <= n) {
            sum += i;
            i++;
        }
        System.out.println("sum is :" + sum);

    }
    }
