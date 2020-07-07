package EAPI;

import java.util.Arrays;

/**
 * java.util.Arrays是一个与数组相关的工具类，里面提供了大量的静态方法
 * public static String toString(数组): 将参数数组变成字符串（按照默认格式 [元素1, 元素2...]）
 * public static void sort(数组): 按照默认升序（从大到最小）对数组的元素进行排序
 */

public class Demo17Arrays {
   public static void main(String[] args) {
       int[] intArray = { 10, 20, 30 };
       String intStr = Arrays.toString(intArray);
       System.out.println(intStr);

       int[] arr1 = { 1, 2, 3, 324, 2, 2 };
       Arrays.sort(arr1);
       System.out.println(Arrays.toString(arr1));
   }
}