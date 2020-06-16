package FExtends;

/**
 * this关键字用来访问本类内容
 * 1. 在本类的成员方法中，访问本类的成员变量
 * 2. 在本类的成员方法中，访问本类的另一个成员方法
 * 3. 在本类的构造函数中，访问本类的另一个构造函数
 *  注意：
 *      1. this()调用也必须是构造函数的第一个语句，唯一一个
 *      2. super和 this两种构造函数，不能同时使用
 */
public class NewPhoneThis extends Phone {
    int num = 20;

    public NewPhoneThis() {
        this(30);
    }

    public NewPhoneThis(int n) {
        this.num = n;
    }

    public void showNum() {
        int num = 22;
        System.out.println(num);
        System.out.println(this.num);
    }

    public int getNum() {
        this.showNum();
        return this.num;
    }
}