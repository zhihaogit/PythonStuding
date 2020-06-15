package EAPI;

/**
 * 与转换相关的常用方法
 * 
 * public char[] toCharArray() 将当前字符串拆分成字符数组作为返回值
 * 
 * public byte[] getBytes() 获得当前字符串底层的字节数组
 * 
 * public String replace(CharSequenve oldString, CharSequence newString)
 *  将所有出现的老字符串替换成为新的字符串，返回替换之后的结果新字符串
 */

public class Demo14StringConvert {
    public static void main(String[] args) {
        String str1 = "abcdefg";
        char[] charArr = str1.toCharArray();
        System.out.println(charArr[0]);
        System.out.println(charArr.length);

        byte[] byteArr = str1.getBytes();
        System.out.println(byteArr);

        String str2 = str1.replace("e", "*");
        System.out.println(str2);
    }
}