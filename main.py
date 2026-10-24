from random import randrange


def which_game_mode():
    print('Welcome to the guessing game.')
    user_input = input('Want to play standard game (1-10)? [Y/n]: ')

    if user_input.lower() == '' or user_input.lower() == 'y':
        return True
    elif user_input.lower() == 'n':
        return False
    else:
        return None


def give_boundaries_user():
    while True:
        try:
            _boundaries = []
            lower = int(input('Input lower boundary: '))
            upper = int(input('Input upper boundary: '))
            if lower < upper:
                _boundaries.append(lower)
                _boundaries.append(upper)
                return _boundaries
            else:
                print()
                print(f'Upper has to be bigger than Lower!')
                print()
                continue
        except ValueError:
            print('Please enter only a valid number!')
            print()


def create_rand_num(lower_bound=1, upper_bound=10):
    _awns = randrange(lower_bound, upper_bound + 1)
    return _awns


def number_guess(lower_bound=1, upper_bound=10):
    while True:
        try:
            _guess = int(input('Input your guess: '))
            if lower_bound <= _guess <= upper_bound:
                return _guess
            else:
                print()
                print(f'Please enter a  valid number between {lower_bound} & {upper_bound}!')
                print()
        except ValueError:
            print('Please enter only a valid number!')
            print()


def play_game(awns, lower, upper):
    count = 1
    l = lower
    u = upper
    print(awns)  #debug line
    while True:
        print()
        print(f'Try: {count}')
        guess = number_guess(l, u)
        if guess == awns:
            print()
            print(20 * '*')
            print(20 * '*')
            print(f'Right in {count} tries.')
            print(20 * '*')
            print(20 * '*')
            break
        else:
            count += 1
            print()
            print(20 * '~')
            print('Wrong, try again.')
            print(20 * '~')


while True:
    mode = which_game_mode()
    if mode == True:
        _boundaries = [1, 10]
        play_game(create_rand_num(), _boundaries[0], _boundaries[1])
        break

    elif mode == False:
        _boundaries = give_boundaries_user()
        play_game(create_rand_num(_boundaries[0], _boundaries[1]), _boundaries[0], _boundaries[1])
        break

    elif not mode:
        print('Please only enter y or no!!!')

    continue
