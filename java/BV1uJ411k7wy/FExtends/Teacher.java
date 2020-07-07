package FExtends;

/**
 * 使用 super来访问父类的 方法
 * 
 * @override写在前面，装饰器，检测是不是有效的覆盖重写
 * 1. 必须保证父子类之间方法的名称相同，参数列表相同
 * 2. 子类的返回值必须 [小于等于]父类方法的返回值范围
 * 提示: java.lang.Object类是所有类的公共最高父类，java.lang.String就是 Object的子类
 * 3. 子类方法的权限必须 [大于等于]父类方法的权限修饰符
 * 提示: public > protected > (default) > private;
 * (default)不是关键字 default，而是什么都不写
 * 
 */
public class Teacher extends Employee {
    int num = 1;

    // int num2 = super.getNum();

    @Override
    public int[] getNum() {
        int num3[] = super.getNum();
        return num3;
    }
}