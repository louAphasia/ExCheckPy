
def dziel(a,b):
    if b==0:
        return 0 # tu powinnien raise FAILED
    return a/b


def main():
    x=int(input("podajx"))
    y=int(input("podaj y"))

    print("wynik",dziel(x,y))


#print("__name__", __name__)  # importuje kalkulator
if __name__=="__main__":
    main()