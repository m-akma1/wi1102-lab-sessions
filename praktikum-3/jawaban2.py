# Praktikum 3 - Problem 2
# Nama    : Muhammad Akmal 
# NIM     : 19624235
# Tanggal : 7 Desember 2024

# Program Dekripsi Kode Rahasia
# Program mendekripsi kode rahasia dengan ketentuan yang diberikan soal. 

# Kamus
# kunci: list[str] -> daftar huruf abjad 
# pesan_rahasia: str -> pesan yang  ingin didekripsi

# Algoritma

kunci = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def dekripsi_angka(pesan: str):
    # Fungsi mendekripsi angka sesuai ketentuan soal.

    # Parameter
    # pesan: str -> pesan yang ingin didekripsi

    # Kembalian
    # hasil: list[int] -> daftar angka yang siap dicocokkan ke kunci

    # Kamus Lokal
    # bilangan: int -> variabel sementara

    hasil = [0 for i in range(len(pesan)//2)]
    for i in range(0, len(pesan), 2):
        bilangan = int(pesan[i])*10 + int(pesan[i+1])
        if bilangan % 2:
            bilangan //= 3
        else:
            bilangan //= 2
        hasil[i//2] = bilangan
    return hasil


def dekripsi_huruf(kode: list):
    # Prosedur mendekripsi kode dan mencetaknya langsung ke terminal

    # Parameter
    # kode: list[int] - > daftar angka yang siap dicocokkan ke kunci

    # Kamus Lokal
    # angka: int -> variabel sementara

    for angka in kode:
        print(kunci[angka - 1], end="")

pesan_rahasia = input("Pesan rahasia: ")
dekripsi_huruf(dekripsi_angka(pesan_rahasia))
