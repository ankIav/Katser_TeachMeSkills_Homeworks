"""
This module completes homework of the 4 lesson
TODO: just run this code, in this program realized choice of task to start
    in def main()
"""

import time


def print_task(task_num: int):
    """
    :param task_num: get task number to print it
    :return: None, just print formatted task
    """
    print('-' * 79 + '\n' + f'Task {task_num}'.center(79))
    dict_tasks = {1: 'Дан словарь, создать новый словарь, поменяв местами'
                     'ключ и значение.' + '\n' + '-' * 79,
                  2: 'Написать программу для нахождения факториала. Факториал '
                     'натурального числа n\nопределяется как произведение '
                     'всех натуральных чисел от 1 до n включительно.\n'
                     'Реализацию выполнить в виде рекурсивной функции.'
                     + '\n' + '-' * 79,
                  3: '*Дан список чисел. Посчитать сколько раз встречается '
                     'каждое число.\nИспользовать для подсчета функцию.'
                     + '\n' + '-' * 79,
                  4: '*Сделать функцию, которая будет вызываться из '
                     'генератора списков и по запросу\nк ней отдавать текущее '
                     'время с задержкой в 1 сек. Количество элементов нового\n'
                     'списка n запрашивать у пользователя.' + '\n' + '-' * 79,
                  }

    for key, value in dict_tasks.items():
        if task_num == key:
            print(value)


def check_naturalis(message: str) -> int:
    """
    This definition is used to correct input of whole numbers
    :param message: get string to print due message
    :return: whole number.
    """
    while True:
        int_naturalis = input(message)

        if not int_naturalis.isdigit():
            print('Wrong value, try again!')
            continue
        else:
            int_naturalis = int(int_naturalis)
            break

    return int_naturalis


def check_int_float(message: str) -> int or float:
    """
    This definition is used to correct input of integer or float numbers
    :param message: get string to print due message
    :return:integer or float value.
    """
    while True:
        int_float = input(message)

        if '-' in int_float and '.' in int_float and \
                int_float.replace('-', '').replace('.', '').isdigit():
            int_float = float(int_float)
            break
        elif '.' in int_float and int_float.replace('.', '').isdigit():
            int_float = float(int_float)
            break
        elif '-' in int_float and int_float.replace('-', '').isdigit():
            int_float = int(int_float)
            break
        elif int_float.isdigit():
            int_float = int(int_float)
            break
        else:
            print('Wrong value, try again!')
            continue

    return int_float


def dict_swap_keys_values(func_dict) -> dict:
    """
    This def for Task 1
    :param func_dict: a main dictionary
    :return: a new dict where key amd values will swap from a main dict.
    """

    swapped_dict = {}

    for key, value in func_dict.items():
        swapped_dict[value] = key

    return swapped_dict


def dict_keys_counter(list_numbers: list) -> dict:
    """
    creating a dict where key is element of list, value of element counter
    :param list_numbers: get list of values to convert them into keys of dict
    :return: dict where key is element of list, value amount of this element.
    """
    dict_keys_amount = {}

    for number in list_numbers:
        dict_keys_amount[number] = dict_keys_amount.setdefault(number, 0) + 1

    return dict_keys_amount


def list_in_range(len_list: int) -> list:
    """
    Creating a list of elements from a keyboard with length of list
    :param len_list: length of list
    :return: a list of elements from a keyboard.
    """

    list_elements = [
        check_int_float(f'Enter the {__iter__ + 1} element: ')
        for __iter__ in range(len_list)
    ]

    return list_elements


def find_factorial(int_number: int) -> int:
    """
    Find factorial
    :return: factorial
    """
    if int_number == 0:
        return 1
    if int_number == 1:
        return int_number
    else:
        return int_number * find_factorial(int_number - 1)


def list_datetime_delay() -> str:
    """
    :return: string %Y-%m-%d %H:%M:%S format with 1 sec delay.:
    """
    seconds = time.localtime().tm_sec - 1

    if 0 <= seconds < 10:
        seconds = '0' + str(seconds)
    elif seconds == -1:
        seconds = '59'

    datetime_string = time.strftime(
        f'%Y-%m-%d %H:%M:{seconds}', time.localtime()
    )
    time.sleep(1)
    return datetime_string


def task_1():
    """
    This def to complete task 1
    :return: swapped dict
    """
    print_task(1)
    dict_given = {1: 'one',
                  2: 'two',
                  3: 'three', }

    new_dict = dict_swap_keys_values(dict_given)
    print(f'Original:\n{dict_given}\nResult:\n{new_dict}')


def task_2():
    """
    This def to compete Task 2
    :return: factorial N
    """
    print_task(2)

    naturalis_n = check_naturalis('Enter the N to find factorial of N: ')

    factorial_n = find_factorial(naturalis_n)
    print(f'Factorial N (n!) = {factorial_n}')


def task_3():
    """
     This def to compete Task 3
    :return: count of repeats in list of numbers.
    """
    print_task(3)
    while True:
        number_list_len = check_naturalis('Enter a count of list of numbers: ')

        if number_list_len == 0:
            print('Wrong value, try again!')
            continue
        else:
            break

    list_numbers = list_in_range(number_list_len)
    dict_numbers = dict_keys_counter(list_numbers)

    for key, value in dict_numbers.items():
        print(f'Count of element {key} repetitions = {value}')


def task_4():
    """
    :return: list of dates and times with delay of 1 sec.
    """
    print_task(4)
    while True:
        n = check_naturalis('Enter n: ')
        if n == 0:
            print('Wrong value, try again!')
            continue
        else:
            break
    list_datetime = [list_datetime_delay() for __iter__ in range(n)]
    print(list_datetime)


def main():
    """
    Main def
    """
    while True:
        task_check = input(
            f'What task of {list(range(1, 5))} do you want to check?'
            f'\n<Enter>/q/Q/quit/QUIT/exit/EXIT to stop the program!\n')
        match task_check:
            case '1':
                task_1()
                break
            case '2':
                task_2()
                break
            case '3':
                task_3()
                break
            case '4':
                task_4()
                break
            case 'q' | 'quit' | 'exit' | 'Q' | 'QUIT' | 'EXIT' | '':
                print('EXIT')
                break
            case _:
                print(f'There is no task number '
                      f'or incorrect value of "{task_check}"! Try again!')
                continue


main()
