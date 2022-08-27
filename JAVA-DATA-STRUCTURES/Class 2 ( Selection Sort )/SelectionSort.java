package DSA.Sorting;

public class SelectionSort {

    public static void selectionsort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int small=i;
            for (int j = i; j < arr.length; j++) {
                if (arr[j]<arr[small]) {
                    small=j;
                }
            }
            int temp = arr[i];
            arr[i]=arr[small];
            arr[small]=temp;
        }
        printArray(arr);
    }
    
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(" "+arr[i]);
        }
    }

    public static void main(String[] args) {
        int[] arr={6,3,2,5,4,1,0};
        selectionsort(arr);   
             
    }
}
