package FExtends.DemoRedPacket;
import java.util.ArrayList;
import java.util.Random;

public class Member extends User {
    public Member(int money, String name) {
        super(money, name);
    }

    public int receiveMoney(ArrayList<Integer> list) {
        int money = super.getMoney();
        int index = new Random().nextInt(list.size());
        int delta = list.remove(index);
        super.setMoney(money + delta);
        System.out.println(super.getName() + "抢了 " + delta + "块钱");
        return super.getMoney();
    }
}