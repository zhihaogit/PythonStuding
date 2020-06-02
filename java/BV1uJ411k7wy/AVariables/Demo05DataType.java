package AVariables;

/**
 * 强制类型转换
 *  1. 特点：代码需要进行特殊的格式处理，不能自动完成
 *  2. 格式：范围小的类型 范围小的变量名 = (范围小的类型) 原本范围大的数据
 * 
 * 注意事项
 *  1. 强制类型转换一般不推荐使用，因为有可能发生精度损失、数据溢出
 *  2. byte/short/char这三种类型都可以发生数学运算
 *  3. byte/short/cahr这三种类型在运算的时候，都会被首先提升成为 int类型，然后再计算
 *  4. boolean类型不能发生类型转换
 */
public class Demo05DataType {
    public static void main(String[] args) {
        // 左边是 int类型，右边是 long类型，不一样，需要强制类型转换
        int num1 = (int) 100L;
        System.out.println(num1); // 100

        // long强制转换为 int类型
        // 可能会发生了数据溢出
        int num2 = (int) 6000000000L;
        System.out.println(num2); // 1705032704

        // double强制转换为 int类型
        // 精度损失，小数点后的数字丢失
        int num3 = (int) 3.14;
        System.out.println(num3); // 3

        char char1 = 'A';
        System.out.println(char1 + 1); // 66，'A'字符的 ascii码相加

        byte num4 = 123;
        byte num5 = 123;
        // byte res1 = num4 + num5;
        // num4和 num5相加会先变成 int，运算之后还是 int类型
        int res2 = num4 + num5;
        System.out.println(res2);

        short num6 = 12;
        short num7 = 34;
        // num6和 num7相加会先变成 int，结果也是 int类型，可以将结果强制转换成 short类型
        short res3 = (short) (num6 + num7);
        System.out.println(res3); // 46
    }
}