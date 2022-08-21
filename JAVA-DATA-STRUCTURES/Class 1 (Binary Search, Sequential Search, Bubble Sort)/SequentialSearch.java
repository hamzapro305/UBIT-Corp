package DSA.Sorting;
import java.util.Scanner;

public class SequentialSearch {

    public static Boolean search(int[] arr,int s
    ) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i]==s) {
                return true;
            }
        }
        return false;
    }
    
    public static void main(String[] args) {
        int[] arr= {0,2,4,6,8,10};
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Number : ");
        int s=sc.nextInt();
        System.out.println(search(arr,s));
    }
}
