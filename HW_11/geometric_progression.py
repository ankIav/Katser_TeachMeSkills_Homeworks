"""This module count a Geometric Progression (next -> GP)
"""


from class_GP import GeometricProgression as gp


def is_int_float(message: str) -> int | float:
    """
    :param message: print due message
    :return: integer or float value.
    """

    while True:
        int_float = input(message)
        try:
            int_float = int(int_float)
        except ValueError:
            try:
                int_float = float(int_float)

            except ValueError as err:
                # Empty inputted value equal 1 as default
                if int_float == '':
                    return 1

                print(f'{err} Try inputting again!')
                continue
            else:
                return int_float
        else:
            return int_float


def naturalis(message: str) -> int:
    """
    :param message: print due message
    :return: int naturalis value
    """

    while True:
        natural = input(message)

        if natural == '':
            return 1

        try:
            natural = int(natural)

            if natural > 0:
                return natural
            else:
                print(f'Try inputting again only naturalis numbers!')
                continue

        except ValueError as err:
            print(f'{err} Try inputting again!')
            continue


"""
Creating a class object with parameters:
    b(1) - start element of GP
    q - factor GP
    c - count of elements GP
    n - N element of GP to find
Enter an empty value set it to default as 1.
"""

geometric_progression = gp(
    is_int_float('Enter b(1) - first element value of GP:\n'),
    is_int_float('Enter q - factor GP:\n'),
    naturalis('Enter c - count of elements GP:\n'),
    naturalis('Enter n - N element of GP to find:\n')
)

print(
    f'List of Geometry Progression {str(geometric_progression)}\n'
    f'\t{geometric_progression.get_list()}'
)

print(
    f'Sum of Geometry Progression {str(geometric_progression)}\n'
    f'\tS({geometric_progression.count}) = {geometric_progression.sum()}'
)
print(
    f'N - element of Geometry Progression {str(geometric_progression)}\n'
    f'\tb({geometric_progression.num}) = {geometric_progression.find_b()}'
)
