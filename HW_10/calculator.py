""""""

from classes import Calculator


field = input('Enter the expression:\n').replace(' ', '').replace(',', '.')
calculator = Calculator(field)

print(calculator._plus())
print(str(calculator))
