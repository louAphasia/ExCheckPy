from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Szyfrowanie RSA danych")
frame=ttk.Frame(root)
frame['padding']=(100,140)

label=Label(root, text="wpisz dane")
label.pack()


root.mainloop()