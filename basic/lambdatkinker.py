import sys
from tkinter import Button, mainloop

x=Button(
    text='Push me',
    command=(lambda:sys.stdout.write('jesss\n')))
x.pack()
mainloop()