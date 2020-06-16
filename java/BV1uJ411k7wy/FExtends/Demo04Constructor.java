package FExtends;

/**
 * 继承关系中，父子类构造方法的访问特点
 * 1. 子类构造方法当中有一个默认隐含的 super()调用，所以一定是先调用父类构造，在调用子类构造
 * 2. 子类构造可以通过 super关键字来调用 父类重载构造
 * 3. super的父类构造调用，必须是子类的构造方法的第一个语句。不能一个子类构造调用多次 super构造
 */
public class Demo04Constructor {
    public static void main(String[] args) {
        NewPhone one = new NewPhone();

        System.out.println(one.getNum());
    }
}