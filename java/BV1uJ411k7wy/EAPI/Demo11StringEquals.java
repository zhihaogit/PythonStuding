package EAPI;

/**
 * ==是进行对象的地址值比较
 * 
 * public boolean equals(Object obj)
 *  参数可以是任何对象，只有参数是一个字符串并且内容相同的才给 true，否则是 false
 * 注意事项：
 *  1. 任何对象都能用 Object进行接收
 *  2. equals方法具有对称性，也就是 a.equals(b)和 b.equals(a)效果一样
 *  3. 如果比较双方一个常量一个变量，推荐把常量字符串写在前面
 * 
 * public boolean equalsIgnoreCase(String str)
 *  忽略大小写，进行内容比较
 */

public class Demo11StringEquals {
    public static void main(String[] args) {
        String str1 = "abc";
        String str2 = "abc";
        char[] charArr = { 'a', 'b', 'c' };
        String str3 = new String(charArr);

        System.out.println(str1 == str3);
        System.out.println(str2.equals(str3));
        System.out.println("abc".equals(str1));
        System.out.println("abc".equals(str3));

        System.out.println("ABC".equalsIgnoreCase(str1));
        System.out.println("ABC".equalsIgnoreCase(str2));
        System.out.println("ABC".equalsIgnoreCase(str3));
    }
}