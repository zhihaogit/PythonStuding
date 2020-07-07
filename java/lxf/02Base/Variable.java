public class Variable {
  /**
   * @param args
   * 
   * 基本数据类型（cpu可以直接进行运算的类型）
   * 整数类型：byte, short, int, long
   * 浮点数类型：float, double
   * 字符类型：char
   * 布尔类型：boolean
   * 
   * 整形类型，java只定义了带符号的整型
   * byte: -128 ~ 127
   * short: -32768 ~ 32767
   * int: -2147483648 ~ 2147483647
   * long: -9223372036854775808 ~ 9223372036854775807
   * 
   * 
   * 引用类型
   * 除了上述基本类型，剩下都是引用类型
   * 常用的引用类型是 String字串
   * String s = "hello";
   */
  public static void main(String[] args) {
    int x = 10;
    System.out.println(x);

    // 定义整型
    int i = 2147483647;
    int i2 = -2147483648;
    int i3 = 2_000_000_000; // 加下划线更容易识别
    int i4 = 0xff0000;      // 十六进制表示的 16711680
    int i5 = 0b1000000000;  // 二进制表示的 512
    long l = 9000000000000000000L;

    // 定义浮点型
    float f1 = 3.14f;
    float f2 = 3.14e38f;
    double d = 1.79e308;
    double d2 = -1.79e308;
    double d3 = 4.9e-324;

    // 布尔类型
    boolean b1 = true;
    boolean b2 = false;
    boolean isGreater = 5 > 3;
    int age = 12;
    boolean isAdult = age >= 18;

    // 字符类型
    char a = 'A';
    char zh = '中';

    // 字符串类型
    String b = "这是一个字串";
  
    /**
     * 常量
     * 加上 final修饰符，这个变量就变成常量了
     * 常量在初始化后不可重新赋值
     */
    final double PI = 3.14;
    double r = 5.0;
    double area = PI * r * r;
    // PI = 300;  // error

    /**
     * var关键字
     * 类型的名字过长，为了省略，可以用 var关键字
     * 编译器会根据赋值语句自动推断出变量德类型
     */

     StringBuilder sb = new StringBuilder();
    //  var sb1 = new StringBuilder();

    /**
     * 变量的作用域
     * 多行语句用 {}括起来
     * 语句块中定义的变量，它有一个作用域，就是从定义处开始，到语句块结束
     * 超出了作用域引用这些变量，编译器就会报错
     */

  }
}