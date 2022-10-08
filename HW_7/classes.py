"""This module of classes"""

import time


class Auto:
    """Simple model of parent class Auto"""

    def __init__(self, brand: str, mark: str, age: int):
        """Initialize attributes of auto"""

        self.brand = brand.upper()
        self.mark = mark.title()
        self.age = age
        self.weight = None
        self.color = None

    def get_color(self, color: str):
        """Initialize attribute color"""

        self.color = color.title()

    def get_weight(self, weight: float):
        """Initialize attribute weight"""

        self.weight = weight

    def move(self):
        """Start moving"""

        print(f'Move {self.brand} {self.mark}')

    def stop(self):
        """Stop moving"""

        print(f'Stop {self.brand} {self.mark}')

    def birthday(self):
        """Increment age"""

        self.age += 1


class Truck(Auto):
    """Inheritance-class from Auto"""

    def __init__(self, brand: str, mark: str, age: int, max_load: int):
        """Initialize attributes of parent class Auto"""

        super().__init__(brand, mark, age)
        self.max_load = max_load

    def move(self):
        """Redefine method of moving from parent class Auto"""

        print('Attention')
        super(Truck, self).move()

    def load(self):
        """Loading a burden with some time"""

        print('Waiting for loading...')
        time.sleep(1)
        print(f'Load {self.brand} {self.mark}')
        time.sleep(1)


class Car(Auto):
    """Inheritance-class from Auto"""

    def __init__(self, brand: str, mark: str, age: int, max_speed: int):
        """Initialize attributes of parent class Auto"""

        super().__init__(brand, mark, age)
        self.max_speed = max_speed

    def move(self):
        """Redefine method of moving from parent class Auto"""

        super(Car, self).move()
        print(f'Max speed is {self.max_speed} km/h')
