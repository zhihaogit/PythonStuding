package EAPI;

// 1. 引入 scanner类
import java.util.Scanner;

/**
 * Scanner 类来获取用户的输入
 */

public class Demo01Scanner {
    public static void main(String[] args) {
        // 2. 创建 scanner实例
        Scanner sc = new Scanner(System.in);

        // 3. 获取键盘输入的 int数字
        int num = sc.nextInt();
        System.out.println(num);

        // 4. 获取键盘输入的字符串
        String str = sc.next();
        System.out.println(str);

        // 5. 关闭文档流
        sc.close();
    }
}