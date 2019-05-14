class SamochodLPG():
    def __init__(self,kolor,marka,lpg):
        self.kolor=kolor
        self.marka=marka       #_SamochodLPG__lpg
        self.__lpg=lpg  #konwencja _lpg ale mozna choc regula ze tylko w tej klasie JEDEN _ A DWA POMIJA
         #PODWOJNE NIE ZADZIALA DZIEDZICZENIE

        #setter i getter

        def setLPG(self,x):
            self.__lpg=lpg
        def run(self):
            print('startuje',self.marka,self.kolor, self.__lpg)

s1=SamochodLPG('red','fiat',15)     # _Samochod_lpg

s1__lpg=40  #nic nie zostanie zmienione   w class _Samochodlpg__lpg  __lpg

#w klasie interpretuje jako _SamochodLPG__lpg


