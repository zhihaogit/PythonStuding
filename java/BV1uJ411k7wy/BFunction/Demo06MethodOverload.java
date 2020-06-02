package BFunction;

/**
 * 方法的重载（overload）：多个方法的名称一样，参数列表不一样
 * 注意事项
 * 方法重载与下列有关
 * 1. 参数的个数不同
 * 2. 参数的类型不同
 * 3. 参数的多类型顺序不同
 * 方法重载与下列无关
 * 1. 与参数的名称无关
 * 2. 与方法的返回值类型无关
 */

public class Demo06MethodOverload {
    public static void main(String[] args) {
        int res = sum(10, 20, 30, 40);
        System.out.println(res);
    }

    public static int sum(double a, int b) {
        System.out.println('2');
        return (int) (a + b);
    }

    public static double sum(double a, double b) {
        System.out.println('2');
        return a + b;
    }

    public static int sum(int a, int b) {
        System.out.println('2');
        return a + b;
    }

    public static int sum(int a, int b, int c) {
        System.out.println('3');
        return a + b + c;
    }

    public static int sum(int a, int b, int c, int d) {
        System.out.println('4');
        return a + b + c + d;
    }
}