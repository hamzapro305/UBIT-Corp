import java.util.ArrayList;
import java.util.Scanner;

public class bubble_sort {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        ArrayList<Integer> list = new ArrayList<Integer>();
        int n;
        int in;
        System.out.print("Enter lenght of list: ");
        n = input.nextInt();

        for (int j = 0; j < n; j++) {
            System.out.print("Enter Number: ");
            in = input.nextInt();
            list.add(in);
        }

        System.out.println(Bubble_sort(list));
        input.close();

    }

    static ArrayList<Integer> Bubble_sort(ArrayList<Integer> list) {

        for (int i = 0; i < list.size() - 1; i++) {
            Boolean swapped = false;
            for (int j = 0; j < list.size() - 1 - i; j++) {
                if (list.get(j) > list.get(j + 1)) {
                    int temp;
                    temp = list.get(j);
                    list.set(j, list.get(j + 1));
                    list.set(j + 1, temp);
                    swapped = true;
                }
            }
            if (!(swapped)) {
                break;
            }
        }
        return list;

    }
}