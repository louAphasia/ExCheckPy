
#  nie musi byc print('fr',__name__)

def add(a,b):
    return a+b

if __name__=='__main__':

    a=int(input('podaj a'))
    b=int(input('podaj b'))

    print('dodawanie',add(a,b))


#dwa pliki jeden na testy a jeden na dzialania  z assert

#__init__.py plik mowi ze to jest pakiet  from . import strings.py
# obecny pakiet .   init py skrótowy zapis  wtedy bedzie tylko import utils a pozniej utils.string.czy_liczba()

#unitest  #doctest

#PyPI   swoje tools spo putest pycodestyle=poprawny stylistycznie PEP8

# requirements.txt jakie biblioteki jakie wersje sa w venv przy projekcie potrzebne nie musi pobierać
#django flask

#a=2; b=3;c=5
#print('{2},{1},{0}'.format(a,b,c))

#z linii kodu pythona wirtualne srodowisko
# python3 -m venv env
#python3 -m venv venv [nazwa katalogu
# jak duzy du -hs env
#jak ma uzywac pythona z wirtualnego
# source env/bin/activate   [pod linuxem]
# po znaku zachety (env)  pip install pakiet tylko tu
#pycodestyle utils.py  bledy stylistyczne spacje entery
# deactivate [wirtualne srodowisko turn off]
