package GInterface;

public class Demo02Interface {
    public static void main(String[] args) {
        MyInterfaceDefaultA impl = new MyInterfaceDefaultA();

        impl.methodAbs();
        impl.methodAbs2();
    }
}