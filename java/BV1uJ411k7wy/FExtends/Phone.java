package FExtends;

public class Phone {
    int num;
    public Phone() {
        System.out.println("Phone constructor");
    }
    public Phone(int args) {
        num = args;
        System.out.println("Phone constructor, params: " + num);
    }

    public void call() {
        System.out.println("call someone");
    }

    public void send() {
        System.out.println("send");
    }

    public void show() {
        System.out.println("show number");
    }
}