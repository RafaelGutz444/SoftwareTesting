from unittest import TestCase
from app.math import Math


class TestMath(TestCase):
    def setUp(self):
        self._math = Math()

    def test_add_two_positive_numbers(self):
        self.assertEqual(self._math.add(10, 20), 30)

    def test_multiply_two_positive_numbers(self):
        self.assertEqual(self._math.multiply(10, 4), 40)

    def test_divide_two_positive_numbers(self):
        self.assertEqual(self._math.divide(40, 2), 20)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self._math.divide(2, 0)

    def test_is_even(self):
        self.assertEqual(self._math.is_even(4), True)

    def test_power(self):
        self.assertEqual(self._math.power(2, 8), 256)

    def test_is_prime_negative_number(self):
        with self.assertRaises(ValueError):
            self._math.is_prime(-1)

    def test_is_prime_zero(self):
        self.assertEqual(self._math.is_prime(0), False)

    def test_is_prime_small_number(self):
        self.assertEqual(self._math.is_prime(3), True)

    def test_is_prime_even(self):
        self.assertEqual(self._math.is_prime(6), False)

    def test_is_prime_prime_num(self):
        self.assertEqual(self._math.is_prime(13), True)

    def test_factorial(self):
        self.assertEqual(self._math.factorial(7), 5040)

    def test_factors_zero(self):
        with self.assertRaises(ValueError):
            self._math.factors(0)

    def test_factors_one(self):
        self.assertEqual(self._math.factors(1), [1])

    def test_factors_pos_number(self):
        self.assertEqual(self._math.factors(6), [1, 2, 3, 6])
