package EAPI;

/**
 * public String substring(int begin, int end)
 *  截取从 begin开始，一直到 end结束，中间的字符串
 *  左闭右开
 */

public class Demo13StringSubstring {
    public static void main(String[] args) {
        String str1 = "HelloWorld";
        String str2 = str1.substring(5);
        String str3 = str1.substring(2, 5);
        System.out.println(str2);
        System.out.println(str3);
    }
}