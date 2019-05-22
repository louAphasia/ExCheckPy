import unittest


class TestDodawania(unittest.TestCase):

    def test_dodawanie(self):
        result = 0
        for i in range(3):
            result = result + 0.1

        self.assertAlmostEqual(result, 0.3)
