#!/usr/bin/env python
#!/usr/bin/env python3

# 支持多种图形界面的第三方库
# Tk
# wxWidgets
# Qt
# GTK

# Tkinter
# 内置模块，封装了访问 Tk的接口
# Tk会调用操作系统提供的本地 GUI接口，完成最终的 GUI

# GUI Program
# 导入所有的包
from tkinter import *
import tkinter.messagebox as messagebox

# 从 Frame派生出一个 Application类，是所有 Widget的父容器
class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text = 'Hello, world!')
        self.helloLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.quitButton = Button(self, text = 'Hello', command = self.hello)
        self.quitButton.pack()

    # 添加可输入文本框
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题
app.master.title('Hello World')
# 主消息循环
app.mainloop()

# GUI的主线程负责监听来自操作系统的消息，并依次处理每一条消息
# 如果消息处理非常耗时，需要在新线程中处理