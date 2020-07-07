package BFunction;

public class Demo03MethodParam {
    public static void main(String[] args) {
        int res = func1(10, 20);
        func2();
        System.out.println(res);
    }

    // 有参函数
    public static int func1(int a, int b) {
        return a * b;
    }

    // 无参函数
    public static void func2() {
        for (int i = 0; i < 10; i++) {
            System.out.println(i);
        }
    }
}