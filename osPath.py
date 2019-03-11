from os.path import abspath, curdir, join, isdir
from os import rename, listdir

x=abspath(curdir)
print(x)

print(curdir)

#rename("openF\writeeeeen.txt","openF\writen.txt")

def showFoo(path):
    print(join(path,"foo"))

showFoo("\ExCheckPy")

class DieFound(Exception):
    pass

def detect():
    for item in listdir(curdir):
        if isdir(item):
            raise DieFound(abspath(item))

print