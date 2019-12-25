# 海龟绘图（Turtle Graphics）
# 在1966年，Seymour Papert和Wally Feurzig发明了一种专门给儿童学习编程的语言——LOGO语言，它的特色就是通过编程指挥一个小海龟（turtle）在屏幕上绘图

# 导入 turtle包的所有内容
from turtle import *

# 设置笔刷宽度
width(4)

# 前进
forward(200)

# 右转 90度
right(90)

# 笔刷颜色
pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

# 调用 done()使得窗口等待被关闭，否则将立刻关闭窗口
# 窗口进入消息循环，等待被关闭
done()
