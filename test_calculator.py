import pytest
from calculator import ClassCalculator

class Test:

	def test_sum_01(self):
		calculator = ClassCalculator()
		assert calculator.sum(5,5) == 10

	def test_sum_02(self):
		calculator = ClassCalculator()
		assert calculator.sum(100,500) == 600

	def test_sum_02(self):
		calculator = ClassCalculator()
		assert calculator.sum(50,-50) == 0

	def test_minus(self):
		calculator = ClassCalculator()
		assert calculator.minus(5,5) == 0

	def test_minus(self):
		calculator = ClassCalculator()
		assert calculator.minus(500,-500) == 1000

	def test_minus(self):
		calculator = ClassCalculator()
		assert calculator.minus(100,50) == 50

	def test_multiply(self):
		calculator = ClassCalculator()
		assert calculator.multiply(2,4) == 8

	def test_multiply(self):
		calculator = ClassCalculator()
		assert calculator.multiply(50,-4) == -200

	def test_multiply(self):
		calculator = ClassCalculator()
		assert calculator.multiply(200, 5) == 1000 

	def test_divide(self):
		calculator = ClassCalculator()
		assert calculator.divide(4,2) == 2

	def test_radical(self):
		calculator = ClassCalculator()
		assert calculator.radical(25) == 5

	def test_log(self):
		calculator = ClassCalculator()
		assert calculator.log(100, 10) == 2

	def test_factorial(self):
		calculator = ClassCalculator()
		assert calculator.factorial(5) == 120

	def test_absolute(self):
		calculator = ClassCalculator()
		assert calculator.abs(-5) == 5