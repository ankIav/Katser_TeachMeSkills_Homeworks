"""This module of classes of geometry"""

import math


class Point(object):
    """Parent class"""

    def __init__(self, x: int, y: int):
        """Initializing attributes coordinates x, y and parameter radius"""

        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """:return: string info about object"""

        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

    def __str__(self) -> str:
        """:return: readable string info about object"""

        return (
            f'Object of class {self.__class__.__name__} '
            f'with attributes: x = {self.x}, y = {self.y}'
        )

    def __lt__(self, other) -> bool:
        """
        :param: self = first obj, other = next obj
        :return: True if square first obj < square second obj.
        """

        return self._square() < other._square()

    def __le__(self, other) -> bool:
        """
        :param: self = first obj, other = next obj
        :return: True if square first obj. <= square second obj.
        """

        return self._square() <= other._square()

    def __eq__(self, other) -> bool:
        """
        :param: self = first obj, other = next obj
        :return: True if coordinates first obj == coordinates second obj.
        """

        return self.x == other.x and self.y == other.y

    def __ne__(self, other) -> bool:
        """
        :param: self = first obj, other = next obj
        :return: True if coordinates first obj != coordinates second obj.
        """

        return self.x != other.x or self.y != other.y

    def __ge__(self, other) -> bool:
        """
        :param: self = first obj, other = next obj
        :return: True if square first obj >= square second obj.
        """

        return self._square() >= other._square()

    def __gt__(self, other) -> bool:
        """
        :param: self = first obj, other = next obj
        :return: True if square first obj. > square second obj.
        """

        return self._square() > other._square()

    def distance_from_origin(self) -> float:
        """:return: value if distance from origin to point"""

        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def _square(self) -> int:
        """Square of rectangle"""

        return abs(self.x * self.y)


class Circle(Point):
    """Inheritance-class from Point"""

    def __init__(self, x: int, y: int, radius: float):
        """Initialize attributes of parent class Point"""

        super().__init__(x, y)
        self.radius = radius

    def __repr__(self) -> str:
        """:return: string info about object"""

        return (
            f'{self.__class__.__name__}'
            f'(x={self.x}, y={self.y}, radius={self.radius})')

    def __str__(self):
        """:return: readable string info about object"""

        return (
            f'Object of class {self.__class__.__name__} '
            f'with attributes: x = {self.x}, '
            f'y = {self.y}, '
            f'radius = {self.radius}'
        )

    def __lt__(self, other) -> bool:
        """
        :param: self = first obj, other = next obj
        :return: True if circumference first obj. < circumference second obj.
        """

        return self.circumference() < other.circumference()

    def __le__(self, other) -> bool:
        """
        :param: self = first obj, other = next obj
        :return: True if circumference first obj. <= circumference second obj.
        """

        return self.circumference() <= other.circumference()

    def __eq__(self, other) -> bool:
        """
        :param: other: WHAT IS THIS????
        :return: true if first obj attr = second obj attr.
        """

        return (
            self.x == other.x
            and self.y == other.y
            and self.radius == other.radius
        )

    def __ne__(self, other) -> bool:
        """
        :param: self = first obj, other = next obj
        :return: True if first obj attr. != second obj attr.
        """

        return (
            self.x != other.x
            or self.y != other.y
            or self.radius != other.radius
        )

    def __ge__(self, other) -> bool:
        """
        :param: self = first obj, other = next obj
        :return: True if circumference first obj. >= circumference second obj.
        """

        return self.circumference() >= other.circumference()

    def __gt__(self, other) -> bool:
        """
        :param: self = first obj, other = next obj
        :return: True if circumference first obj. > circumference second obj.
        """

        return self.circumference() > other.circumference()

    def edge_distance_from_origin(self) -> float:
        """:return: value of edge distance from origin????"""

        return abs(Circle.distance_from_origin(self) - self.radius)

    def area(self) -> float:
        """:return: area of circle"""

        return math.pi * (self.radius ** 2)

    def circumference(self) -> float:
        """:return: value of circumference"""

        return 2 * math.pi * self.radius

    def sub_circles(self, other) -> float | Point:
        """
        method for subtracting the radii of circles
        :param other: another circle
        :return: radius difference value or object class Point.
        """

        return (
            abs(self.radius - other.radius) if self.radius != other.radius
            else Point(self.x - other.x, self.y - other.y)
        )
