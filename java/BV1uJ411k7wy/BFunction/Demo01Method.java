package BFunction;
/**
 * 方法不能定义在方法中，即方法不能嵌套
 * 对于方法最后一行 return可以省略不写
 */
public class Demo01Method {
    public static void main(String[] args) {
        mySelf();
    }

    public static void mySelf() {
        System.out.println("my name");
    }
}