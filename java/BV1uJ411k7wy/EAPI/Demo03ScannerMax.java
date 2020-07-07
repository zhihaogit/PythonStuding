package EAPI;

import java.util.Scanner;

public class Demo03ScannerMax {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    
        System.out.println("输入第一个数字");
        int num1 = sc.nextInt();
        System.out.println("输入第二个数字");
        int num2 = sc.nextInt();
        System.out.println("输入第三个数字");
        int num3 = sc.nextInt();

        int max = num1 >= num2
            ? num1 >= num3
                ? num1
                : num3
            : num2 >= num3
                ? num2
                : num3;

        System.out.println("最大的数字是：" + max);
    
        sc.close();

    }
}