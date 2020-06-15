package EAPI;

/**
 * 分割字符串的方法
 * public String[] split(String regex)
 * 参数是一个正则表达式
 */
public class Demo15StringSplit {
    public static void main(String[] args) {
        String str1 = "1,2,3,4";
        String[] str1Arr = str1.split(",");
        System.out.println(str1Arr.length);

        String str2 = "1.2.3.4";
        String[] str2Arr = str2.split("\\.");
        for (int i = 0; i < str2Arr.length; i++) {
            System.out.println(str2Arr[i]);
        }
        System.out.println(str2Arr);
    }
}