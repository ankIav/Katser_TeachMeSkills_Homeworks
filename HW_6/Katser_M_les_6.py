"""This module completes homework of the 6 lesson"""
# TODO: pip install openpyxl

import json
import csv
from openpyxl.workbook import Workbook
import random


def file_write_txt_task_2(open_mode: str, *args: list):
    """
    Creating of updating Katser_M_less_6_Task_2.txt file.
    :param open_mode: file_mode in open()
    :param args: tuple of args, meanwhile lists
    :return: Katser_M_less_6_Task_2.txt.
    """

    with open(
            r'output_files/Katser_M_less_6_Task_2.txt',
            open_mode) as file:
        for arg in args:
            file.write('\n'.join(arg))
        # after every list creating new line
        file.write('\n')


def task_1():
    """
    This def to complete Task 1.
    :return: decoding to utf-8 and coding to latin 1. Printing outputs.
    """

    code_byte_str = b'r\xc3\xa9sum\xc3\xa9'

    decode_utf_str_1 = code_byte_str.decode('utf-8')
    print(decode_utf_str_1)

    code_latin1_str = decode_utf_str_1.encode('latin-1')
    print(code_latin1_str)

    decode_utf_str_2 = code_latin1_str.decode('iso-8859-1')
    print(decode_utf_str_2)


def task_2():
    """
    This def to complete Task 2.
    :return: Create and add strings to txt file.
    """

    strings = [input(f'Enter some string # {i + 1}: ') for i in range(4)]

    file_write_txt_task_2('w', strings[:2])
    file_write_txt_task_2('a', strings[2:])


def task_3():
    """
    This def to complete Task 3.
    :return: Create a JSON file.
    """

    # A first easy try - perfect form of data to json
    # list_dicts_data = [
    #     {'id': 111111, 'name': 'Anna', 'age': 25},
    #     {'id': 222222, 'name': 'Kenny', 'age': 18},
    #     {'id': 333333, 'name': 'Ben', 'age': 60},
    #     {'id': 444444, 'name': 'Emma', 'age': 32},
    #     {'id': 555555, 'name': 'Alex', 'age': 27},
    #     {'id': 666666, 'name': 'Mark', 'age': 33},
    # ]

    dict_data = {
        111111: ('Anna', 25),
        222222: ('Kenny', 18),
        333333: ('Ben', 60),
        444444: ('Emma', 32),
        555555: ('Alex', 27),
        666666: ('Mark', 33)
    }
    with open(
            'output_files/Katser_M_less_6_Task_3.json',
            'w') as file:
        json.dump(dict_data, file)


def task_4():
    """
    This def to complete Task 4
    :return: CSV file from JSON with new column 'phone'
    """

    with open(
            'output_files/Katser_M_less_6_Task_3.json') as json_file:
        jsondata = json.load(json_file)

        list_dicts_data = []
        dict_person = {}

        for key, value in jsondata.items():
            # one dict = one person with id, name, age fields
            dict_person['id'] = key
            dict_person['name'] = value[0]
            dict_person['age'] = value[1]

            list_dicts_data.append(dict_person.copy())  # copy must have

        jsondata = list_dicts_data

    # adding new field 'phone' into CSV file to every person
    with open(
            'output_files/Katser_M_less_6_Task_4.csv',
            'w') as csv_file:
        for person in jsondata:
            person['phone'] = (
                f'+375({random.choice([29, 33, 44])})'
                f'{random.randint(1000000, 9999999)}'
            )

        # header name is keys of list jsondata[0].
        wr = csv.DictWriter(csv_file, fieldnames=jsondata[0].keys())
        wr.writeheader()  # naming header method.
        wr.writerows(jsondata)  # fill data of dicts


def task_5():
    """
    This def to complete Task 5
    :return: XLSX file from CSV without a row 'phone'
    """

    wb = Workbook()
    ws = wb.active

    # reading CSV file filling our Workbook
    with open(
            'output_files/Katser_M_less_6_Task_4.csv',
            'r') as csv_file:
        csv_data = [row for row in csv.reader(csv_file)]
        # creating first row(header) in XLSX file with empty first column.
        row_xlsx = [f'Person {i + 1}' for i in range(len(csv_data) - 1)]
        row_xlsx.insert(0, '')

        ws.append(row_xlsx)

        index_row = 0  #
        list_rows_xlsx = []
        # column from CSV is a row in our XLSX.
        for index_row in range(len(csv_data[index_row])):
            # run index in a column from CSV without Transpose
            for index_column in range(len(csv_data)):
                # run index a row from CSV without Transpose
                list_rows_xlsx.append(csv_data[index_column][index_row])
                # increment to another row from CSV without Transpose
                index_column += 1

            # increment to another column from CSV without Transpose
            index_row += 1

            # we don't need an AGE row in our XLSX file
            ws.append(list_rows_xlsx) if 'age' not in list_rows_xlsx else 0

            # clear the list after appending into XLSX before next appending
            list_rows_xlsx.clear()

    # save and close XLSX file
    wb.save('output_files/Katser_M_less_6_Task_5.xlsx')
    wb.close()


task_1()
task_2()
task_3()
task_4()
task_5()
