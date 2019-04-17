run=True
while run==True:
    liczba1=input("podaj liczbe x ")
    liczba2=input("podaj liczbe y ")
    l=int(liczba1)
    n=int(liczba2)
    count=input("jakie chcesz wykonac dzialnie na liczbach x i y  + czy - czy : czy * ")
    if count == "+":
        print("x+y = " ,l+n)
    elif count == "-":
        print("x-y = ", l-n)
    elif count =="*":
        print("x*y =", l*n)
    elif count ==":":
        if n==0:
            raise ZeroDivisionError("Don divide by 0")
        else:
            print("x:y =", l/n)
    cont=input("chcesz kontunowac?")
    if cont=="no":
        run=False




#imie=input("podaj imie:  ")

#print("Hello", imie)