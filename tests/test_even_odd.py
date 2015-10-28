import unittest2
import newbie


class TestEvenOdd(unittest2.TestCase):
    def test_should_return_even(self):
        even = newbie.even_odd(2)
        self.assertEqual(even, 'even')

    def test_should_return_odd(self):
        odd = newbie.even_odd(1)
        self.assertEqual(odd, 'odd')

    def test_should_throw_exception_if_text(self):
        self.assertRaises(TypeError, newbie.even_odd, 'asdf')