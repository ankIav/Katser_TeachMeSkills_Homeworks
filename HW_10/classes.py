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


class Calculator:
    """The main class, which will calculate an expression"""

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
            if (
                    string[i] == '-'
                    and string[i - 1] in operators.values()
                    or (string[i] == '-' and i == 0)
            ):
                string[i + 1] = f'-{string[i + 1]}'
                del string[i]  # after transport minus to num delete this el.

        return string  # string now is list ['num', '+', '-num'...] format

    def __init__(self, expression: str):
        """Initializing attribute expression
        """
        self.expression = self.str_to_list(expression)

    def __repr__(self) -> str:
        """:return: string info about the obj.
        """
        return f'{__class__.__name__}(Expression: {" ".join(self.expression)})'

    def __str__(self) -> str:
        """:return: readable ifo about the obj.
        """
        return " ".join(self.expression)

    def _plus(self):
        """

        :return:
        """
        for num in self.expression:
            if num not in operators.values():
                num = float(num)
                self.result += num

        return self.result
