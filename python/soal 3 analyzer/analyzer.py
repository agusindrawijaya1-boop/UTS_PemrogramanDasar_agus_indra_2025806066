from collections import Counter

def analyze_text(text):
    lines = text.splitlines()
    words = text.lower().split()

    jumlah_baris = len(lines)
    jumlah_kata = len(words)

    counter = Counter(words)
    top_5 = counter.most_common(5)

    vokal = "aiueo"

    jumlah_vokal = 0
    jumlah_konsonan = 0

    for huruf in text.lower():
        if huruf.isalpha():
            if huruf in vokal:
                jumlah_vokal += 1
            else:
                jumlah_konsonan += 1

    return {
        "baris": jumlah_baris,
        "kata": jumlah_kata,
        "top_5": top_5,
        "vokal": jumlah_vokal,
        "konsonan": jumlah_konsonan
    }