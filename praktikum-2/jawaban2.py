# Praktikum 2 - Problem 2
# Nama    : Muhammad Akmal 
# NIM     : 19624235
# Tanggal : 31 Oktober 2024

## Program Bagi-Bagi Konsumsi
# Program memastikan setiap pengunjung dengan tiket dari 0 s.d. 999 inklusif (asumsi soal) tidak mendapat konsumsi lebih dari 1 kali, program menerima masukan hingga diberi tanda stop ("XXX")

## Kamus
# no_tiket : array of int in range(0, 1000)
# dapat, curang, tiket : int
# masukan : str -> int

## Algoritma

# Asumsi yang saya buat dari soal adalah tiket pengunjung hanya berada di rentang 000 - 999 inklusif
no_tiket = [0 for i in range(1000)]

# Buat penghitung banyak orang yang mendapat konsumsi
dapat = 0

# Terima input hingga masukan adalah "XXX"
masukan = str(input("Masukkan nomor tiket pengunjung: "))
while (masukan != "XXX") :
    masukan = int(masukan)

    # Tambahkan nilai di array untuk setiap permintaan
    if (no_tiket[masukan] == 0) :
        print("Pengunjung tersebut bisa mendapat konsumsi.")
        no_tiket[masukan] += 1
        dapat += 1
    else :
        print("Pengunjung tersebut tidak bisa mendapat konsumsi lagi.")
        no_tiket[masukan] += 1
    
    masukan = str(input("Masukkan nomor tiket pengunjung: "))

# Hitung berapa orang yang curang
curang = 0
for tiket in no_tiket :
    if tiket > 1 :
        curang += 1

# Keluarkan data
print(f"Total pengunjung yang mendapat konsumsi: {dapat}")
print(f"Total pengunjung yang mencoba mendapat konsumsi lebih dari satu kali: {curang}")