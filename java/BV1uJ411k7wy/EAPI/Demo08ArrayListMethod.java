package EAPI;

import java.util.ArrayList;

public class Demo08ArrayListMethod {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();

        // 添加元素
        list.add("1");
        list.add("2");
        list.add("3");
        list.add("4");
        list.add("5");

        // 根据索引获取元素
        String num0 = list.get(0);
        String num2 = list.get(2);
        System.out.println(num0);
        System.out.println(num2);

        // 根据索引删除元素
        list.remove(0);
        System.out.println(list);

        // 获取长度
        int size = list.size();
        System.out.println(size);

        // 遍历操作
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }
    }
}