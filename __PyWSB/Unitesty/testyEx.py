from __PyWSB.WSB_class import CzasChyla


import  unittest


# TDD tworzymy testy 2 krok uruchamiamy test uruchomienie testow weryfikuje czy poprawnie configure tools do testowania
# 3 krok implementacja 4 uruchamiamy

class TimeTesty(unittest.TestCase):

    def setUp(self):
        self.jakas=[1,2,3,4]

    def tearDown(self):
        # co trzeba przygotowac
        pass

    def test_constructor_object_with_timestamp_as_string(self):
        t=CzasChyla.Czas("3 h 19 min")
        print(self)
        self.assertEqual(t._godz,3)
        self.assertEqual(t._minuty,19)

    def test_error_ujemne(self):
        with self.assertRaises(CzasChyla.InvalidTimeException):
            t = CzasChyla.Czas(-1, -20)

    def test_constructor_with_hour_integershourminutes(self):
        t=CzasChyla.Czas(2,33)

        self.assertEqual(t._godz,2)
        self.assertEqual(t._minuty,33)


        # testy jak minuty i godziny sa 0 jak oba sa ujemne a jedno ujemne a drugie

    def test_to_string_returns_correct_with_positive_value(self):
        t=CzasChyla.Czas(1,20)

        time=t.to_string()

        self.assertEqual(time,"1 h 20 min")

    #dopisac inne testy gdy godzina mniejsza od zera

    def test_add_minutes(self):
        t=CzasChyla.Czas(0,3)

        s=t.add(CzasChyla.Czas(0,18))

        self.assertEqual(s._godz,0)
        self.assertEqual(s._minuty,21)

    def test_add_ponad_60_minutes(self):

        t=CzasChyla.Czas(0,57)
        s=t.add(CzasChyla.Czas(0,4))

        self.assertEqual(s._godz,1)
        self.assertEqual(s._minuty,1)

    def test_only_hour(self):
        t=CzasChyla.Czas(2,0)
        s=t.add(CzasChyla.Czas(3,0))
        self.assertEqual(s._godz,5)
        self.assertEqual(s._minuty,0)

    def test_add_hours_minutes(self):

        t=CzasChyla.Czas(2,29)
        s=t.add(CzasChyla.Czas(1,32))
        self.assertEqual(s._godz,4)
        self.assertEqual(s._minuty,1)




