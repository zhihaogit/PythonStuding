package CArray;
/**
 * 使用动态初始化数组的时候，其中的元素将会自动拥有一个默认值
 * 整数类型 --> 0
 * 浮点类型 --> 0.0
 * 字符类型 --> '\u0000'
 * 布尔类型 --> false
 * 引用类型 --> null
 */
public class Demo03ArrayUse {
    public static void main(String[] args) {
        int[] arr = new int[6];

        arr[1] = 3;
        System.out.println(arr[0]);
        System.out.println(arr[1]);
        System.out.println(arr[2]);
    }
}