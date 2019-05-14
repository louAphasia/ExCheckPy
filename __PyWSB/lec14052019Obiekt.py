# order > podzial na funkcje / moduly pakiety > KLASY

s1kolor='red'
s1marka='bmw'

s2kolor='black'
s2marka='fiat'


def run(kolor,marka):
    print(kolor,marka)

run(s1kolor,s1marka)
run(s2kolor,s2marka)
#zmieszanie roznych aut powiazanie argumentow tylko z marka kolor i marka powiazanie

class Auto:  #klasa pomoze nam pogrupowac marke z kolorem
    def __init__(self,kolor,marka,benzyna):
        self.kolor=kolor
        self.marka=marka
        self.benzyna=benzyna

    #def czyrun(self):
     #   if self.czy_mozna():
      #      print(self.kolor,self.marka)

    def czy_mozna(self):
        return self.benzyna>10

    def run(self):
        print(self.kolor,self.marka)  #s1.run()  a nie run(s1)

class Samochod():
    def __init__(self,kolor,marka):
        self.kolor=kolor
        self.marka=marka

    def run(self):
        if self.czy_mozna_wystartowac():
             print(self.kolor,self.marka)


class SamochodBenzyna(Samochod):
    def __init__(self,kolor,marka,benzyna):
        super().__init__(kolor,marka)#self.kolor=kolor
        #self.marka=marka
        self._benzyna=benzyna  #ZMIENNA PRYWATNA
        #wszystkie zmienne

    def czy_mozna_wystartowac(self):
        return self.benzyna>20

#METODA PRYWATNA ZNAK _ FUNKCJA ZMIENNNA I SPOZA KLASY NIE MOZEMY SIE ODWOLUWAC
s1=SamochodBenzyna('red','mondeo',15)
s1.run()#zadziala dziedziczy konstruktor


class SamochodLPG(Samochod):  #dziedziczenie
    pass

'''

s1=Auto()
s1.kolor='black'
s1.marka='bmw'

#konstruktor
def init(sam,kolor,marka):
    sam.kolor=kolor
    sam.marka=marka

s2=Auto()
init(s2,'red','fiat')

run(s2)'''