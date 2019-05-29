from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk


# funkcje £ szyfrujaca i druga zapisujaca do pliku
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
feet1=StringVar()
pesel=IntVar()

# FEET ENTRY
label_surname=ttk.Label(mainframe,text='NAZWISKO').grid(column=1,row=1,sticky=(W,E))
feeten1=ttk.Entry(mainframe, textvariable=feet)
feeten1.grid(column=2,row=1,sticky=(N,S),columnspan=2)

label_name=ttk.Label(mainframe,text='IMIE').grid(column=1,row=2,sticky=(W,E))
feeten2=ttk.Entry(mainframe, textvariable=feet1)
feeten2.grid(column=2,row=2,sticky=(N,S),columnspan=2)

label_pesel=ttk.Label(mainframe,text='PESEL').grid(column=1,row=3,sticky=(W,E))
feeten3=ttk.Entry(mainframe, textvariable=pesel)
feeten3.grid(column=2,row=3,sticky=(N,S),columnspan=2)
# LABEL  Button w MAINFRAME

label_rekordy=ttk.Label(mainframe,text="liczba wpisanych Rekordów").grid(column=4,row=1,sticky=(W,E))
label_rekordyCount=ttk.Label(mainframe,textvariable=meters).grid(column=4,row=2,sticky=(W,E))

ttk.Button(mainframe,text="Dodaj",command=calculate).grid(column=2,row=4,sticky=W)

ttk.Button(mainframe,text="Szyfruj i przeslij",command=calculate).grid(column=3,row=4,sticky=W)






tk.Button(mainframe,text="pokaż ilosc rekordow",relief="raised").grid(column=4,row=4)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5,pady=5)

#feeten.focus()  nie wiem co to robi
root.bind('<Return>',calculate)

#label=Label(root, text='Szyfrowania RSA')
#label.pack()

#ttk.Button(root,text="SAVE").grid()

root.mainloop()