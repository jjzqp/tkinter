from calcUI import *
from tkinter import *
import re
RE_RULE = '\([^()]+\)'

def calc(strs):
    step = 0
    while 1:
        step += 1
        result = re.search(RE_RULE, strs)
        if result:  # if exist '()'
            temp_ = result.group()
            calc_res = str(eval(temp_))
            strs = re.sub(RE_RULE, calc_res, strs, 1)  # replace  source values, Note!!! must "1" 不然会出现使用相同的结果多次替换
            print(strs, "step: %s" % step)
        else:  # if not '()'
            return eval(strs)

class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。

    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.Text1.insert(1.0, '>>> ')
    def update_new_line(self,*arg):
        strs = self.Text1.get(1.0,END).split('>>> ')
        val = strs[-1].strip('\n')
        if len(val):
            print(val)
            result = calc(val)
            print(result)
            if result:
                # 输出结果
                self.Text1.insert(END, result)
                self.Text1.insert(END, '\n')

        self.Text1.insert(END, '>>> ')
        
        
    def Text1_Return(self, event):
        # print("enter")
        self.Text1.after(100, self.update_new_line, None)


if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass