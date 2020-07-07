package AVariables;

public class Demo03VariableNotice {
    public static void main(String[] args) {
        /**
         * 定义一个变量，但没有进行赋值，直接打印输出就是错误的
         */
        // int num1;
        // System.out.println(num1);

        /**
         * 变量不能在声明前使用，也不能超出作用域使用
         */
        {
            // System.out.println(num2);
            int num2 = 10;
            System.out.println(num2);
        }
        // System.out.println(num2);

        /**
         * 一个语句生成多个变量，一般情况下，不推荐
         */
        int a, b, c;
        a = 10;
        b = 20;
        c = 30;

        int d = 10, e = 20, f = 30;
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(d);
        System.out.println(e);
        System.out.println(f);
    }
}