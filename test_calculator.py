"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        assert 10 == calculator.divide(100, 10)

    def test_modulus(self):
        assert 5 == calculator.modulus(10, 2)

    def test_exponentiation(self):
        assert 16 == calculator.exponentiate(2, 4)

    def test_square_root(self):
        assert 5 == calculator.square_root(25)

    def test_factorial(self):
        assert 120 == calculator.factorial(5)

    def test_percentage(self):
        assert 20 == calculator.percentage(100, 2)
