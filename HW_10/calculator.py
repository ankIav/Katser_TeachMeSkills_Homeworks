""""""

from classes import Calculator


field = input('Enter the expression:\n').replace(' ', '').replace(',', '.')
calculator = Calculator(field)

print(str(calculator))
print(calculator._plus())

