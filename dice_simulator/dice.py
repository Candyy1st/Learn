import random

number = random.randint(1,6)

x = 'y' \

while x == 'y':
    if number == 1:
        print('_________')
        print('|       |')
        print('|   0   |')
        print('|       |')
        print('---------')

    if number == 2:
        print('_________')
        print('|       |')
        print('| 0   0 |')
        print('|       |')
        print('---------')

    if number == 3:
        print('_________')
        print('| 0     |')
        print('|   0   |')
        print('|     0 |')
        print('---------')

    if number == 4:
        print('_________')
        print('| 0   0 |')
        print('|       |')
        print('| 0   0 |')
        print('---------')

    if number == 5:
        print('_________')
        print('| 0   0 |')
        print('|   0   |')
        print('| 0   0 |')
        print('---------')

    if number == 6:
        print('_________')
        print('| 0   0 |')
        print('| 0   0 |')
        print('| 0   0 |')
        print('---------')

    x = input('Press y to roll again : ')