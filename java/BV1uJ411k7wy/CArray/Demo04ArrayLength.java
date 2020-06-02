package CArray;

public class Demo04ArrayLength {
    public static void main(String[] args) {
        // 获取数组的长度
        // 数组一旦创建，程序运行期间，长度不可改变
        int[] arr = { 1, 2, 3, 4, 5 };
        int len = arr.length;
        System.out.println(len);
    }
}