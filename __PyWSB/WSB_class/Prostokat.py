class Prostokat:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return 2*self.a+2*self.b


def main():
    a = int(input("podaj a:"))
    b = int(input("podaj b:"))

    prostokat = Prostokat(a, b)

    print("Pole:", prostokat.pole())

if __name__=='__main__':
    main()
