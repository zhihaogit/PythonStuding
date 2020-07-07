package FExtends.DemoRedPacket;


public abstract class User {
    int money = 0;
    String name = "";

    public User() {
    }

    public User(int money, String name) {
        this.money = money;
        this.name = name;
    }

    public void show() {
        System.out.println(this.name + "的余额是 " + this.money);
    }

    public int getMoney() {
        return this.money;
    }

    public int setMoney(int money) {
        this.money = money;
        return this.money;
    }

    public String getName() {
        return this.name;
    }
}