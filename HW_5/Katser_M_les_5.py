"""
This module completes homework of the 5 lesson
TODO: just run this code, in this program realized choice of task to start
    in def main()
"""

import time


def decorator_pursuance_time(function_to_decorate):
    """
    Decorator counts time to pursuance some function and print this time
    and execute definition print_task().
    """

    def wrapper(arg):
        """
        Structure of decoration.
        """

        start_time = time.time()
        print_task(arg)
        function_to_decorate(arg)
        print(f'{time.time() - start_time} seconds')

    return wrapper


def print_task(task_num: int):
    """
    :param task_num: get task number to print it
    :return: None, just print formatted task
    """

    print('-' * 79 + '\n' + f'Task {task_num}'.center(79))
    dict_tasks = {1: 'Написать лямбда-функцию, определяющую четное/нечетное. '
                     'Функция принимает \nпараметр (число) и если оно четное, '
                     'то выдает слово "четное", если нет - \n"нечетное".'
                     + '\n' + '-' * 79,
                  2: 'Дан список чисел. Вернуть список, где при помощи функции'
                     ' map() каждое число \nпереведено в строку. В качестве '
                     'функции в map использовать lambda.'
                     + '\n' + '-' * 79,
                  3: 'При помощи функции filter() из кортежа слов '
                     'отфильтровать только те, которые \nявляются палиндромами'
                     ' (которые читаются одинаково в обе стороны).'
                     + '\n' + '-' * 79,
                  5: '**Сделать функцию, которая вход принимает строку. '
                     'Анализирует ее исключительно \nметодом .isdigit() без '
                     'доп. библиотек и переводит строку в число. Функция умеет'
                     ' \nраспознавать отрицательные числа и десятичные дроби.'
                     + '\n' + '-' * 79,
                  }

    for key, value in dict_tasks.items():
        if task_num == key:
            print(value)


def input_to_int(message: str) -> int:
    """
    This definition is used to correct input of whole numbers
    :param message: get string to print due message
    :return: integer value.
    """

    while True:
        integer = input(message)

        if integer.find('-') == 0 and integer.replace('-', '', 1).isdigit():
            integer = int(integer)
            break

        elif integer.isdigit():
            integer = int(integer)
            break

        else:
            print(f'Wrong value of {integer}')
            continue

    return integer


def input_to_int_or_float(message: str) -> int | float:
    """
    This definition is used to correct input of integer or float numbers
    :param message: get string to print due message
    :return:integer or float value.
    """

    while True:
        int_float = input(message)

        if (
                '-.' in int_float
                and int_float.find('-.') == 0
                and int_float.replace('-.', '', 1).isdigit()
        ):
            int_float = float(int_float.replace("-.", "-0."))
            break
        elif (
                '-' in int_float and '.' in int_float
                and int_float.find('-') == 0
                and int_float.replace('-', '', 1).replace('.', '', 1).isdigit()
        ):
            int_float = float(int_float)
            break

        elif '.' in int_float and int_float.replace('.', '', 1).isdigit():
            int_float = float(int_float)
            break

        elif (
                '-' in int_float
                and int_float.find('-') == 0
                and int_float.replace('-', '', 1).isdigit()
        ):
            int_float = int(int_float)
            break

        elif int_float.isdigit():
            int_float = int(int_float)
            break

        else:
            print('Wrong value, try again!')
            continue

    return int_float


def list_in_range(len_list: int) -> list:
    """
    Creating a list of elements from a keyboard with length of list
    :param len_list: length of list
    :return: a list of elements from a keyboard.
    """

    list_elements = [
        input_to_int_or_float(f'Enter the {__iter__ + 1} element: ')
        for __iter__ in range(len_list)
    ]

    return list_elements


def filter_palindrome(word: str) -> bool:
    """
    :param word: every element of tuple
    :return: True or False
    """

    if len(word) <= 1:
        return False

    elif word[:len(word) // 2] == word[:(len(word) // 2) - 1:-1]:
        return True

    else:
        return False


@decorator_pursuance_time
def task_1(tusk_num: int):
    """
    This def to complete Task 1.
    :param tusk_num: number of task
    :return: string, which contains check even or odd integer.
    """

    integer = input_to_int('Enter some integer:\n')

    lambda_even_obb = lambda x: 'Even' if x % 2 == 0 else 'Odd'

    print(lambda_even_obb(integer))


@decorator_pursuance_time
def task_2(tusk_num: int):
    """
    This def to complete Task 1.
    :param tusk_num: number of task
    :return: list of numbers converted to list of strings.
    """

    while True:
        number_list_len = input_to_int('Enter a count of list of numbers: ')

        if number_list_len == 0:
            print('Wrong value, try again!')
            continue
        else:
            break

    list_numbers = list_in_range(number_list_len)

    list_str_numbers = list(map(lambda x: str(x), list_numbers))

    for __iter__, str_number in enumerate(list_str_numbers):
        print(type(list_str_numbers[__iter__]))


@decorator_pursuance_time
def task_3(tusk_num: int):
    """
    This def to complete Task 1.
    :param tusk_num: number of task
    :return: tuple of palindrome strings.
    """

    while True:
        number_list_len = input_to_int('Enter a count of list of numbers: ')

        if number_list_len == 0:
            print('Wrong value, try again!')
            continue
        else:
            break

    tuple_str = tuple(
        input(f'Enter string № {i + 1}: ')
        for i, word in enumerate(range(number_list_len))
    )

    tuple_str = tuple(filter(filter_palindrome, tuple_str))
    print(f'Tuple of palindromes: {tuple_str}')


@decorator_pursuance_time
def task_5(tusk_num: int):
    """
    :param tusk_num: number of task
    :return: Type entered value
    """

    int_float = input_to_int_or_float('Enter some number: \n')

    if int_float < 0 and type(int_float) == float:
        print(f'You entered negative float value: {int_float}')

    elif int_float > 0 and type(int_float) == float:
        print(f'You entered positive float value: {int_float}')

    elif int_float < 0 and type(int_float) == int:
        print(f'You entered negative integer value: {int_float}')

    else:
        print(f'You entered positive integer value: {int_float}')


def main():
    """
    Main def
    """

    while True:
        task_check = input(
            f'What task of [1, 2, 3, 5] do you want to check?'
            f'\n<Enter>/q/Q/quit/QUIT/exit/EXIT to stop the program!\n')
        match task_check:
            case '1':
                task_1(1)
                break
            case '2':
                task_2(2)
                break
            case '3':
                task_3(3)
                break
            case '5':
                task_5(5)
                break
            case 'q' | 'quit' | 'exit' | 'Q' | 'QUIT' | 'EXIT' | '':
                print('EXIT')
                break
            case _:
                print(f'There is no task number '
                      f'or incorrect value of "{task_check}"! Try again!')
                continue


main()
