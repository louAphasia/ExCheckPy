from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Szyfrowanie RSA danych")
frame=ttk.Frame(root)
frame['padding']=(100,140)

result=StringVar()
label=ttk.Label(root,textvariable=result)
result.set("New value")
label.pack()

style = ttk.Style()
style.configure("BW.TLabel", relief="raised")

l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")

label=Label(root, text="wpisz dane",width=5,height=10,bg='red',fg='white',font='Arial 12 bold')
label.pack()



ima=PhotoImage(file='cat.gif')  # gif nie moze jpg Image format why?
label2=Label(root,image=ima)
label2.pack()



root.mainloop()