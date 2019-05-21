# SyntaxError  Błedy skladiowe NA ETAPIE interpretacji naszego kodu pojawiają się przed WYKONANIEM
# ZeroDevisionError
# obsługa bledow

# return False i True bledy co zwraca funkcja  umowa albo wartości SUCCESS = 0 ERR_FOUND=1 konwencja co zwraca

'''class DigitsErrors(num):
    ERR_FOUND=0
    SUCCESS=1

#porzadkuje sie w tej klasie umieszcza
def check(text):
    for x in text:
        if x not in digits:
            return ERR_FOUND'''

# EXCEPTION
# klasa BaseException
#  wyjatkki hierarchia po niej dzieddzicza all wyjatki SystemExit
# KeyboardInterrput
# Exception >  AssertionError   [ instrukcja assert
     #     > ArithmeticError - tu jest ZeroDevisionError  OverflowError
          #> ImportError
          # > RuntimeError - RecursionError NotImplementError
          # > SyntaxError
          # > ValueError


try:
    x=int('E')
    print("proba")
    x=2/0
    #kod w ktorym moze wyst wyjatek
except ArithmeticError as nazwa:
    print("zlapano wyjatek", nazwa)
    # kod obslugujacy prz tym wyjatku
except ValueError as nazwa1:
    print('kolorki blad')#kod oblsugujacy przy innym
else:
    print("wszystko udalo sie ")
    # gdy nie zgloszona bledu w try bledu wykona sie
finally:
    print("blok zawsze wykonywany")
    # wykona sie zawsze

######################## wyjatki przerywaja dzialanie funkcji
def f():
    x=int('E')
    # przerwanie tej funkcji
    print(x)

def g():
    print()
    f()
    # tu tez przerwana funkcja g
    print('wykonano g')


try:
    g()
except ValueError as e:
    print("zalapano",e)


def funk():
    try:
        x=int('15')
        return x
    except ArithmeticError as e:
        print("e")
    finally:
        print("wykona")  # blok wykona sie nawet jak jest instrukcja return

# nie chcemy obslugiwac ale chcemy aby cos sie wykonalo zawsze
try:
    plik=open("text",'r')
finally:
    plik.close()




 # class wyjatkow > wybor klasy nadrzednej zwykle Exception lub podklas tej klasy nie od BaseException
    # #tworzymy konstruktor __init__
 # raise my okreslamy kiedy wystapi blad

 #if x in string:
#   raise ValueError(x+' ')

 class EmptyString(ValueError):
     def __init__(self):
         super().__init__('String is empty')

class NotDigit(ValueError):
    pass

def check(s):
    raise EmptyString


try:
    check('5')
except (EmptyString,NotDigit) as e:
    print(e)

class MyException(Exception):
    def __init__(self):
        super().__init__()


try:
    raise MyException
except Exception:  # wykona sie ten pierwszy zawsze probuje pierwsze dopasowanie skoro dziedziczy jesli chce priorytet
    # musze zmienic kolejnosc
    print("Excp")
except MyException:
    print("MyException")


# wyjatki moga przechowywac dane

