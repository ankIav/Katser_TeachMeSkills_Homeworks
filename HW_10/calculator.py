""""""

from classes import Calculator

while True:
    try:
        field = input('Enter the expression:\n').replace(' ', '').replace(',', '.')

        calculator = Calculator(field)

        print(calculator.calculate())
    except Exception as err:
        print(f'{err}\nTry again!')
        continue
    break


# field = input('Enter the expression:\n').replace(' ', '').replace(',', '.')
#
# calculator = Calculator(field)
#
# print(calculator.calculate())
#
# print(f'{err}\nTry again!')
