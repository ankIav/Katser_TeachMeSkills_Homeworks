"""
This program completes homework tasks from lesson 2
var_N_M, where N - task number, M - variable number
"""

# region HOMEWORK LESSON 2, TASK 1: creating 3 variables with same data and id

print('HOMEWORK LESSON 2, TASK 1: creating 3 variables with same data and id')
var_1_1 = 2
var_1_2 = var_1_3 = var_1_1  # Initialisation of var_1_2 and var_1_3 which equals var_1_1

print(id(var_1_1), id(var_1_2), id(var_1_3), sep='    ')

print('True') if id(var_1_1) == id(var_1_2) and \
                 id(var_1_1) == id(var_1_3) and \
                 id(var_1_2) == id(var_1_3) else print('False')
# endregion

"""HOMEWORK LESSON 2, TASK 2: creating 2 variables with the same data and different id"""

print('HOMEWORK LESSON 2, TASK 2: creating 2 variables with the same data and different id')

var_2_1 = [1, 2]
var_2_2 = [1, 2]

print(id(var_2_1), id(var_2_2), sep='    ')

# ----------------------------------------------------------------------------------------------
#     HOMEWORK LESSON 2, TASK 3: changing variables in task 1 and 2
# ----------------------------------------------------------------------------------------------
print("""---------------------------------------------------------------
HOMEWORK LESSON 2, TASK 3_1: changing variables in task 1
---------------------------------------------------------------""")

var_1_2 = str(var_1_1)
var_1_3 = tuple(str(var_1_1))
print(id(var_1_1), id(var_1_2), id(var_1_3[0]))

print('True') if id(var_1_1) == id(var_1_2) and \
                 id(var_1_1) == id(var_1_3) and \
                 id(var_1_2) == id(var_1_3[0]) else print('False')

print('---------------------------------------------------------------\n'
      'HOMEWORK LESSON 2, TASK 3_2: changing variables in task 2\n'
      '---------------------------------------------------------------')

var_2_1 = bool(var_2_1)
var_2_2 = bool(var_2_2)
# TODO: я не совсем понял задание, но переменные теперь одного идентификатора
print(id(var_2_1), id(var_2_2))

# HOMEWORK LESSON 2, TASK 4:

main_string = input("Input something: ")
"""
[::2] means get chars id=0,2... and so on with step = 2 - this is logic to get ODD chars
[1::2] means get chars id=1,3... and so on with step = 2 - this is logic to get EVEN chars
"""
odd_string = main_string[::2]
even_string = main_string[1::2]

print(f'Inputted string is: "{main_string}"\n\n')
print(odd_string, even_string, '\n!!!', sep='     ')
