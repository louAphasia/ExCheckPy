# nie trzeba import pytest
# pytest moze wywolywac unitest
from __PyWSB.kalkulator import dziel
import unittest
# w unitest potrzebna jest klasa z dziedziczeniem i def
from unittest import *
import pytest

# python -m unitest discover
# a uruchomienie pytest wystarczy pytest wykryje oba

def test_poprawne_dziel():
     assert dziel(4,2)==2


def testdzielzero():
    with pytest.raises(ZeroDivisionError):
        dziel(4,0)

# przy main w kalkulatorze importuje kalkulator caly plik sie wykonuje od inputow unitescie
# pytest zaprotestowal OSError nie powinnien wczytywac od uzytkownika teraz jest ok if __name__=="__main__"

class test(unittest.TestCase):
    def test(self):
        w=dziel(4,2)
        self.assertEqual(w,2)

