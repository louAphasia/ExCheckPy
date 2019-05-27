import unittest

from czas import Czas,InvalidTimeException

class TestTime(unittest.TestCase):

    def test_construct_object_with_string(self):
        t = Czas("1 h 19 min")

        self.assertEqual(t._godz, 1)
        self.assertEqual(t._minuty, 19)

    def test_construct_object_with_hour_and_minutes_as_integers(self):
        t = Czas(1, 19)

        self.assertEqual(t._godz, 1)
        self.assertEqual(t._minuty, 19)

    def test_construct_with_positive_horu_and_negative_minute(self):
        with self.assertRaises(InvalidTimeException):
            t = Czas(1, -20)


    def test_to_string_with_positive_hour_and_minute(self):
        t = Czas(1, 20)

        self.assertEqual(t.to_string(), "1 godz 20 min")

    def test_to_string_with_positive_hour_and_zero_minutes(self):
        t = Czas(2, 0)

        self.assertEqual(t.to_string(), "2 godz 0 min")

    def test_to_string_when_hour_is_zero(self):
        t = Czas(0, 12)

        self.assertEqual(t.to_string(), "0 godz 12 min")

    def test_to_string_when_hour_and_minute_is_zero(self):
        t = Czas(0, 0)

        self.assertEqual(t.to_string(), "0 godz 0 min")


    def test_add_with_only_minutes(self):
        t = Czas(0, 3)

        s = t.add(Czas(0, 18))

        self._assertOriginalObjectIsUnchanged(t, 0, 3)

        self.assertEqual(s._godz, 0)
        self.assertEqual(s._minuty, 21)

    def test_add_when_minutes_comes_to_hours(self):
        t = Czas(0, 57)

        s = t.add(Czas(0, 4))

        self._assertOriginalObjectIsUnchanged(t, 0, 57)

        self.assertEqual(s._godz, 1)
        self.assertEqual(s._minuty, 1)

    def test_add_only_hours(self):
        t = Czas(2, 0)

        s = t.add(Czas(3, 0))

        self._assertOriginalObjectIsUnchanged(t, 2, 0)

        self.assertEqual(s._godz, 5)
        self.assertEqual(s._minuty, 0)

    def test_add_hours_and_minutes(self):
        t = Czas(2, 29)

        s = t.add(Czas(1, 32))

        self._assertOriginalObjectIsUnchanged(t, 2, 29)

        self.assertEqual(s._godz, 4)
        self.assertEqual(s._minuty, 1)


    def test_sub_with_zero(self):
        t = Czas(7, 31)

        s = t.sub(Czas(0, 0))

        self._assertOriginalObjectIsUnchanged(t, 7, 31)

        self.assertEqual(s._godz, 7)
        self.assertEqual(s._minuty, 31)

    def test_sub_only_minutes(self):
        t = Czas(7, 40)

        s = t.sub(Czas(0, 20))

        self._assertOriginalObjectIsUnchanged(t, 7, 40)

        self.assertEqual(s._godz, 7)
        self.assertEqual(s._minuty, 20)

    def test_sub_should_change_hours_when_subtracting_minutes(self):
        t = Czas(7, 40)

        s = t.sub(Czas(0, 41))

        self._assertOriginalObjectIsUnchanged(t, 7, 40)

        self.assertEqual(s._godz, 6)
        self.assertEqual(s._minuty, 59)


    def test_multiply_by_zero(self):
        t = Czas(7, 31)

        s = t.multiply(0)

        self._assertOriginalObjectIsUnchanged(t, 7, 31)

        self.assertEqual(s._godz, 0)
        self.assertEqual(s._minuty, 0)

    def test_multiply_only_minutes(self):
        t = Czas(0, 20)

        s = t.multiply(2)

        self._assertOriginalObjectIsUnchanged(t, 0, 20)

        self.assertEqual(s._godz, 0)
        self.assertEqual(s._minuty, 40)

    def test_multiply_when_minutes_exceedes_one_hour_should_increase_hours(self):
        t = Czas(0, 31)

        s = t.multiply(2)

        self._assertOriginalObjectIsUnchanged(t, 0, 31)

        self.assertEqual(s._godz, 1)
        self.assertEqual(s._minuty, 2)

    def test_multiply_when_minutes_exceedes_six_hours_should_increase_hours(self):
        t = Czas(0, 31)

        s = t.multiply(12)

        self._assertOriginalObjectIsUnchanged(t, 0, 31)

        self.assertEqual(s._godz, 6)
        self.assertEqual(s._minuty, 12)

    def _assertOriginalObjectIsUnchanged(self, t, original_h, original_m):
        self.assertEqual(t._godz, original_h)
        self.assertEqual(t._minuty, original_m)