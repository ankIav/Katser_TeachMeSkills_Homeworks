"""Description of class Geometry Progression (next GP)
"""


def decorator_check(method):
    """
    Check count elements of GP
    :return:
    """

    def wrapper(self):
        if self.count == 0:
            return f'Count of Your geometric progression = 0!'

        return method(self)

    return wrapper


class GeometricProgression:
    """

    """

    def __init__(self, start=1, q=1, count=1, num=1):
        """
        Initializing attributes of class.
        :param start: start of GP
        :param q: factor GP
        :param count: count of elements of GP.
        """
        self.start = start
        self.q = q
        self.count = count
        self.num = num

    def __str__(self):
        """
        :return: formatted info of object
        """
        return (
            f'start = {self.start}, factor = {self.q}, count = {self.count}'
        )

    @staticmethod
    def __sum(start, q, count) -> int | float:
        """
        a hidden recursion func to count sum of GP
        :param start: first element of GP
        :param q: factor
        :param count: count of set of GP
        :return: sum of GP.
        """
        # exit recursion
        if count == 1:
            return start

        return start + GeometricProgression.__sum(start * q, q, count - 1)

    @decorator_check
    def sum(self) -> int | float:
        """
        :return: Sum of PG
        """

        return self.__sum(self.start, self.q, self.count)

    @decorator_check
    def find_b(self) -> int | float | str:
        """
        :return: a(n) element of GP
        """
        if self.num > 0:
            return self.start * (self.q ** (self.num - 1))

    @staticmethod
    def __yield(start, q, count):
        """
        a hidden recursion func to count next el of GP
        :param start: first element of GP
        :param q: factor
        :param count: count of set of GP
        :return: next el of GP.
        """
        for i in range(count):
            yield start * q

    @decorator_check
    def get_list(self) -> list:
        """
        :return: Get full list of elements of GP into list
        """

        return [
            next(self.__yield(self.start, self.q ** i, self.count))
            for i in range(self.count)
        ]


prog = GeometricProgression(2, 3, 6, 0)

print(
    f'Sum of Geometry Progression {str(prog)}\n'
    f'S({prog.count}) = {prog.sum()}'
)
print(
    f'N-element of Geometry Progression {str(prog)}\n'
    f'b({prog.num}) = {prog.find_b()}'
)

print(prog.get_list())
