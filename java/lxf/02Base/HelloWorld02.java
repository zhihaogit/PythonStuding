/**
 * public是访问修饰符，表示该 class是公开的。不写 public，也能正确编译，但这个类无法从命令行执行
 */
public class HelloWorld02 {
  /**
   * @param args static关键字表明这个函数是静态方法；void关键字表明这个方法的返回值为 void，即没有任何返回值；
   *             java入口程序规定的方法必须是静态方法；方法名必须是 main 括号里的参数必须是 String数组；
   */
  public static void main(String[] args) {
    System.out.println("hello world!");
  }
}