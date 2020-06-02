package AVariables;

public class Demo01Const {
    public static void main(String[] args) {
        // 字符串常量 双引号括起来的 n个字符为字符串常量，双引号括起来的内容可以为空
        System.out.println("ABC");
        System.out.println("");
        System.out.println("DEF");

        // 整数常量
        System.out.println(30);
        System.out.println(-500);

        // 浮点数常量
        System.out.println(3.1415926);
        System.out.println(-2.5);

        // 字符常量 单引号括起来的单个字符是字符常量
        System.out.println('A');
        System.out.println('6');
        // 字符常量必须有且仅有一个字符，没有不行
        // System.out.println('');
        // 字符常量必须有且仅有一个字符，多个不行
        // System.out.println('AB');

        // 布尔常量
        System.out.println(true);
        System.out.println(false);

        // 空常量 null，空常量不能直接用来打印输出
        // System.out.println(null);
    }
}