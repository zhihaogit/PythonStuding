public class BooleanCalculate {
  public static void main(String[] args) {
    // 布尔运算
    // 比较运算符： > >= < <= == !=
    // 与或非：&& || !
    boolean isGreater = 5 > 3;

    // 短路运算
    boolean result = true || (5 / 0 > 0); // true

    // 三元运算符
    int n = -100;
    int x = n >= 0 ? n : -n;
  }
}