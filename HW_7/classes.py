"""This module of classes"""

import time


class Auto:
    """Simple model of parent class Auto"""

    def __init__(self, brand: str, mark: str, age: int):
        """Initialize attributes of auto"""

        self.brand = brand.strip().upper()
        self.mark = mark.strip().upper()
        self.age = age
        self.weight = None
        self.color = None
        self._auto_info = {}

    def set_color(self, color: str):
        """Initialize attribute color"""

        self.color = color.strip().title()

    def set_weight(self, weight: float):
        """Initialize attribute weight"""

        self.weight = weight

    def get_info(self):
        """Printing full info about auto"""

        # self._auto_info = {
        #     'Brand': self.brand,
        #     'Mark': self.mark,
        #     'Age': f'{self.age} years',
        # }
        self._auto_info['Brand'] = self.brand
        self._auto_info['Mark'] = self.mark
        self._auto_info['Age'] = self.age

        if self.color is not None and self.weight is not None:
            self._auto_info['Color'] = self.color
            self._auto_info['Weight'] = f'{self.weight} tonn'
        elif self.color is not None and self.weight is None:
            self._auto_info['Color'] = self.color
        elif self.color is None and self.weight is not None:
            self._auto_info['Weight'] = f'{self.weight} tonn'

        print(f'Full {self.__class__.__name__} info:')

        for key, value in self._auto_info.items():
            print(f'\t{key} is {value}')

    def move(self):
        """Start moving"""

        print(f'Move {self.brand} {self.mark}')

    def stop(self):
        """Stop moving"""

        print(f'Stop {self.brand} {self.mark}\n{"-"*20}')

    def birthday(self):
        """Increment age"""

        self.age += 1


class Truck(Auto):
    """Inheritance-class from Auto"""

    def __init__(self, brand: str, mark: str, age: int, max_load: int):
        """Initialize attributes of parent class Auto"""

        super().__init__(brand, mark, age)
        self.max_load = max_load

    def get_info(self):
        """Redefine method of printing full info of auto"""

        self._auto_info['Max load'] = f'{self.max_load} tonn'
        super(Truck, self).get_info()

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

    def get_info(self):
        """Redefine method of printing full info of auto"""

        self._auto_info['Max load'] = f'{self.max_speed} km/h'
        super(Car, self).get_info()

    def move(self):
        """Redefine method of moving from parent class Auto"""

        super(Car, self).move()
        print(f'Max speed is {self.max_speed} km/h')
