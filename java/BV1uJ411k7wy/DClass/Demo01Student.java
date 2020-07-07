package DClass;
/**
 * 1. 导包
 * import 包名称.类名称
 * 对于和当前类属于同一个包的情况，可以省略导包语句不写
 * 
 * 2. 创建
 * new 类名称()
 * 
 * 3. 使用其中的成员变量，格式
 * 对象名.成员变量名
 */
public class Demo01Student {
    public static void main(String[] args) {

        // 1. 导包
    
        // 2. 实例化
        Student stu = new Student("ggg", 17);
    
        // 3. 使用成员变量
        System.out.println(stu.getName()); // null
        System.out.println(stu.getAge());  // 0

        stu.setName("hahaha");
        stu.setAge(18);
        System.out.println(stu.getName());
        System.out.println(stu.getAge());

        // 4. 使用成员方法
        stu.eat();
        stu.play("hehehe");
    }
    
}