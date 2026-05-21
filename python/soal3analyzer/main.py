import argparse
from analyzer import analyze_text
from utils import grafik_ascii

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--file",
        required=True,
        help="Nama file input"
    )

    args = parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as file:
        text = file.read()

    hasil = analyze_text(text)

    report = ""

    report += "=== LAPORAN ANALISIS TEKS ===\n\n"

    report += f"Jumlah Baris : {hasil['baris']}\n"
    report += f"Jumlah Kata : {hasil['kata']}\n"
    report += f"Jumlah Vokal : {hasil['vokal']}\n"
    report += f"Jumlah Konsonan : {hasil['konsonan']}\n\n"

    report += "5 Kata Terbanyak:\n"

    for kata, jumlah in hasil['top_5']:
        report += f"{kata} : {jumlah}\n"

    report += grafik_ascii(hasil['top_5'])

    with open("report.txt", "w", encoding="utf-8") as file:
        file.write(report)

    print(report)

if __name__ == "__main__":
    main()