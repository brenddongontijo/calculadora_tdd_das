from math import sqrt
from math import log

class ClassCalculator:
	def sum(self, firstNumber, secondNumber):
		return firstNumber + secondNumber

	def minus(self, firstNumber, secondNumber):
		return firstNumber - secondNumber

	def multiply(self, firstNumber, secondNumber):
		return firstNumber * secondNumber

	def divide(self, firstNumber, secondNumber):
		return firstNumber / secondNumber

	def radical(self, number):
		return sqrt(number)

	def log(self, number, base):
		return log(number, base)