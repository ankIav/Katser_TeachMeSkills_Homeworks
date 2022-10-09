"""This module contains objects and methods of classes"""

from classes import Truck, Car


# create 2 trucks in list
trucks_list = [
    Truck('kamaz', '6460', 10, 20),
    Truck('man', 'tgx', 4, 30)
]

# set some optional attributes to our trucks
trucks_list[0].set_color('Blue')
trucks_list[0].set_weight(14)
trucks_list[1].set_color('grey')

# use every method
for truck in trucks_list:
    truck.get_info()
    truck.load()
    truck.move()
    truck.stop()

# create 2 cars in list
cars_list = [
    Car('mercedes', 'benz', 6, 250),
    Car('lada', 'kalina', 14, 200)
]

# set some optional attributes to our cars
cars_list[1].set_weight(3)
cars_list[1].birthday()  # increment age of car lada

# use every method
for car in cars_list:
    car.get_info()
    car.move()
    car.stop()
