from colorama import init, Fore
from game import play_game
from scoreboard import save_score, show_top_scores

init(autoreset=True)

print(Fore.CYAN + "=== GUESS BATTLE GAME ===")

player_name = input("Masukkan nama pemain: ")

print("\nPilih Level")
print("1. Easy")
print("2. Medium")
print("3. Hard")

try:
    level = int(input("Pilih level: "))

    if level not in [1, 2, 3]:
        print(Fore.RED + "Level harus 1, 2, atau 3!")
    else:
        score = play_game(level)

        print(Fore.GREEN + f"\nScore kamu: {score}")

        save_score(player_name, score)

        print(Fore.YELLOW + "\n=== TOP SCORE ===")
        show_top_scores()

except ValueError:
    print(Fore.RED + "Input harus angka!")