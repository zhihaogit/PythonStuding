package CArray;

public class Demo09ArrayReturn {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 };
        System.out.println(arr);
        int[] res = returnArr(arr);
        System.out.println(res);
    }

    public static int[] returnArr(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            arr[i] *= 2;
            System.out.println(arr[i]);
        }
        System.out.println(arr);
        return arr;
    }
}