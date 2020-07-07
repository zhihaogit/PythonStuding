package FExtends;

/**
 * 
 */
public class Demo03Override {
    public static void main(String[] args) {
        Teacher one = new Teacher();

        System.out.println(one.getNum());

        NewPhone two = new NewPhone();
        two.call();
        two.send();
        two.show();
    }
    
}