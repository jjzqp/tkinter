'''
1.如果你没有指定 Label 的大小，那么 Label 的尺寸是正好可以容纳其内容
2.可以通过 height 和 width 选项来明确设置 Label 的大小:如果你显示的是文本，那么这两个选项是以文本单元为单位定义 Label 的大小；如果你显示的是位图或者图像，那么它们以像素为单位（或者其他屏幕单元）定义 Label 大小
3.可以通过 foreground（或 fg）和 background（或 bg）选项来设置 Label 的前景色和背景色。你也可以选择 Label 中的文本用哪种字体来显示
4.还可以使用 #RRGGBB 的格式指定具体的颜色值，例如 “#%02x%02x%02x” % (123, 188, 233)
5.可以显示 Tkinter 变量的内容。言下之意就是当变量的内容发生改变时，Label 中显示的内容也会自动更新
6. Label 显示 PhotoImage 和 BitmapImage 对象
'''
import tkinter as tk
longtext = """
Label 可以显示多行文本，你可以直接使用换行符
或使用 wraplength 选项来实现。当文本换行的时
候，你可以使用 anchor 和 justify 选项来使得
文本如你所希望的显示出来。
"""
root = tk.Tk()

label1 = tk.Label(root,text="Hello",width=10,height=10)
label2 = tk.Label(root,text="World",font={"Courier New",12},fg="red",bg="black")
label3 = tk.Label(root,text=longtext,anchor="w",justify="left")

label_v = tk.StringVar()  #定义lable字符变量
label4 = tk.Label(root,textvariable=label_v)
label_v.set("new value")

photo = tk.PhotoImage(file="888.gif")
label5 = tk.Label(root,image=photo)
label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()

root.mainloop()



