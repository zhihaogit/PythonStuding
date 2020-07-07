package EAPI;

import java.util.Random;

public class Demo05Random {
    public static void main(String[] args) {
        Random r = new Random();
        // 随机获取一个 int数字
        int num = r.nextInt();
        System.out.println(num);

        int num2 = r.nextInt(20);
        System.out.println(num2);

        int num3 = r.nextInt(9) + 1;
        System.out.println(num3);
    }
}