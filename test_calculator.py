import pytest
from calculator import ClassCalculator

def test_sum():
	calculator = ClassCalculator()
	assert calculator.sum(5,5) == 10

def test_minus():
	calculator = ClassCalculator()
	assert calculator.minus(5,5) == 0

def test_multiply():
	calculator = ClassCalculator()
	assert calculator.multiply(2,4) == 8

def test_divide():
	calculator = ClassCalculator()
	assert calculator.divide(4,2) == 2
