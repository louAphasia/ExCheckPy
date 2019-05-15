class Colors:
    def __init__(self):
        self.colors=dict()


    def to_hex(self):
        self.colors = {'Red': '#2345', 'Blue': '#243456'}
        color=input("podaj kolor  ")
        print(self.colors.get(color))


def main():

    c=Colors()
    #assert c.to_hex('Red')=='#2345'
    #assert c.to_hex('Blue') =='#243456'
    #print(c.to_hex())
    c.to_hex()

if __name__=='__main__':
    main()