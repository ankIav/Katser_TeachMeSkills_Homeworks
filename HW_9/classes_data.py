"""This module compete Tasks HW 9"""

from dataclasses import dataclass
for data

@dataclass
class DataMetahuman:
    """
    Like Batman's database about all heroes
    """

    alter_ego: str
    age: int
    sex: str
    first_name: str
    last_name: str
    country: str
    abilities: list
    weaknesses: list


class Hero:
    """
    Class to show Hero info and way to win
    """

    def __init__(self, _metahuman):
        """Initialize attr"""

        self.metahuman = _metahuman

    def show_info(self):
        """Show full info"""
        print(
            f'Alter ego \t{self.metahuman.alter_ego.title()}\n'
            f'Full name {self.metahuman.first_name} {self.metahuman.last_name}'
            f'\nAbilities: {self.metahuman.abilities}\n'
            f'Weak: {self.metahuman.weaknesses}'
        )

    @classmethod
    def show_loyality(cls):
        """Show loyalty"""
        print(f'This Meta is a {cls.__name__}')


class Villian(Hero):
    """This class for villions"""

    @staticmethod
    def destroy_city():
        """Method to destroy city"""

        print(f'{__class__.__name__} will destroy the city!')


list_heroes = ['superman', 'wonder-woman']
list_villians = ['reverse flash']


list_meta_data = [superman, reverse_flash, wonder_woman]
list_meta = []

# Is metahuman hero or villian?
for meta in list_meta_data:

    if meta.alter_ego in list_heroes:
        meta = Hero(meta)
        list_meta.append(meta)
    elif meta.alter_ego in list_villians:
        meta = Villian(meta)
        list_meta.append(meta)


# show info and loyalty
for data in list_meta:
    #
    if data.__class__.__name__ == 'Villian':
        data.show_info()
        data.show_loyality()
        Villian.destroy_city()
    else:
        data.show_info()
        data.show_loyality()