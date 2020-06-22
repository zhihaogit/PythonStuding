package FExtends;

/**
 * 抽象类：抽象方法所在的类必须是抽象类，class前面加 abstract
 * 抽象方法：加上 abstract关键字，去掉大括号
 * 
 * 使用抽象类：
 * 1. 不能直接创建 new抽象类对象
 * 2. 必须使用一个子类继承抽象父类
 * 3. 子类内部必须覆盖重写所有抽象方法
 * 4. 创建子类实例进行使用
 * 
 * 注意事项：
 * 1. 抽象类不能创建对象，如果创建，编译无法通过而报错。只能创建其非抽象子类的对象
 * 2. 抽象类中，可以有构造方法，是供子类创建对象时，初始化父类成员而使用
 * 3. 抽象类中，不一定含有抽象方法，有抽象方法的类一定是抽象类
 * 4. 抽象类的子类必须重写抽象类中的所有抽象方法，除非是该子类也是抽象类
 */
public abstract class ClassAnimalAbstract {
    public abstract void eat();

    public void normalEat() {
        System.out.println("normal eat method");
    }
}