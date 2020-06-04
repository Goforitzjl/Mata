import tkinter as tk
import tkinter.messagebox
from DeepSearch import DeepSearch
from GreedSearch import GreedSearch
import StartGui
import random


class IndexGui:
    def __init__(self, option, size, entry):
        self.option = option
        if len(size)>3:
            self.size=int(size[0:2])
        else:
            self.size = int(size[0])
        self.entry = entry
        self.window = tk.Tk()
        print(self.entry)

    def comeBack(self):
        # self.window.withdraw()
        # self.window.quit()
        self.window.destroy()
        startgui = StartGui.StartGui()
        startgui.mainGui()

    def mainGui(self):
        self.window.title("马踏棋盘")
        width = str(self.size * 62 + 300)
        height = str(self.size * 62)
        geometry = width + "x" + height + "+500" + "+200"
        self.window.geometry(geometry)

        if self.option == "Deep":
            try:
                dstartX = ""
                dstartY = ""
                dstart = ""
                if self.entry == "":
                    dstartX = random.randint(0, self.size - 1)
                    dstartY = random.randint(0, self.size - 1)
                    dstart = (dstartX, dstartY)
                else:
                    dstartX = int(self.entry[0]) - 1
                    dstartY = int(self.entry[2]) - 1
                    dstart = (dstartX, dstartY)
                print(dstart)
                deep = DeepSearch(dstart, self.size)
                deep.start()
                dtime = deep.getTime()
                dpath = deep.getPath()
                dstep = 1
                for path in dpath:
                    tk.Label(self.window, text=dstep).grid(row=path[0] + 1, column=path[1] + 1, padx=10, pady=10,
                                                           ipadx=10,
                                                           ipady=10)
                    dstep += 1
                tk.Label(self.window, text="深度优先算法用时：" + str(dtime) + "s", font=('Arial', 12), ).place(
                    x=self.size * 62 + 30,
                    y=50, anchor='nw')
                tk.Label(self.window,
                         text="初始位置:" + "第" + str(dstartX + 1) + "行，" + "第" + str(dstartY + 1) + "列").place(
                    x=self.size * 62 + 30, y=100, anchor="nw")
                dbutton = tk.Button(self.window, text='返回首页', font=('Arial', 12), width=10, height=1,
                                    command=self.comeBack)
                dbutton.place(x=self.size * 62 + 30, y=150)
            except:
                tk.messagebox.showinfo(title='ERROR', message='抱歉，请重试！')
                self.comeBack()
        if self.option == "Greed":
            try:
                gstartX = ""
                gstartY = ""
                gstart = ""
                if self.entry == "":
                    gstartX = random.randint(0, self.size - 1)
                    gstartY = random.randint(0, self.size - 1)
                    gstart = (gstartX, gstartY)
                else:
                    gstartX = int(self.entry[0]) - 1
                    gstartY = int(self.entry[2]) - 1
                    gstart = (gstartX, gstartY)
                greed = GreedSearch(gstart, self.size)
                greed.start()
                gtime = greed.getTime()
                gpath = greed.getPath()
                print("value", gpath)
                gstep = 1
                for path in gpath:
                    tk.Label(self.window, text=gstep).grid(row=path[0] + 1, column=path[1] + 1, padx=10, pady=10,
                                                           ipadx=10,
                                                           ipady=10)
                    gstep += 1
                tk.Label(self.window, text="贪婪算法用时：" + str(gtime) + "s", font=('Arial', 12), ).place(
                    x=self.size * 62 + 30,
                    y=50, anchor='nw')
                tk.Label(self.window,
                         text="初始位置:" + "第" + str(gstartX + 1) + "行，" + "第" + str(gstartY + 1) + "列").place(
                    x=self.size * 62 + 30, y=100, anchor="nw")
                gbutton = tk.Button(self.window, text='返回首页', font=('Arial', 12), width=10, height=1,
                                    command=self.comeBack)
                gbutton.place(x=self.size * 62 + 30, y=150)
            except:
                tk.messagebox.showinfo(title='ERROR', message='抱歉，请重试！')
                self.comeBack()
        self.window.protocol("WM_DELETE_WINDOW", lambda: exit(0))
        self.window.mainloop()
