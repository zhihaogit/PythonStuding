package EAPI;

import java.util.Scanner;
import java.util.Random;

public class Demo06RandomGuess {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random r = new Random();
        int randomNum = r.nextInt(100) + 1;

        while (true) {
            int guessNum = sc.nextInt();
            if (randomNum > guessNum) {
                System.out.println("猜大了，重试");
            } else if (randomNum > guessNum) {
                System.out.println("猜小了，重试");
            } else {
                System.out.println("猜对了");
                break;
            }
        }

        System.out.println("game over");

        sc.close();
    }
}