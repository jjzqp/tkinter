'''
1. 如果你没有指定 **Label **的大小，那么 Label的尺寸是正好可以容纳其内容而已。你可以使用 padx 和 pady 选项在 Button 的内容和边框间添加额外的间距。
2. 当然你可以通过 height 和 width 选项来明确设置 Button 的大小：如果你显示的是文本，那么这两个选项是以文本单元为单位定义 **Button **的大小；如果你显示的是位图或者图像，那么它们以像素为单位（或者其他屏幕单元）定义 **Button **大小
3. 对于内容为文本的 Button 组件，你可以使用像素为单位指定 Buttton 的尺寸
'''
import tkinter as tk
root = tk.Tk()

def callback():
    print("call function")
btn = tk.Button(root,text="call",command=callback)
btn.pack()

f = tk.Frame(root,width=64,height=64)
f.pack_propagate(0)
f.pack()
btn = tk.Button(root,text="call2",command=callback)
btn.pack(fill="both",expand=1)

root.mainloop()
