from datetime import time

class Czas:
    def __init__(self,time):
        self.time=time.split('h',1)
        self.__godz=self.time[0]
        self.__minuty=self.time[1]


    def to_string(self)->str:
        x=int(self.__godz)
        s = self.__minuty.strip('min')
        y=int(s)
        t=time(x,y)
        m=t.strftime("%I:%M%p")
        return m

    def dodaj(self,t):
        x=t.split('.')
        a=int(self.__godz)
        s=self.__minuty.strip('min')
        c=int(x[0])
        d=int(x[1])
        b=int(s)
        n2=(b+d)%60
        if n2==0:
            a=a+1
        n1 = (a + c) % 24
        t=time(n1,n2)
        m = t.strftime("%I:%M%p")
        return m


    def odejmij(self,t):
        x = t.split('.')
        a = int(self.__godz)
        s = self.__minuty.strip('min')
        c = int(x[0])
        d = int(x[1])
        b = int(s)
        n2 = abs(b - d)%60
        n1 = abs(a - c) % 24
        t = time(n1, n2)
        m = t.strftime("%I:%M%p")
        return m

    #print(f"%0{4}d" % (d))

    def pomnoz(self,ile):
        a = int(self.__godz)
        s = self.__minuty.strip('min')
        b = int(s)
        n1 = (a*ile)%24
        n2 = (b*ile)%60
        t = time(n1, n2)
        m = t.strftime("%I:%M%p")
        return m



def main():

    c=Czas("12 h 30 min")
    print(c.to_string())
    print(c.dodaj('9.30'))
    print(c.odejmij('8.35'))
    print(c.pomnoz(2))






if __name__== '__main__':
    main()