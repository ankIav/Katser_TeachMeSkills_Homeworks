from random import randint

# region Task 1

print('-----------------Task 1-----------------')

while True:  # Input cycle with checking of correct inputting of 2 words
    string_two_words = input('Input 2 words: ')

    if len(string_two_words.split()) == 2:
        break
    else:
        print('You have not entered two(2) words, try again!')

print('Inputted string: {var}'.format(var=string_two_words))

# TODO: Uncomment the next block of code to see alternative solution
# first_word, second_word = string_two_words.split()
# new_string = second_word + ' ! ' + first_word
#
# print(f'Final result: {new_string.center(len(new_string) + 2, "!")}')

new_string = ''
# FOR loop can be used for more words to flip the sentence.
for word in string_two_words.split()[::-1]:
    new_string += word + ' ! '

new_string = new_string.strip()[:-2]
new_string = new_string.center(len(new_string) + 2, "!")

print(f'Final result: {new_string}')
# endregion

# region Task 2
print('-----------------Task 2-----------------')

name_age_dict = {}
name = input('Enter your name: ')
age = 0

while name:  # cycle for correct input integer AGE
    age = input('Enter your age: ')

    if not age.isdigit():
        print('Error, try again!')
        continue
    else:
        age = int(age)

        if age < 0:
            print('Age cannot be negative!')
            continue

        break

name_age_dict[name.title().strip()] = age

for key, value in name_age_dict.items():
    if value < 10:
        print(f'Hello, junior {key}!')
    elif 10 <= value <= 18:
        print(f'How are you doing, {key}?')
    elif 18 < value < 100:
        print(f'What do you wish, {key}?')
    else:
        print(f'{key}, you lie - nowadays you cannot live so much...')

# endregion

# region Task 3
# TODO: Input the next code instead of WHILE cycle:
#  the difference lies in the absence of BREAK, i.e. no exit condition.
'''
while name:  # cycle for correct input integer AGE
    age = input('Enter your age: ')

    if not age.isdigit():
        print('Error, try again!')
        continue
    else:
        age = int(age)

        if age < 0:
            print('Age cannot be negative!')
            continue
'''
# endregion

# region Task 4
print('-----------------Task 4 variant 1 FOR-----------------')

n = int(input('Input n: '))

sum_cubes = sum(i ** 3 for i in range(n + 1))

print(f'Sum of cubes from 1 to N = {sum_cubes}')
print('-----------------Task 4 variant 2 WHILE-----------------')

i = 1
sum_cubes = 0

while i <= n:
    cube = i ** 3
    sum_cubes += cube
    i += 1

print(f'Sum of cubes from 1 to N = {sum_cubes}')
# endregion

# region Task 5
print('-----------------Task 5-----------------')

start_random, end_random = map(
    int, input('enter range of lucky number (through a space): ').split())
lucky_num = randint(start_random, end_random)

while True:
    hidden_num = int(input('Enter your number to get luck: '))

    if lucky_num > hidden_num:
        print('Mistake! Lucky number is bigger, try again!')
    elif lucky_num < hidden_num:
        print('Mistake! Lucky number is smaller, try again!')
    else:
        print('''-----------------------------
    !!!Congratulations!!!
      You have get luck
        ''')
        break
