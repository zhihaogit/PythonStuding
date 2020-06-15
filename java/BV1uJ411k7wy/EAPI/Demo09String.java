package EAPI;

public class Demo09String {
    public static void main(String[] main) {
        // 1. 使用空参数构造
        String str1 = new String();
        System.out.println(str1);

        // 2. 使用字符数组来创建
        char[] charArray = { 'A', 'B', 'C' };
        String str2 = new String(charArray);
        System.out.println(str2);

        // 3. 使用字节数组来创建
        byte[] byteArray = {97, 98, 99};
        String str3 = new String(byteArray);
        System.out.println(str3);

        // 4. 字面量创建
        String str4 = "ABCabc";
        System.out.println(str4);
    }
}