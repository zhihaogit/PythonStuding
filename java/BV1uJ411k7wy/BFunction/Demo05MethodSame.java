package BFunction;

public class Demo05MethodSame {
    public static void main(String[] args) {
        boolean res = isSame(10, 10);
        System.out.println(res);
    }

    public static boolean isSame(int a, int b) {
        // return a == b
        //     ? true
        //     : false;
        return a == b;
    }
}