/**
 * 整数的数值表示不但是精确的，而且整数运算永远是精确的，即使是除法也是精确的，因为两个整数相除只能得到结果的整数部分
 * 整数由于存在范围限制，如果计算结果超出了范围，就会产生溢出，但不会报错
 * 
 */
public class IntCalculate {
  public static void main(String[] args) {
    int x = 12345 / 67;
    int y = 12345 % 67;

    // 自增，自减
    x++;
    ++x;
    y--;
    --y;

    // 移位操作
    int n = 7;
    // 左移 1位
    int a = n << 1; // 14
    int b = n >> 1; // 3
  }
}