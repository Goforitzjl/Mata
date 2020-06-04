import tkinter as tk
import IndexGui
from tkinter import ttk


class StartGui:

    def __init__(self):
        self.window = tk.Tk()
        self.radiobuttonVar = tk.StringVar()
        self.ccboxVar = tk.StringVar()
        self.entry = tk.StringVar()

    def start(self):
        # self.window.withdraw()
        self.window.destroy()
        indexgui = IndexGui.IndexGui(self.radiobuttonVar.get(), self.ccboxVar.get(), self.entry.get())  # get()!!
        indexgui.mainGui()

    def mainGui(self):
        self.window.title("马踏棋盘")
        self.window.geometry("350x300+500+200")
        self.radiobuttonVar.set("Deep")
        self.ccboxVar.set("5x5")
        self.entry.set("")
        tk.Label(self.window, text='算法选择:', font=('Arial', 15), ).place(x=50, y=50, anchor='nw')
        tk.Label(self.window, text='棋盘大小:', font=('Arial', 15), ).place(x=50, y=100, anchor='nw')
        tk.Label(self.window, text='起始位置:', font=('Arial', 15), ).place(x=50, y=150, anchor='nw')
        tk.Label(self.window, text='(如果为空则随机生成)', font=('Arial', 9), ).place(x=230, y=150, anchor='nw')
        tk.Entry(self.window, show=None, textvariable=self.entry, font=('Arial', 12), width=8).place(x=150, y=150,
                                                                                                     anchor="nw")
        r1 = tk.Radiobutton(self.window, text='深度优先算法', variable=self.radiobuttonVar, value='Deep',
                            )
        r1.place(x=150, y=50, anchor="nw")
        r2 = tk.Radiobutton(self.window, text='贪心算法', variable=self.radiobuttonVar, value='Greed',
                            )
        r2.place(x=250, y=50, anchor="nw")

        ccbox = tk.ttk.Combobox(self.window, textvariable=self.ccboxVar, height=40, width=8)
        ccbox.place(x=150, y=100, anchor="nw")
        ccbox["value"] = ("5x5", "6x6", "7x7", "8x8", "9x9", "10x10", "15x15", "20x20")
        ccbox.current(0)

        button = tk.Button(self.window, text='开始', font=('Arial', 12), width=10, height=1, command=self.start)
        button.place(x=125, y=200, anchor="nw")
        self.window.protocol("WM_DELETE_WINDOW", lambda: exit(0))
        self.window.mainloop()
