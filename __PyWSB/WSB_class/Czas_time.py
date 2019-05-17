from datetime import time

class Czas:
    def __init__(self,godz,minuty):
        self.__time=time(hour=godz,minute=minuty)


    def to_string(self)->str:
        print(self.__time)

    def dodaj(self,t):
        x=t.split('h')
        c=Czas(x[0],x[1])
        return (self.__time - c)

    def odejmij(self,t):
        x =int(t.split('h'))
        c = Czas(x[0], x[1])
        return (self.__godz - c.x[0], self.__minuty - x[1])

    def pomnoz(self,ile):
        return (self.__godz*ile,self.__minuty*ile)



def main():

    c=Czas(12,30)
    c.to_string()

    c.odejmij('10 h 20')





if __name__== '__main__':
    main()