from random import randrange

lower_bound = 1
upper_bound= 10

def welcome_msg():
    print('Welcome to the guessing game.')
    print(f'Guess a number between {lower_bound} and {upper_bound}.')
    print()

def number_guess():
    while True:
        try:
            _guess = int(input('Input your guess: '))
            if lower_bound <= _guess <= upper_bound:
                return _guess
            else:
                print(f'Please enter a  valid number between {lower_bound} & {upper_bound}!')
        except ValueError:
            print('Please enter only a valid number!')

def create_rand_num():
    _awns = randrange(lower_bound, upper_bound+1)
    return _awns

def play_game():
    count = 1
    while True:
        print(awns)

        guess = number_guess()
        if guess == awns:
            print(20 * '*')
            print(f'Right in {count} tries.')
            print(20 * '*')
            break
        else:
            count += 1
            print(20 * '~')
            print('Wrong, try again.')
            print(20 * '~')

welcome_msg()

awns = create_rand_num()

play_game()

