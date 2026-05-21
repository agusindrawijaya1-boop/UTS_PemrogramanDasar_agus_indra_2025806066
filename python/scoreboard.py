import json

FILE_NAME = "scores.json"


def load_scores():

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

            # Pastikan data berupa list
            if isinstance(data, list):
                return data
            else:
                return []

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_score(player, score):

    scores = load_scores()

    scores.append({
        "player": player,
        "score": score
    })

    with open(FILE_NAME, "w") as file:
        json.dump(scores, file, indent=4)


def show_top_scores():

    scores = load_scores()

    # Ambil hanya data yang punya key score
    valid_scores = [s for s in scores if "score" in s and "player" in s]

    # Urutkan dari score terbesar
    valid_scores.sort(key=lambda x: x.get("score", 0), reverse=True)

    print("\n=== TOP 5 SCORE ===")

    if not valid_scores:
        print("Belum ada score.")
        return

    for i, data in enumerate(valid_scores[:5], start=1):

        print(f"{i}. {data['player']} - {data['score']} pts")