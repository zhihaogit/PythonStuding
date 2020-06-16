package FExtends;

/**
 * super关键字的用法
 * 1. 在子类的成员方法中，访问父类的成员变量
 * 2. 在子类的成员方法中，访问父类的成员方法
 * 3. 在子类的构造方法中，访问父类的构造方法
 */

public class NewPhoneSuper extends Phone {
    int num = 30;

    public NewPhoneSuper() {
        super();
    }

    public void sendSome() {
        super.send();
    }

    public int getParentNum() {
        return super.num;
    }
}