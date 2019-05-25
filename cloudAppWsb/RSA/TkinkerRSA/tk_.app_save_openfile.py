from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


# funkcje
def calculate(*args):
    try:
        value=float(feet.get())
        meters.set((0.3*value*10000+0.5)/10000)
    except ValueError:
        pass

#def save as
def saveasfile():
    savea=filedialog.asksaveasfile(mode='w', defaultextension='.txt')

    if savea:
        texttosave=feeten.get()
        savea.write(texttosave)
        savea.close()
    else:
        messagebox.showinfo("Error","cancelled")

# otwiera plik ale z dysku jako open as
def openfile():
    filename="wpis"
    filename=filedialog.askopenfilename(initialdir="/",title="Open file",filetypes=(("Text files", "*.txt"),("All Files", "*.*")))


#### funkcja save do pliku
def save():
    filename='wpis.txt'
    if filename:
        texta=feeten.get()
        savet=open(filename,'a')
        savet.write(texta)
        savet.close()
    else:
        messagebox.showinfo("Error", "no file open")
# tkinker MAIN

root=Tk()
root.title("Szyfrowanie RSA")

#MAINFRAME

mainframe=ttk.Frame(root,padding="10 10 12 12")
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)

#feet do funkcji
feet=StringVar()
meters=StringVar()

# FEET ENTRY

feeten=ttk.Entry(mainframe,width=10, textvariable=feet)
feeten.grid(column=2,row=1,sticky=(N,S))

# LABEL  Button w MAINFRAME
ttk.Label(mainframe,textvariable=meters).grid(column=2,row=2,sticky=(W,E))


ttk.Button(mainframe,text="Szyfruj",command=calculate).grid(column=3,row=3,sticky=W)
ttk.Button(mainframe,text="Zapisz do pliku", command=save).grid(column=2,row=3,sticky=W)
ttk.Button(mainframe,text="Otworz plik z dysku ", command=openfile).grid(column=1,row=3,sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1,row=2,sticky=E)
ttk.Label(mainframe, text="wynik").grid(column=3,row=2,sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5,pady=5)

#feeten.focus()  nie wiem co to robi
root.bind('<Return>',calculate)

#label=Label(root, text='Szyfrowania RSA')
#label.pack()

#ttk.Button(root,text="SAVE").grid()

root.mainloop()