from calculator.arithmetic import get_numbers, addition, subtraction, multiplication, division
from unittest import TestCase
from unittest.mock import patch

class TestArithmetic(TestCase):
    def setUp(self):
        self.positive_numbers = [6, 12]
        self.negative_numbers = [-6, -12]
        self.mix_numbers = [-6, 12]

    @patch('builtins.input', return_value='6 12 3')
    def test_get_numbers(self, mock_input):
        result = get_numbers()
        expected = [6.0, 12.0, 3.0]
        self.assertEqual(result, expected)

    @patch('builtins.input', return_value='6,12,3')
    def test_get_numbers_with_comma_as_separator(self, mock_input):
        with self.assertRaises(ValueError) as context:
            get_numbers()
        self.assertEqual(str(context.exception), "Masukkan angka dengan spasi sebagai pemisah dan gunakan '.' ketika menggunakan desimal.")

    @patch('builtins.input', return_value='6')
    def test_get_numbers_with_one_number(self, mock_input):
        with self.assertRaises(ValueError) as context:
            get_numbers()
        self.assertEqual(str(context.exception),"Harap masukkan Angka lebih dari satu!")

    def test_addition_positive_number(self):
        self.assertEqual(addition(self.positive_numbers), 18)

    def test_addition_negative_number(self):
        self.assertEqual(addition(self.negative_numbers), -18)

    def test_addition_mix_number(self):
        self.assertEqual(addition(self.mix_numbers), 6)

    def test_subtraction_positive_number(self):
        self.assertEqual(subtraction(self.positive_numbers), -6)

    def test_subtraction_negative_number(self):
        self.assertEqual(subtraction(self.negative_numbers), 6)

    def test_subtraction_mix_number(self):
        self.assertEqual(subtraction(self.mix_numbers), -18)

    def test_multiplication_positive_number(self):
        self.assertEqual(multiplication(self.positive_numbers), 72)

    def test_multiplication_negative_number(self):
        self.assertEqual(multiplication(self.negative_numbers), 72)

    def test_multiplication_mix_number(self):
        self.assertEqual(multiplication(self.mix_numbers), -72)

    def test_division_positive_number(self):
        self.assertEqual(division(self.positive_numbers), 0.5)

    def test_division_negative_number(self):
        self.assertEqual(division(self.negative_numbers), 0.5)

    def test_division_mix_number(self):
        self.assertEqual(division(self.mix_numbers), -0.5)

    def test_division_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as context:
            division([12, 0])
        self.assertEqual(str(context.exception), "Anda tidak bisa membagi bilangan dengan angka 0!")
        