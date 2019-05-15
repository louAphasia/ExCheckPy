import sys
#WZORZEC OBIEKTOWY OPERACYJNY NAZWA POLITYKA
#Strategia WZORZEC PROJEKTOWY   ZAMKNIECIE KAPSUŁKOWANIE 2 KLASY ZAMKNIECIE
# LINII Z PLIKU I Z JEDNEJ Z TERMINALA LACZY INTERFACE

#WZORZEC KOMPOZYT  jeden plik a kilka plikow taki sam sposb
# czesto klient = petla while nasza


class ConsoleReader:
    def __init__(self):
        self.eof=False  # utowrze aby nie wystapil blad

    def readline(self):
        return input()

    def close(self):
        pass  # jest ta metoda bo pojawilby sie blad dyby z consoli reader

class FileReader:
    def __init__(self,file_name):
        self.input_file=open(file_name)
        self.eof=False   #czy natrafilem na koniec pliku

    def readline(self):
        text = self.input_file.readline()  # ---> \n  a pusty napis zwraca
        if text == '':
           self.eof=True #running = False
        if len(text) > 0 and text[-1] == '\n':
            text = text[:-1]
        return text

    def close(self):
        self.input_file.close()


class MultiReader:
    def __init__(self,readers):
        self.readers=readers  # to jest lista
        self.eof=False
        self.index_to_read=0

    def readline(self):
        text=self.readers[self.index_to_read].readline()  # [0]  musi sie zmieniac z kolejnego pliku odczytywać
        #print('index',self.index_to_read)
        if self.readers[self.index_to_read].eof  and len(self.readers)-1>self.index_to_read:
            self.index_to_read+=1
        if len(self.readers)-1==self.index_to_read:
            self.eof=True  #tez juz nie mam wiecej rzeczy do przeczytania

        return text


    def close(self):
        for reader in self.readers:
            reader.close()   #zamyka wszystkie pliki

print('params', sys.argv)

files_to_open=sys.argv[1:]

print('files', files_to_open)

# otiweral i sprawdzal czy plik ma byc czytanyif len(files_to_open)>0:
 # czy ma uzyc z konsoli czy z pliku    input_file=open(files_to_open[0])


if len(files_to_open)>0:
    file_readers=[]
    for file_name in files_to_open:
        file_reader =FileReader(file_name)  # otwieram
        file_readers.append(file_reader)
    reader=MultiReader(file_readers)
else:
    reader=ConsoleReader()

while not reader.eof:  # dopoki nie napotkalem na koniec pliku
    text=reader.readline()
    print(text)

reader.close()
