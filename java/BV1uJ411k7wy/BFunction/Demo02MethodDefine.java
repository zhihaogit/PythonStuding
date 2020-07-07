package BFunction;

/**
 * 方法的三种调用格式
 * 1. 单独调用：方法名称（参数）
 * 2. 打印调用：System.out.println(方法名称(参数))
 * 3. 赋值调用
 */
public class Demo02MethodDefine {
    public static void main(String[] args) {
        // 单独调用
        sum(10, 20);
        // 打印调用
        System.out.println(sum(10, 20));
        // 赋值调用
        int res = sum(10, 20);
        System.out.println(res);
    }

    public static int sum(int a, int b) {
        int result = a + b;
        return result;
    }
}