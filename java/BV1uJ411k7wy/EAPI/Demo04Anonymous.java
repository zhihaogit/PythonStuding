package EAPI;

import DClass.Student;

public class Demo04Anonymous {
    public static void main(String[] args) {
        Student one = new Student("haha", 18);
        int age = one.getAge();
        System.out.println(age);

        // 匿名对象
        new Student("no one", 20).eat();
    }
}