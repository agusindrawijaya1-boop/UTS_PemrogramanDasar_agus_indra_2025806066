def grafik_ascii(top_words):
    hasil = "\n=== GRAFIK FREKUENSI ===\n"

    for kata, jumlah in top_words:
        hasil += f"{kata:10} {'#' * jumlah}\n"

    return hasil