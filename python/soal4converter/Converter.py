import csv
import json

data_mahasiswa = []

total_nilai = 0
jumlah_data = 0

with open("data_mahasiswa.csv", "r") as file:
    reader = csv.DictReader(file)

    print("=== DATA MAHASISWA ===")

    for row in reader:
        print(
            f"{row['Nama']} | "
            f"{row['NIM']} | "
            f"{row['NilaiAkhir']} | "
            f"{row['Mutu']}"
        )

        total_nilai += float(row['NilaiAkhir'])
        jumlah_data += 1

        data_mahasiswa.append({
            "nama": row["Nama"],
            "nim": row["NIM"],
            "nilai_akhir": float(row["NilaiAkhir"]),
            "mutu": row["Mutu"]
        })

rata_rata = total_nilai / jumlah_data

print("\nRata-rata nilai akhir:", rata_rata)

with open("data_mahasiswa.json", "w") as file:
    json.dump(data_mahasiswa, file, indent=4)

print("\nData berhasil dikonversi ke JSON")