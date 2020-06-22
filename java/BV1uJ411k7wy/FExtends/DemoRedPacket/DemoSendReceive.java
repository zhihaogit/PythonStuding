package FExtends.DemoRedPacket;
import java.util.ArrayList;

public class DemoSendReceive {
    public static void main(String[] args) {
        Manager manager = new Manager(100, "manager");
        Member A = new Member(10, "A");
        Member B = new Member(12, "B");
        Member C = new Member(14, "C");

        manager.show();
        A.show();
        B.show();
        C.show();

        ArrayList<Integer> list = manager.sendMoney(31, 3);
        A.receiveMoney(list);
        B.receiveMoney(list);
        C.receiveMoney(list);

        manager.show();
        A.show();
        B.show();
        C.show();
    }
}