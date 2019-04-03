class Fraction:
    def __init__(self,top,bottom):
        self.num=top
        self.den=bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self, other_fra):
        new_num=self.num*other_fra.den+\
            self.den*other_fra.num
        new_den=self.den*other_fra.den

        common=gcd(new_num,new_den)

        return Fraction(new_num//common,new_den//common)

    def __mul__(self,other_fra):
        new_num=self.num*other_fra.num
        new_den=self.den*other_fra.den

        common=gcd(new_num,new_den)
        return Fraction(new_num//common,new_den//common)

def gcd(m,n):
    while m%n!=0:
        oldm=m
        oldn=n

        m=oldn
        n=oldm%oldn
    return n

x=Fraction(3,4)
y=Fraction(6,8)

print(x+y)
print(x*y)