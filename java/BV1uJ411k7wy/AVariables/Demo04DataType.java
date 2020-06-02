package AVariables;

public class Demo04DataType {
    /**
     * 自动类型转换（隐式）
     *  1. 特点：代码不需要进行特殊处理，自动完成
     *  2. 规则：数据范围从小到大
     * 强制类型转换（显式）
     * 
     * @param args
     */
    public static void main(String[] args) {
        System.out.println(100);      // 100    整数，默认就是 int类型
        System.out.println(100.431);  // 100.431     浮点数，默认是 double类型

        // 左边是 long类型，右边是默认的 int类型，左右不一样，隐式转换
        // int ---> long
        long num1 = 100;
        System.out.println(num1); // 100

        // 左边是 double类型，右边是 float类型，左右不一样，隐式转换
        // float ---> double
        double num2 = 2.5F;
        System.out.println(num2); // 2.5

        // 左边是 float类型，右边是 long类型，左右不一样，隐式转换
        // long ---> float
        float num3 = 100L;
        System.out.println(num3); // 100.0
    }
}