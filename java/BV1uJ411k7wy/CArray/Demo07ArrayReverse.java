package CArray;

public class Demo07ArrayReverse {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 };
        System.out.println(arr);
        int last = arr.length - 1;
        for (int i = 0; i < last; i++) {
            last--;
            int tmp = arr[i];
            arr[i] = arr[last];
            arr[last] = tmp;
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
}