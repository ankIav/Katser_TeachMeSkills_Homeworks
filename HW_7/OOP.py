"""This module contains objects and methods of classes"""

from classes import *

# create 2 trucks in list
trucks_list = [
    Truck('kamaz', '6460', 10, 20),
    Truck('man', 'tgx', 4, 30)
]

# set some optional attributes to our trucks
trucks_list[0].set_color('Blue')
trucks_list[0].set_weight(14)
trucks_list[1].set_color('grey')

# using every method
for truck in trucks_list:
    # using methods of class
    truck.get_info()
    truck.load()
    truck.move()
    truck.stop()
