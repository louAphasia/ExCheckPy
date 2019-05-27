import tkinter
from tkinter import *

def write():
    file=open("plik.txt",'a+')
    file.write(meinf.get()+ '\n')
    file.close()

gui=Tk()

meinf=Entry(gui)
meinf.grid(row=9,column=1)

buttonwrite=Button(gui)
buttonwrite.config(text="write to file", command=write)
buttonwrite.grid(row=8,column=1)

gui.mainloop()