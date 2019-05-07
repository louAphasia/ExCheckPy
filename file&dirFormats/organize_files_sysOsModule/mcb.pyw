import shelve, sys
from ExCheckPy import pyperclip

mcbsh=shelve.open('mcb')
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    mcbsh[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcbsh.keys())))
    elif sys.argv[1] in mcbsh:
        pyperclip.copy(mcbsh[sys.argv[1]])
mcbsh.close()