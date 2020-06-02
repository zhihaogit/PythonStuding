package BFunction;

public class Demo04MethodReturn {
    public static void main(String[] args) {
        int res = func1(10, 30);
        System.out.println(res);

        func2(10, 20);
    }

    // 有返回值
    public static int func1(int a, int b) {
        return a + b;
    }

    /**
     * 无返回值
     * 无返回值函数不能打印调用，赋值调用，只能直接调用
     */
    public static void func2(int a, int b) {
        int res = a + b;
        System.out.println(res);
    }
}