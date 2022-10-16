"""Module about Calculator class"""


# main operators in calculator
operators = {
    'plus': '+',
    'minus': '-',
    'multiply': '*',
    'division': '/',
}


class WrongFormat(Exception):
    """Exceprion raised for wrong format inputted.
    """
    def __init__(self, element='', message='Wrong format inputted values'):
        self.element = element
        self.message = message
        super().__init__(self.element)
        super().__init__(self.message)

    def __str__(self):
        return f'{self.element} -> {self.message}'


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
                    (string[i] == '-' and string[i - 1] in operators.values())
                    or (string[i] == '-' and i == 0)
            ):
                string[i + 1] = f'-{string[i + 1]}'
                del string[i]  # after transport minus to num delete this el.

            while (
                    (string[i] == '+' and string[i - 1] in operators.values())
                    or (string[i] == '+' and i == 0)
            ):
                string[i + 1] = f'{string[i + 1]}'
                del string[i]  # after transport minus to num delete this el.
            # Replacing .num and -.num into 0.num and -0.num
            while (
                    '-.' in string[i]
                    and string[i].find('-.') == 0
            ):
                string[i] = string[i].replace('-.', '-0.')
            while (
                    '.' in string[i]
                    and string[i].find('.') == 0
            ):
                string[i] = string[i].replace('.', '0.')

        # checking for simple errors.
        if len(string) == 0:
            raise WrongFormat('', 'Empty expression')
        elif len(string) == 1 and (string[0] == '0.' or string[0] == '-0.'):
            raise WrongFormat(string[0])

        return string

    @staticmethod
    def str_to_int_float(args):
        """
        :param args:
        :return:
        """
        list_return = []
        for i in args:
            try:
                i = int(i)
                list_return.append(i)
            except ValueError:
                try:
                    i = float(i)
                    list_return.append(i)
                except ValueError:
                    if i in operators.values():
                        list_return.append(i)
                    else:
                        raise WrongFormat(i, 'Wrong inputted value')
            continue

        # one more check for errors in start/end or raw in string.
        for i in range(len(list_return)):
            while (
                list_return[0] in operators.values()
                or list_return[-1] in operators.values()
                or (
                    list_return[i] in operators.values()
                    and list_return[i+1] in operators.values()
                )
            ):
                raise WrongFormat(list_return[i], "Wrong format!")


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

        return ' '.join(map(str, expression))

    #     return f'{str(self)} = {self.result}'

    @staticmethod
    def __uh(expression, i):
        del expression[i], expression[i]
        expression.insert(0, 'del')
        expression.insert(0, 'del')

    def calculate(self):
        """
        :return:
        """

        expression = self.str_to_int_float(self.expression)
        count_add = 0

        for i in range(len(expression)):
            while expression[i] == '/':
                expression[i - 1] /= expression[i + 1]
                self.__uh(expression, i)
                count_add += 2
                break

        for i in range(len(expression)):
            while expression[i] == '*':
                expression[i - 1] *= expression[i + 1]
                self.__uh(expression, i)
                count_add += 2
                break

        for i in range(len(expression)):
            while expression[i] == '-':
                expression[i - 1] -= expression[i + 1]
                self.__uh(expression, i)
                count_add += 2
                break

        for i in range(len(expression)):
            while expression[i] == '+':
                expression[i - 1] += expression[i + 1]
                self.__uh(expression, i)
                count_add += 2
                break

        return f'{str(self)} = {expression[-1]}'
        #
        # return f'{expression} = {count_add}\ncalculate = {expression[-1]}'
