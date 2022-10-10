"""This module contains objects and methods of classes"""

from classes_auto import Truck, Car
from classes_coordinates import Point, Circle


def output_print(compare: str, name_cls: str):
    for key, value in dict_compares.items():
        print(compare * 40) if len(compare) == 1 else print(compare * 20)
        for value_k, value_v in value.items():
            print(
                f'Is {name_cls} #{key + 1} {compare} '
                f'{name_cls} #{value_k + 1}? '
                f'- {value_v}'
            )


def compare_lt(element: object, func_list: list, name_cls: str):
    """
    <
    """
    for j in range(len(func_list)):
        # skip comparing element to itself
        if idx == j:
            continue

        tmp_dict_compares[j] = (element < func_list[j])
        dict_compares[i] = tmp_dict_compares

    output_print('<', name_cls)


def compare_le(element: object, func_list: list, name_cls: str):
    """
    <=
    """
    for j in range(len(func_list)):
        # skip comparing element to itself
        if idx == j:
            continue

        tmp_dict_compares[j] = (element <= func_list[j])
        dict_compares[i] = tmp_dict_compares

    output_print('<=', name_cls)


def compare_eq(element: object, func_list: list, name_cls: str):
    """
    ==
    """
    for j in range(len(func_list)):
        # skip comparing element to itself
        if idx == j:
            continue

        tmp_dict_compares[j] = (element == func_list[j])
        dict_compares[i] = tmp_dict_compares

    output_print('=', name_cls)


def compare_ne(element: object, func_list: list, name_cls: str):
    """
    !=
    """
    for j in range(len(func_list)):
        # skip comparing element to itself
        if idx == j:
            continue

        tmp_dict_compares[j] = (element != func_list[j])
        dict_compares[i] = tmp_dict_compares

    output_print('!=', name_cls)


def compare_ge(element: object, func_list: list, name_cls: str):
    """
    >=
    """
    for j in range(len(func_list)):
        # skip comparing element to itself
        if idx == j:
            continue

        tmp_dict_compares[j] = (element >= func_list[j])
        dict_compares[i] = tmp_dict_compares

    output_print('>=', name_cls)


def compare_gt(element: object, func_list: list, name_cls: str):
    """
    >
    """
    for j in range(len(func_list)):
        # skip comparing element to itself
        if idx == j:
            continue

        tmp_dict_compares[j] = (element > func_list[j])
        dict_compares[i] = tmp_dict_compares

    output_print('>', name_cls)


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

list_points.append(list_circles[1].sub_circles(list_circles[3]))

for i, circle in enumerate(list_circles):
    print(f'{"-"*20}{circle.__class__.__name__} #{i+1} methods{"-"*20}')
    print(str(circle))
    print(repr(circle))
    print(f'Area = {circle.area()}')
    print(f'Circumference = {circle.circumference()}')
    print(f'Edge distance from origin = {circle.edge_distance_from_origin()}')

    # comparing elements each other
    print(f'{"="*10}Comparing elements each other{"="*10}')

    idx = list_circles.index(circle)
    dict_compares = {}
    tmp_dict_compares = {}

    compare_lt(circle, list_circles, circle.__class__.__name__)  # <
    compare_le(circle, list_circles, circle.__class__.__name__)  # <=
    compare_eq(circle, list_circles, circle.__class__.__name__)  # ==
    compare_ne(circle, list_circles, circle.__class__.__name__)  # !=
    compare_ge(circle, list_circles, circle.__class__.__name__)  # >=
    compare_gt(circle, list_circles, circle.__class__.__name__)  # >


# using all methods to Point objs
for i, point in enumerate(list_points):
    print(f'{"-"*20}{point.__class__.__name__} #{i+1} methods{"-"*20}')
    print(str(point))
    print(repr(point))
    print(f'Distance from origin = {point.distance_from_origin()}')

    # comparing elements each other
    print(f'{"="*10}Comparing elements each other{"="*10}')

    idx = list_points.index(point)
    dict_compares = {}
    tmp_dict_compares = {}

    compare_lt(point, list_points, point.__class__.__name__)  # <
    compare_le(point, list_points, point.__class__.__name__)  # <=
    compare_eq(point, list_points, point.__class__.__name__)  # ==
    compare_ne(point, list_points, point.__class__.__name__)  # !=
    compare_ge(point, list_points, point.__class__.__name__)  # >=
    compare_gt(point, list_points, point.__class__.__name__)  # >
