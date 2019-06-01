from tkinter import *
from tkinter import ttk
from ExCheckPy.cloudAppWsb.RSAcloud.szyfrowanieTekstu import *
from ExCheckPy.cloudAppWsb.RSA.encryptASCIIdecrypt import *
from tkinter import messagebox
import tkinter as tk


# funkcje £ szyfrujaca i  zapisujaca do pliku
def szyfruj():

    filename='encrypted_file.txt' # nadanie nazwy pliku w którym będzie zapisany zaszyfrowany tekst
    filename2='decrypted_file.txt'
    mode='encrypt'  # moze byc 'decrypt'  WYBIERAMY TRYB

    # otwieramy tekst do szyfrowania

    if mode == 'encrypt':
        with open(r'rekordy.txt', 'r', encoding='utf-8') as r:
            message= r.read()
            print(message)
        # generujemy klucze publiczne i prywatne pobieramy klucz pod indeksem [0] a prywatny pod [1]
        pubiprivKey= genKeys()
        print(pubiprivKey)
        publKey=pubiprivKey[0]
        privKey=pubiprivKey[1]

        makeKeyFiles('klucz',pubiprivKey)



        x=TextIndexDec(message)
        print('ords',x)
        e= encrypted(x,publKey)
        print('encrypted',e)
        dch=DecCharASCII(e)
        print(dch)
        WriteToFile(filename,dch)

    #if mode == 'decrypt':

        m = readFileKey('klucz_privkey.txt')
        print(m)
        re=ReadFromFile(filename)
        print(re)
        o=ChrnaOrds(re)
        print("ords",o)
        de=decrypted(o,m)
        print("decrypted",de)
        dee=DecCharASCII(de)
        print(dee)



# 2 funkcje zliczajace rekordy WPISANE
def rekords():
    c = -1
    for c, wiersz in enumerate(open('rekordy.txt', 'r')):
        pass
    c += 1
    return c

def countRekords():
    account=rekords()
    return value.set(account)


def close_window ():
    root.destroy()



#### funkcja save do pliku WPISYWANE REKORDY
def save():
    filename='rekordy.txt'
    if filename:
        data1=feeten1.get()

        data2=feeten2.get()
        data3=feeten3.get()
        savet=open(filename,'a')
        savet.write(data1+' ')
        savet.write(data2+' ')
        savet.write(data3+'\n')
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
surname=StringVar()
name=StringVar()
pesel=IntVar()

value=IntVar()

# FEET ENTRY
label_surname=ttk.Label(mainframe,text='NAZWISKO').grid(column=1,row=1,sticky=(W,E))
feeten1=ttk.Entry(mainframe,width=40, textvariable=surname)
feeten1.grid(column=2,row=1,sticky=(N,S),columnspan=2)

label_name=ttk.Label(mainframe,text='IMIE').grid(column=1,row=2,sticky=(W,E))
feeten2=ttk.Entry(mainframe,width=40, textvariable=name)
feeten2.grid(column=2,row=2,sticky=(N,S),columnspan=2)

label_pesel=ttk.Label(mainframe,text='PESEL').grid(column=1,row=3,sticky=(W,E))
feeten3=ttk.Entry(mainframe,width=40, textvariable=pesel)
feeten3.grid(column=2,row=3,sticky=(N,S),columnspan=2)
# LABEL  Button w MAINFRAME

label_rekordy=ttk.Label(mainframe,text="liczba wpisanych Rekordów").grid(column=4,row=1,sticky=(W,E))
label_rekordyCount=ttk.Label(mainframe,width=50,textvariable=value).grid(column=4,row=2,sticky=(W,E))

ttk.Button(mainframe,text="Dodaj",command=save).grid(column=2,row=4,sticky=W)

ttk.Button(mainframe,text="Szyfruj i przeslij",command=szyfruj).grid(column=3,row=4,sticky=W)

tk.Button(mainframe,text="pokaż ilosc rekordow",relief="raised",command=countRekords).grid(column=4,row=3)


ttk.Button (mainframe, text = "Zamknij", command = close_window).grid(column=4, row=4)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5,pady=5)

#feeten.focus()  nie wiem co to robi
#root.bind('<Return>',calculate)

#label=Label(root, text='Szyfrowania RSA')
#label.pack()

#ttk.Button(root,text="SAVE").grid()

root.mainloop()