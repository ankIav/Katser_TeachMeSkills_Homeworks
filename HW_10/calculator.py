""""""

from classes import Calculator


field = input('Enter the expression:\n').replace(' ', '').replace(',', '.')
calculator = Calculator(field)

# print(repr(calculator))
print(calculator.calculate())

