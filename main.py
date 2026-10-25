from random import randrange

STANDARD_RANGE: tuple[int,int]= (1, 10)


def ask_game_mode() -> bool | None:
    lower, upper = STANDARD_RANGE
    print('Welcome to the guessing game.')
    user_input = input(f'Want to play standard game ({lower}-{upper})? [Y/n]: ')

    if user_input.lower() == '' or user_input.lower() == 'y':
        return True
    elif user_input.lower() == 'n':
        return False
    else:
        return None


def ask_boundaries() -> tuple[int,int]:
    while True:
        try:
            lower = int(input('Input lower boundary: '))
            upper = int(input('Input upper boundary: '))
            if lower < upper:
                return lower, upper
            else:
                print()
                print('Upper has to be bigger than Lower!')
                print()
                continue
        except ValueError:
            print('Please enter only a valid number!')
            print()


def create_rand_num(lower=1, upper=10):
    answer = randrange(lower, upper + 1)
    return answer


def ask_guess(lower=1, upper=10):
    while True:
        try:
            guess = int(input('Input your guess: '))
            if lower <= guess <= upper:
                return guess
            else:
                print()
                print(f'Please enter a valid number between {lower} & {upper}!')
                print()
        except ValueError:
            print('Please enter only a valid number!')
            print()


def play_game(answer, lower, upper):
    attempts = 1
    while True:
        print()
        print(f'Try: {attempts}')
        guess = ask_guess(lower, upper)
        if guess == answer:
            print()
            print(20 * '*')
            print(20 * '*')
            print(f'Right in {attempts} tries.')
            print(20 * '*')
            print(20 * '*')
            break
        else:
            attempts += 1
            print()
            print(20 * '~')
            print('Wrong, try again.')
            print(20 * '~')




def main():
    while True:
        standard = ask_game_mode()
        if standard is None:
            print('Please enter only y/n')
            continue

        if standard:
           lower, upper = STANDARD_RANGE 
        else:
           lower, upper = ask_boundaries()
        answer = create_rand_num(lower ,upper)
        play_game(answer, lower, upper)
        break

if __name__ == '__main__':
    main()
