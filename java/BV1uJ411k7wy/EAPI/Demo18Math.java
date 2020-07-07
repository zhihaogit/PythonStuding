package EAPI;

public class Demo18Math {
    public static void main(String[] args) {
        // Math.abs 取整
        System.out.println(Math.abs(3.14));
        System.out.println(Math.abs(0));
        System.out.println(Math.abs(-3.14));

        // Math.ceil 向上取整
        System.out.println(Math.ceil(9.9));
        System.out.println(Math.ceil(9.1));
        System.out.println(Math.ceil(9.0));

        // Math.floor 向下取整
        System.out.println(Math.floor(9.9));
        System.out.println(Math.floor(9.1));
        System.out.println(Math.floor(9.0));

        // Math.round 四舍五入
        System.out.println(Math.round(9.5));
        System.out.println(Math.round(9.4));

        // Math.PI pi值，double
        System.out.println(Math.PI);
    }
}