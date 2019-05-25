from tkinter import *
from tkinter import ttk


root=Tk()

la=ttk.Label(root, text="Starting...")

la.grid()

la.bind('<Enter>',lambda e:la.configure(text="moved mouse inside"))
la.bind('<Leave>',lambda e:la.configure(text="moved mouse outside"))
la.bind('<1>',lambda e:la.configure(text="clikck left mouse"))
#lewy to 1
la.bind('<Double-1>',lambda e:la.configure(text="Double clicked"))
la.bind('<3>',lambda e:la.configure(text="-------clicked"))
# prawy to 3
la.bind('<B3-Motion>',lambda e:la.configure(text="right button drag to %d, %d" % (e.x,e.y)))
la.bind('<B1-Motion>',lambda e:la.configure(text="left button drag to %d, %d" % (e.x,e.y)))


root.mainloop()