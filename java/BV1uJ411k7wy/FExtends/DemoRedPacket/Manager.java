package FExtends.DemoRedPacket;
import java.util.ArrayList;

public class Manager extends User {
    ArrayList<Integer> totalMoneyArr = new ArrayList<>();

    public Manager(int money, String name) {
        super(money, name);
    }

    public ArrayList<Integer> sendMoney(int sum, int count) {
        int money = super.getMoney();
        if (sum > money) {
            System.out.println("余额不足");
        } else {
            System.out.println(super.getName() + "发了 " + sum + "块钱");
            super.setMoney(money - sum);
            int per = sum / count;
            int last = sum % count;

            for (int i = 0; i < count; i++) {
                if (i < count - 1) {
                    this.totalMoneyArr.add(per);
                } else {
                    this.totalMoneyArr.add(per + last);
                }
            }
        }
        return this.totalMoneyArr;
    }
}