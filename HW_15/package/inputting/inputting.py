"""This module is simple def to return INT value without errors
"""


# This is simple def to return INT value without errors
def inting(msg='', var='') -> int:
    """
    :param msg: str message before inputting
    :param var: str name of var
    :return: int value
    """

    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(f'Wrong int format {var}, Try again!')
            continue


# This is simple def to return FLOAT value without errors
def floating(msg='', var='') -> float:
    """
    :param msg: str message before inputting
    :param var: str name of var
    :return: float value
    """

    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(f'Wrong int format {var} variable, Try again!')
            continue
