from colorama import init, Fore
from game import play_level
from scoreboard import save_score, show_top_scores

# Inisialisasi colorama
init(autoreset=True)


def main():
    print(Fore.BLUE + "=== GUESS BATTLE GAME ===")

    player_name = input("Masukkan nama pemain: ")

    total_score = 0

    for level in range(1, 4):
        score = play_level(level)
        total_score += score

    print(Fore.CYAN + f"\nGame selesai!")
    print(Fore.GREEN + f"Total skor {player_name}: {total_score}")

    # Simpan skor
    save_score(player_name, total_score)

    # Tampilkan top score
    show_top_scores()


if __name__ == "__main__":
    main()