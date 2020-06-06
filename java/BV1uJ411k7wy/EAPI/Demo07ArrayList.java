package EAPI;

import java.util.ArrayList;

/**
 * ArrayList是一个数组队列，相当于动态数组
 * 容量可以动态增长
 * 可以添加、删除、修改、遍历
 * ArrayList中的操作不是线程安全的，建议单线程中才使用
 * <>里面是泛型，泛型只能是引用类型
 * 希望向集合 ArrayList当中存储基本类型数据，必须使用基本类型对应的 包装类
 * 基本类型 包装类（引用类型，包装类都位于 java.lang中）
 * byte     Byte
 * short    Short
 * int      Integer
 * long     Long
 * float    Float
 * double   Double
 * char     Character
 * boolean  Boolean
 * 从 JDK1.5+开始，支持自动装箱，自动拆箱
 * 自动装箱：基本类型 --> 包装类型
 * 自动拆箱：包装类型 --> 基本类型
 */

public class Demo07ArrayList {
    public static void main(String[] args) {
        // 创建一个集合，里面装的都是 String字符串类型的数据
        // 从 JDK1.7开始，右侧的尖括号内部可以不写内容，但是 <>本身还是要写
        ArrayList<String> list = new ArrayList<>();
        System.out.println(list);

        // 向集合中添加一些数据，需要用到 add方法
        list.add("HHAA");
        System.out.println(list);

        list.add("HAHA");
        list.add("HAAH");
        System.out.println(list);

        ArrayList<Integer> intList = new ArrayList<>();
        intList.add(1);
        intList.add(2);
        intList.add(3);
        System.out.println(intList);
    }
}