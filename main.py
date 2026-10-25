from random import randint

STANDARD_RANGE: tuple[int, int] = (1, 10)
BANNER_WIDTH = 20


def print_banner(char: str) -> None:
    line = char * BANNER_WIDTH
    print(line)
    print(line)


def ask_game_mode() -> bool | None:
    lower, upper = STANDARD_RANGE
    print("Welcome to the guessing game.")
    raw = input(f"Want to play standard game ({lower}-{upper})? [Y/n]: ")
    

    if raw.lower() == "" or raw.lower() == "y":
        return True
    elif raw.lower() == "n":
        return False
    else:
        return None


def ask_boundaries() -> tuple[int, int]:
    while True:
        try:
            lower = int(input("Input lower boundary: "))
            upper = int(input("Input upper boundary: "))
            if lower < upper:
                return lower, upper
            print()
            print("Upper has to be bigger than Lower!")
            print()
        except ValueError:
            print("Please enter only a valid number!")
            print()


def create_rand_num(lower: int, upper: int) -> int:
    answer = randint(lower, upper)
    return answer


def ask_guess(lower: int, upper: int) -> int:
    while True:
        try:
            guess = int(input("Input your guess: "))
            if lower <= guess <= upper:
                return guess
            print()
            print(f"Please enter a valid number between {lower} & {upper}!")
            print()
        except ValueError:
            print("Please enter only a valid number!")
            print()


def play_game(answer, lower, upper):
    attempts = 1
    while True:
        print()
        print(f"Try: {attempts}")
        guess = ask_guess(lower, upper)
        if guess == answer:
            print()
            print_banner("*")
            print(f"Right in {attempts} tries.")
            print_banner("*")
            break
        attempts += 1
        print()
        print_banner("~")
        print("Wrong, try again.")
        print_banner("~")


def main():
    while True:
        standard = ask_game_mode()
        if standard is None:
            print("Please enter only y/n")
            continue

        if standard:
            lower, upper = STANDARD_RANGE
        else:
            lower, upper = ask_boundaries()
        answer = create_rand_num(lower, upper)
        play_game(answer, lower, upper)
        break


if __name__ == "__main__":
    main()
