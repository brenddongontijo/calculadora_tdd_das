import pytest
from calculator import ClassCalculator

def test_sum():
	calculator = ClassCalculator()
	assert calculator.sum(5,5) == 10
