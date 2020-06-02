package CArray;
/**
 * 数组
 * 概念：是一种容器，可以同时存放多个数据值
 * 特点：
 * 1. 数组是一种引用数据类型
 * 2. 数组当中的多个数据，类型必须统一
 * 3. 数组的长度在程序运行期间不可改变
 * 初始化方式：
 * 1. 动态初始化（指定长度）
 * 数据类型[] 数组名称 = new 数据类型[数组长度];
 * 2. 静态初初始化（指定内容）
 * 数据类型[] 数组名称 = new 数据类型[]{元素1, 元素2, ...};
 * 省略格式的静态初始化
 */
public class Demo01Array {
    public static void main(String[] args) {
        // 动态初始化
        int[] arr1 = new int[5];
        double[] arr2 = new double[6];
        String[] arr3 = new String[7];
        // 声明过程，拆分成两步
        int[] arr7;
        arr7 = new int[7];

        // 静态初始化的标准格式
        int[] arr4 = new int[] { 5, 10, 15, 20 };
        String[] arr5 = new String[] { "hello", "world", "!" };
        // 声明过程，拆分成两步
        int[] arr8;
        arr8 = new int[] { 0, 1, 2 };

        // 静态初始化的省略格式
        // 声明过程，不能拆分成两步
        int[] arr6 = { 10, 20, 30 };
    }
}