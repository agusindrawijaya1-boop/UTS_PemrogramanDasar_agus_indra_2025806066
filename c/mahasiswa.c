#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Mahasiswa {
    char nama[100];
    char nim[20];
    float tugas, uts, uas;
    float nilaiAkhir;
    char mutu;

    struct Mahasiswa *next;
};

typedef struct Mahasiswa Mahasiswa;

// ================= HITUNG NILAI =================
float hitungNilaiAkhir(float tugas, float uts, float uas) {
    return (0.3 * tugas) + (0.3 * uts) + (0.4 * uas);
}

char hitungMutu(float nilai) {
    if (nilai >= 85)
        return 'A';
    else if (nilai >= 70)
        return 'B';
    else if (nilai >= 60)
        return 'C';
    else if (nilai >= 50)
        return 'D';
    else
        return 'E';
}

// ================= TAMBAH DATA =================
void tambahMahasiswa(Mahasiswa **head) {
    Mahasiswa *baru = (Mahasiswa *)malloc(sizeof(Mahasiswa));

    if (baru == NULL) {
        printf("Gagal alokasi memori!\n");
        return;
    }

    printf("\n=== Input Data Mahasiswa ===\n");

    printf("Nama   : ");
    getchar();
    fgets(baru->nama, sizeof(baru->nama), stdin);
    baru->nama[strcspn(baru->nama, "\n")] = 0;

    printf("NIM    : ");
    scanf("%s", baru->nim);

    printf("Nilai Tugas : ");
    scanf("%f", &baru->tugas);

    printf("Nilai UTS   : ");
    scanf("%f", &baru->uts);

    printf("Nilai UAS   : ");
    scanf("%f", &baru->uas);

    baru->nilaiAkhir = hitungNilaiAkhir(
        baru->tugas,
        baru->uts,
        baru->uas
    );

    baru->mutu = hitungMutu(baru->nilaiAkhir);

    baru->next = NULL;

    if (*head == NULL) {
        *head = baru;
    } else {
        Mahasiswa *temp = *head;

        while (temp->next != NULL) {
            temp = temp->next;
        }

        temp->next = baru;
    }

    printf("Data berhasil ditambahkan!\n");
}

// ================= TAMPIL DATA =================
void tampilMahasiswa(Mahasiswa *head) {
    if (head == NULL) {
        printf("\nData kosong!\n");
        return;
    }

    printf("\n================ DATA MAHASISWA ================\n");

    printf("%-20s %-12s %-8s %-8s %-8s %-12s %-5s\n",
           "Nama", "NIM", "Tugas", "UTS", "UAS",
           "NilaiAkhir", "Mutu");

    Mahasiswa *temp = head;

    while (temp != NULL) {
        printf("%-20s %-12s %-8.2f %-8.2f %-8.2f %-12.2f %-5c\n",
               temp->nama,
               temp->nim,
               temp->tugas,
               temp->uts,
               temp->uas,
               temp->nilaiAkhir,
               temp->mutu);

        temp = temp->next;
    }
}

// ================= CARI DATA =================
void cariMahasiswa(Mahasiswa *head) {
    char cariNIM[20];
    int ditemukan = 0;

    printf("\nMasukkan NIM yang dicari: ");
    scanf("%s", cariNIM);

    Mahasiswa *temp = head;

    while (temp != NULL) {
        if (strcmp(temp->nim, cariNIM) == 0) {

            printf("\nData ditemukan!\n");

            printf("Nama         : %s\n", temp->nama);
            printf("NIM          : %s\n", temp->nim);
            printf("Nilai Tugas  : %.2f\n", temp->tugas);
            printf("Nilai UTS    : %.2f\n", temp->uts);
            printf("Nilai UAS    : %.2f\n", temp->uas);
            printf("Nilai Akhir  : %.2f\n", temp->nilaiAkhir);
            printf("Huruf Mutu   : %c\n", temp->mutu);

            ditemukan = 1;
            break;
        }

        temp = temp->next;
    }

    if (!ditemukan) {
        printf("Data tidak ditemukan!\n");
    }
}

// ================= HAPUS DATA =================
void hapusMahasiswa(Mahasiswa **head) {
    char hapusNIM[20];

    printf("\nMasukkan NIM yang ingin dihapus: ");
    scanf("%s", hapusNIM);

    Mahasiswa *temp = *head;
    Mahasiswa *prev = NULL;

    while (temp != NULL &&
           strcmp(temp->nim, hapusNIM) != 0) {

        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("Data tidak ditemukan!\n");
        return;
    }

    if (prev == NULL) {
        *head = temp->next;
    } else {
        prev->next = temp->next;
    }

    free(temp);

    printf("Data berhasil dihapus dan memori dibebaskan!\n");
}

// ================= SIMPAN FILE CSV =================
void simpanCSV(Mahasiswa *head) {
    FILE *file = fopen("data_mahasiswa.csv", "w");

    if (file == NULL) {
        printf("Gagal membuat file!\n");
        return;
    }

    fprintf(file,
            "Nama,NIM,Tugas,UTS,UAS,NilaiAkhir,Mutu\n");

    Mahasiswa *temp = head;

    while (temp != NULL) {

        fprintf(file,
                "%s,%s,%.2f,%.2f,%.2f,%.2f,%c\n",
                temp->nama,
                temp->nim,
                temp->tugas,
                temp->uts,
                temp->uas,
                temp->nilaiAkhir,
                temp->mutu);

        temp = temp->next;
    }

    fclose(file);

    printf("Data berhasil disimpan ke data_mahasiswa.csv\n");
}

// ================= FREE MEMORY =================
void freeMemory(Mahasiswa *head) {
    Mahasiswa *temp;

    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}

// ================= MAIN =================
int main() {

    Mahasiswa *head = NULL;

    int pilihan;

    do {

        printf("\n========== MENU ==========\n");
        printf("1. Tambah Mahasiswa\n");
        printf("2. Tampilkan Data\n");
        printf("3. Cari Mahasiswa\n");
        printf("4. Hapus Mahasiswa\n");
        printf("5. Simpan ke CSV\n");
        printf("0. Keluar\n");

        printf("Pilih menu: ");
        scanf("%d", &pilihan);

        switch (pilihan) {

            case 1:
                tambahMahasiswa(&head);
                break;

            case 2:
                tampilMahasiswa(head);
                break;

            case 3:
                cariMahasiswa(head);
                break;

            case 4:
                hapusMahasiswa(&head);
                break;

            case 5:
                simpanCSV(head);
                break;

            case 0:
                freeMemory(head);
                printf("Program selesai.\n");
                break;

            default:
                printf("Pilihan tidak valid!\n");
        }

    } while (pilihan != 0);

    return 0;
}