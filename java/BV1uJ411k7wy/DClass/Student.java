package DClass;

public class Student {

    // 成员变量
    private String name;
    private int age;
    private String alias;
    private boolean male;

    /**
     * 构造方法
     * 不要写返回值类型，不写 void
     * 不能 return一个具体返回值
     * 构造方法也可以重载
     */
    public Student() {
        System.out.println("构造方法");
    }

    public Student(String name, int age) {
        System.out.println("构造方法");
        this.name = name;
        this.age = age;
    }

    // 成员方法
    public void eat() {
        System.out.println("吃饭！");
    }

    public void sleep() {
        System.out.println("睡觉！");
    }

    public void study() {
        System.out.println("学习！");
    }

    public void play(String who) {
        System.out.println("跟" + who + "一起玩！");
    }

    public void setName(String name) {
        // this指代实例化的实例
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int getAge() {
        return age;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }

    public String getAlias() {
        return alias;
    }

    public void setMale(boolean male) {
        this.male = male;
    }

    public boolean isMale() {
        return male;
    }
}