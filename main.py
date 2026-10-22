from random import randrange

prt1 = True
count = 1
r_min = 1
r_max = 10
awns = randrange(r_min, r_max + 1)

while prt1:
    try:
        r = input('Want to play with standard range 1 - 10? [y/n]: ')

        awns = randrange(r_min, r_max + 1)
        if r.lower() == 'n':
            r_min = int(input('Enter a min range number: '))
            r_max = int(input('Enter a max range number: '))
        elif r.lower() == 'y':
            prt1 = False
        else:
            print('\n----- please enter only y/n -----\n')
            continue

    except ValueError:
        print('Please enter a number!')
        continue

while True:
    try:
        # ask user to input a guess
        print(f'Guess a number between {r_min} - {r_max}: [Try {count}]')
        print(50 * '#')
        print()
        guess = int(input('Enter a Number: '))

        if guess == awns:
            print(50 * '#')
            print(f'\nYou\'re right. Number {guess} is the right answer!')
            print(f'\nIt took you {count} tries.\n')
            print(50 * '#')
            break
        else:
            print('That\'s wrong! Try again...')
            print()
            count += 1
        continue
    except ValueError:
        print('\nPlease enter only Numbers!\n')
        continue



