class Interpreter:
    def __init__(self):
        self.variables=dict()
        self.is_running=True

    def execute(self,line):

        splitl=line.split()

        if len(splitl)>0 and splitl[0] == '#':
            return
        if len(splitl)>2 and splitl[1]=='=':
            self.variables[splitl[0]]=splitl[2]
        if len(splitl)>0 and splitl[0]=='exit()':
            self.is_running=False

        print('linia',line)
        print('zmienne',self.variables)



def main():
    i=Interpreter()

    #is_running=True
    while i.is_running:
        x=input()
        i.execute(x)

