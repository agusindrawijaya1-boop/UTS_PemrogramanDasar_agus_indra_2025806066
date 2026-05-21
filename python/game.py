import random
from colorama import Fore, Style


LEVELS = {
    1: {"range": 10, "attempts": 3},
    2: {"range": 50, "attempts": 5},
    3: {"range": 100, "attempts": 7}
}


def play_level(level):
    config = LEVELS[level]

    max_number = config["range"]
    attempts = config["attempts"]

    secret_number = random.randint(1, max_number)

    print(Fore.CYAN + f"\nLEVEL {level}")
    print(f"Tebak angka dari 1 - {max_number}")
    print(f"Jumlah percobaan: {attempts}")

    while attempts > 0:
        try:
            guess = int(input("Masukkan tebakan: "))

            if guess == secret_number:
                print(Fore.GREEN + "Benar! Kamu menang!")
                score = attempts * 10
                return score

            elif guess < secret_number:
                print(Fore.YELLOW + "Terlalu kecil!")

            else:
                print(Fore.YELLOW + "Terlalu besar!")

            attempts -= 1
            print(Fore.MAGENTA + f"Sisa percobaan: {attempts}")

        except ValueError:
            print(Fore.RED + "Input harus berupa angka!")

    print(Fore.RED + f"Kalah! Angka yang benar adalah {secret_number}")
    return 0