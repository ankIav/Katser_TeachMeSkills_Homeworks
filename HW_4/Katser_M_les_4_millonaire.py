""""
Millionaire the game
"""

iter_step = -1
loop_flag = 0
step_money = {0: 0, 1: 10, 2: 50, 4: 100, 5: 250, 6: 500,
              7: 1000, 8: 2500, 9: 5000, 10: 10000, 11: 25000,
              12: 50000, 13: 100000, 14: 250000, 15: 500000, 16: 1000000}

while iter_step == -1:
    play_or_not = input('Enter "start" to start the game!'.center(79) + '\n'
                        + 'Enter q/quit/ to finish game!'.center(79) + '\n'
                        + 'Enter start/s/ to play!'.center(79) + '\n'
                        + '-' * 79 + '\n')

    if play_or_not.lower() == 'q' or play_or_not == 'quit':
        while loop_flag == 0:
            play_or_not = input(
                'Are you sure you want to exit? (y/n)'.center(79) + '\n')

            if play_or_not.lower() == 'y':
                break
            elif play_or_not.lower() == 'n':
                break

        continue
    elif play_or_not.lower() == 'start' or play_or_not.lower() == 's':
        iter_step += 1

print(iter_step)
