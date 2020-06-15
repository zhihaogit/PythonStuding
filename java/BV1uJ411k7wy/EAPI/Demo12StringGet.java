package EAPI;

/**
 * String当中与获取有关的常用方法有
 * 
 * public int length() 获取字符串当中含有的字符个数，拿到字符串长度
 * public String concat(String str) 将当前字符串和参数字符串拼接，并返回新的字符串
 * public char charAt(int index) 获取指定索引位置的单个字符
 * public int indexOf(String str) 查找参数字符串在本字符串当中首次出现的索引位置，没有返回 -1
 */

public class Demo12StringGet {
    public static void main(String[] args) {
        String str1 = "Hello";
        char[] charArr = {'W', 'o', 'r', 'l', 'd'};
        String str2 = new String(charArr);
        String str3 = str1.concat(str2);

        System.out.println(str1);
        System.out.println(str2);
        System.out.println(str3);
        
        int str3Len = str3.length();
        System.out.println(str3Len);

        char char1 = str3.charAt(2);
        System.out.println(char1);

        int index1 = str3.indexOf("llo");
        int index2 = str3.indexOf("lllo");
        System.out.println(index1);
        System.out.println(index2);
    }
}