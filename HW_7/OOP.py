"""This module contains objects and methods of classes"""

from classes import Truck, Car
from classes_coordinates import Point, Circle


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

# Task 3
# creating some objects of classes Point and Circle

list_points = [
    Point(1, 1),
    Point(1, 2),
    Point(22, 16),
    Point(-1, -2)
]

list_circles = [
    Circle(1, 1, 1),
    Circle(1, 2, 3),
    Circle(2, 5, 15),
    Circle(-1, -2, 3)
]

# using all methods to Point objs
for i, point in enumerate(list_points):
    print(f'{"-"*20}Point #{i+1} methods{"-"*20}')
    print(str(point))
    print(repr(point))
    print(
        f'Distance point #{i+1} from origin = '
        f'{list_points[i].distance_from_origin()}'
    )

    # comparing elements each other
    print(f'{"="*10}Comparing elements each other{"="*10}')

    idx = list_points.index(point)
    dict_compares = {}
    tmp_dict_compares = {}

    """
    <
    """
    for j in range(len(list_points)):
        # skip comparing element to itself
        if idx == j:
            continue

        tmp_dict_compares[j] = (point < list_points[j])
        dict_compares[i] = tmp_dict_compares

    for key, value in dict_compares.items():
        print('<' * 40)
        for value_k, value_v in value.items():
            print(
                f'Is {point.__class__.__name__} #{key+1} < '
                f'{point.__class__.__name__} #{value_k+1}? '
                f'- {value_v}'
            )

    """
    <=
    """
    for j in range(len(list_points)):
        # skip comparing element to itself
        if idx == j:
            continue

        tmp_dict_compares[j] = (point <= list_points[j])
        dict_compares[i] = tmp_dict_compares

    for key, value in dict_compares.items():
        print('<=' * 20)
        for value_k, value_v in value.items():
            print(
                f'Is {point.__class__.__name__} #{key+1} <= '
                f'{point.__class__.__name__} #{value_k+1}? '
                f'- {value_v}'
            )

    """
    ==
    """
    for j in range(len(list_points)):
        # skip comparing element to itself
        if idx == j:
            continue

        tmp_dict_compares[j] = (point == list_points[j])
        dict_compares[i] = tmp_dict_compares

    for key, value in dict_compares.items():
        print('==' * 20)
        for value_k, value_v in value.items():
            print(
                f'Is {point.__class__.__name__} #{key+1} == '
                f'{point.__class__.__name__} #{value_k+1}? '
                f'- {value_v}'
            )

    """
    !=
    """
    for j in range(len(list_points)):
        # skip comparing element to itself
        if idx == j:
            continue

        tmp_dict_compares[j] = (point != list_points[j])
        dict_compares[i] = tmp_dict_compares

    for key, value in dict_compares.items():
        print('!=' * 20)
        for value_k, value_v in value.items():
            print(
                f'Is {point.__class__.__name__} #{key+1} != '
                f'{point.__class__.__name__} #{value_k+1}? '
                f'- {value_v}'
            )

    """
    >=
    """
    for j in range(len(list_points)):
        # skip comparing element to itself
        if idx == j:
            continue

        tmp_dict_compares[j] = (point >= list_points[j])
        dict_compares[i] = tmp_dict_compares

    for key, value in dict_compares.items():
        print('>=' * 20)
        for value_k, value_v in value.items():
            print(
                f'Is {point.__class__.__name__} #{key+1} >= '
                f'{point.__class__.__name__} #{value_k+1}? '
                f'- {value_v}'
            )

    """
    >
    """
    for j in range(len(list_points)):
        # skip comparing element to itself
        if idx == j:
            continue

        tmp_dict_compares[j] = (point > list_points[j])
        dict_compares[i] = tmp_dict_compares

    for key, value in dict_compares.items():
        print('>' * 40)
        for value_k, value_v in value.items():
            print(
                f'Is {point.__class__.__name__} #{key+1} > '
                f'{point.__class__.__name__} #{value_k+1}? '
                f'- {value_v}'
            )
