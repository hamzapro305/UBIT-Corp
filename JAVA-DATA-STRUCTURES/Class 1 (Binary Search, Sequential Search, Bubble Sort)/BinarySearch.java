package DSA.Sorting;

import java.util.Scanner;

public class BinarySearch {

    public static Boolean search(int[] arr, int a) {
        int sp = 0;
        int ep = arr.length;
        int mid = (sp + ep) / 2;

        for (int i = 0; i < arr.length; i++) {
            if (a < arr[mid]) {
                ep = mid;
                mid = (sp + ep) / 2;
            } else if (a > arr[mid]) {
                sp = mid;
                mid = (sp + ep) / 2;
            } else {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int[] arr = { 0, 2, 4, 6, 8, 10 };
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter Number : ");
        int a = scan.nextInt();
        System.out.println(search(arr, a));
        scan.close();
    }
}