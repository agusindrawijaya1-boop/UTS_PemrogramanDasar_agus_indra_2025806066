import random
from colorama import Fore

def play_game(level):

    if level == 1:
        max_number = 10
        attempts = 3

    elif level == 2:
        max_number = 50
        attempts = 5

    elif level == 3:
        max_number = 100
        attempts = 7

    else:
        print(Fore.RED + "Level tidak valid!")
        return 0

    secret_number = random.randint(1, max_number)

    print(Fore.CYAN + f"\nTebak angka 1 - {max_number}")

    while attempts > 0:

        try:
            guess = int(input("Tebakan: "))

            if guess == secret_number:

                print(Fore.GREEN + "Benar!")

                score = attempts * 50

                print(Fore.GREEN + f"Score: {score}")

                return score

            elif guess < secret_number:
                print(Fore.YELLOW + "Terlalu kecil!")

            else:
                print(Fore.YELLOW + "Terlalu besar!")

            attempts -= 1

            print(Fore.CYAN + f"Sisa kesempatan: {attempts}")

        except ValueError:
            print(Fore.RED + "Input angka!")

    print(Fore.RED + f"Kalah! Jawaban: {secret_number}")

    return 0