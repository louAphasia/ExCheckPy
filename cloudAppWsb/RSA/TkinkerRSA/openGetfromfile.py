from tkinter import *

root = Tk()

with open("wpis.txt", "r") as f:
    Label(root, text=f.read()).pack()

root.mainloop()