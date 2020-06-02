package BFunction;

public class Demo07MethodOverloadSame {
    public static void main(String[] args) {
        byte a = 10;
        byte b = 20;
        boolean res = isSame(a, b);
        System.out.println(res);
    }

    public static boolean isSame(byte a, byte b) {
        return a == b;
    }

    public static boolean isSame(short a, short b) {
        return a == b;
    }

    public static boolean isSame(int a, int b) {
        return a == b;
    }

    public static boolean isSame(long a, long b) {
        return a == b;
    }
}