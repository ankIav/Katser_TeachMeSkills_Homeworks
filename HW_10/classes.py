"""Module about Calculator class"""

import math


# main operators in calculator
operators = {
    'plus': '+',
    'minus': '-',
    'multiply': '*',
    'division': '/',
    'equal': '=',
}


class WrongFormat(Exception):
    """Creating own exception errors
    """
    pass


class Calculator:
    """The main class, which will calculate an expression
    """

    result = 0

    @staticmethod
    def str_to_list(string: str) -> list:
        """
        :param string: get string
        :return: reformat into useful list
        """
        # separate operation symbols with whitespace
        for op in operators.values():
            if op in string:
                string = string.replace(op, f' {op} ')

        # turning string numbers and operators into elements of list
        string = string.split()
        # Getting a first negative and another nums into really negative nums.
        for i, el in enumerate(string):
            while (
                    string[i] == '-'
                    and string[i - 1] in operators.values()
                    or (string[i] == '-' and i == 0)
            ):
                string[i + 1] = f'-{string[i + 1]}'
                del string[i]  # after transport minus to num delete this el.

        return string  # string now is list ['num', '+', '-num'...] format

    @staticmethod
    def str_to_int_float(args):
        """
        :param args:
        :return:
        """
        list_return = []
        for element in args:
            try:
                element = int(element)
                list_return.append(element)
            except ValueError:
                try:
                    element = float(element)
                    list_return.append(element)
                except ValueError:
                    list_return.append(element)
            continue

        return list_return

    def __init__(self, expression: str):
        """Initializing attribute expression
        """
        self.expression = self.str_to_list(expression)

    def __repr__(self) -> str:
        """:return: string info about the obj.
        """
        return f'{__class__.__name__}(Expression: {str(self)})'

    def __str__(self) -> str:
        """:return: readable ifo about the obj.
        """
        expression = self.str_to_int_float(self.expression)
        for i, el in enumerate(expression):
            try:
                while (
                    expression[i] < 0
                    and expression[i - 1] in operators.values()
                ):
                    expression[i + 1] = f'{str(expression[i + 1])}'
                    del expression[i]
            except Exception:
                continue

        return ' '.join(map(str, self.expression))

    def _plus(self):
        """
        :return:
        """
        expression = self.str_to_int_float(self.expression)
        for num in expression:
            while num not in operators.values():
                self.result += num
                break
        return self.result
