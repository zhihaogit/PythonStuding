# 分形树
from turtle import *

# 设置色彩模式是 rgb
colormode(255)

lt(90)

lv = 14
l = 120
s = 45

width(lv)

# 初始化 rgb颜色
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(1)
pendown()
fd(1)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set the color
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)

speed('fastest')

draw_tree(l, 4)

done() 
