class ObjFunc:
    def __init__(self):
        self.ala='ala ma kota'

    def __call__(self):
        print("jestem obiekt func")

    def __repr__(self):  # zwrocic napis reprezentacja tego obiektu  > __init__
        return "ala ma {}".format(self.ala)

f=ObjFunc
f() # to wywolanie funkcji f.__call__()



    #wybierana ta nadpisana z domyslnej
print( str(f))