def input_digital_check(variable_number):
    """
    check variables on correctly input (digital)
    """

    while True:
        number = input(
            'Input a digital value of %s: ' % variable_number)  # number is string

        try:
            number = int(number)  # trying to make number integer
        except ValueError:  # if not integer

            try:
                number = float(number)  # trying to make number float
            except ValueError:  # if not float
                print(
                    "You've entered a wrong value of %s, try again!" % variable_number)
                continue  # run cycle again
            else:  # if exception was not in float(number), that is means input was correct and break cycle WHILE
                break

        else:  # if exception was not in int(number), that is means input was correct and break cycle WHILE
            break

    return number


def input_operation_check(list_operators_keys):
    """
    check operation for correct input
    """
    while True:
        operation_type = input(
            'Input type of operation between number 1 and 2: ')

        if operation_type in list_operators_keys:
            break

        else:
            print("You've entered wrong operation, try again!")

    return operation_type


def sum_calculator_of_two_numbers(number1, number2):
    """
    calculator function of 2 numbers
    """
    return number1 + number2


def minus_calculator_of_two_numbers(number1, number2):
    """
    calculator function of 2 numbers
    """
    return number1 - number2


def multiply_calculator_of_two_numbers(number1, number2):
    """
    calculator function of 2 numbers
    """
    return number1 * number2


def divide_calculator_of_two_numbers(number1, number2):
    """
    calculator function of 2 numbers
    """
    try:
        return number1 / number2

    except ZeroDivisionError:
        return 'Division by zero!'


number_1 = input_digital_check('first number')
number_2 = input_digital_check('second number')

operators = {'+': sum_calculator_of_two_numbers(number_1, number_2),
             '-': minus_calculator_of_two_numbers(number_1, number_2),
             '*': multiply_calculator_of_two_numbers(number_1, number_2),
             '/': divide_calculator_of_two_numbers(number_1, number_2),
             }

operation = input_operation_check(operators.keys())

for key, value in operators.items():
    if operation == key:
        print(value)
