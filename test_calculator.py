import pytest
from calculator import ClassCalculator

class Test:

	def test_sum_01(self):
		calculator = ClassCalculator()
		assert calculator.sum(5,5) == 10
		assert calculator.sum(100,500) == 600
		assert calculator.sum(50,-50) == 0

	def test_minus(self):
		calculator = ClassCalculator()
		assert calculator.minus(5,5) == 0
		assert calculator.minus(500,-500) == 1000
		assert calculator.minus(100,50) == 50

	def test_multiply(self):
		calculator = ClassCalculator()
		assert calculator.multiply(2,4) == 8
		assert calculator.multiply(50,-4) == -200
		assert calculator.multiply(200, 5) == 1000 

	def test_divide(self):
		calculator = ClassCalculator()
		assert calculator.divide(4,2) == 2
		assert calculator.divide(100,-5) == -20
		assert calculator.divide(50,5) == 10

		with pytest.raises(ZeroDivisionError):
			calculator.divide(100,0)


	def test_radical(self):
		calculator = ClassCalculator()
		assert calculator.radical(25) == 5
		assert calculator.radical(256) == 16
		assert calculator.radical(81) == 9

	def test_log(self):
		calculator = ClassCalculator()
		assert calculator.log(100, 10) == 2

	def test_factorial(self):
		calculator = ClassCalculator()
		assert calculator.factorial(5) == 120

	def test_absolute(self):
		calculator = ClassCalculator()
		assert calculator.abs(-5) == 5