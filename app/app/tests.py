"""
Tests for the calculator functions
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test that two numbers are subtracted from each other"""
        res = calc.subtract(15, 10)
        self.assertEqual(res, 5)
