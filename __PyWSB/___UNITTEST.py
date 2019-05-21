#testy jednostkowe  pojedyncze moduly
# integracyjne systemowe [dodatkowe tools ] akceptacyjne

# Unittest  nie wymaga instalacji
# test fixture = akcje przed testem i po testem np. polaczenie z danym serwerem
# # test case = przypadkowy test /test suite = grupowanie testów moga byc zagniezdzone

# test nazwa pliku nazywa się od test_  albo katalog testz z __init__
# SUT system under test
import unittest



def czyLiczba():
        pass

class CzyLiczba(unittest.TestCase):

 # wazne aby nazwa zaczynala sie od test_
    def test_poprawna_liczba_dodatnia(self):
        result= czyLiczba("5")
        self.assertTrue(result)

        # inne assertEqual(a,b)
        # assertFalse(x)
        # assertIs*a,b(  assertIsNot(a,b)

        # assertIsNone(  assertIn


# Case 0.1 * 10 == 1  False   10 razy 0.1   0,9999999999999999999999999999999999
# 3,33333333333333  komputer ograniczone miejsce w pamięci  wiec przechowa 3.333 a nie 3.33(3)
# komputer w binarnym liczy 0.1 w dzisietnym skonczona a w binarnym nie da sie zapisac
# procesor robi przyblizenie tej liczby
# PAMIĘTAĆ !!!!!!!!!!! JAK porownac 0.1*10 == 1.00   wartosc bezwg  | 9.9999 - 10 |  < 0.01   granica bledu
# tak porownujemy liczby  float z .   Bibliotek funkcje
# assertAlmostEqual*a,b)   round(a-b,7( ==0

#assertGreater*(
#(a wartosc uzyskana a b ta ktora oczekujemy

# test sprwdza jedna rzecz np. dodawanie  polaczenia uruchomienie to inne testy

#class TestKalkulator(unittest.TestCase):

 #   def setUp(self):
  #      self.kalkulator()

    #terminal python -m unittest tests.utils_strings   w formie importu
    # python -m unittest -v tests/utils/test/pu
    # python -m unitest discover { sam szuka testow

'''class Check(unittest.TestCase):
    def test_liczba(self):
        with self.assertRaises(AttributeError)''' # ten ktory sie spodziewamy