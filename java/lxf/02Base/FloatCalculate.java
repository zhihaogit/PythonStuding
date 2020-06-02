/**
 * 浮点数运算和整数运算相比，只能进行加减乘除计算，不能进行位运算和移位运算
 * 由于浮点数存在运算误差，所以比较两个浮点数是否相等常常会出现错误的结果
 * 浮点数在内存的表示方法和整数比更加复杂
 */
public class FloatCalculate {
  public static void main(String[] args) {
    double x = 1.0 / 10;
    double y = 1 - 9.0 / 10;
    // 比较 x和 y是否相等，先计算其差的绝对值：
    double r = Math.abs(x - y);
    // 再判断绝对值是否足够小
    if (r < 0.00001) {
      // 可以认为相等
    } else {
      // 不相等
    }

    // 类型提升
    // 如果参与运算的两个数其中一个是整型，那么整型可以自动提升到浮点型
    int n = 5;
    double d = 1.2 + 24.0 / n; // 6.0
    System.out.println(d);

    // 溢出
    // 整数运算在除数为 0时会报错，而浮点数运算在除数为 0时，不会报错，但会返回几个特殊值
    NaN       // 表示 Not a Number
    Infinity  // 表示无穷大
    -Infinity // 表示负无穷大
    double d1 = 0.0 / 0;  // NaN
    double d2 = 1.0 / 0;  // Infinity
    double d3 = -1.0 / 0; // -Infinity

    // 强制类型转换
    int n1 = (int) 12.3; // 12
  }
}