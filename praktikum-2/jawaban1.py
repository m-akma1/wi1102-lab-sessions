# Praktikum 2 - Problem 1
# Nama    : Muhammad Akmal 
# NIM     : 19624235
# Tanggal : 31 Oktober 2024

## Program Mencari Luas Tanah
# Diberikan M buah tanah dengan luas masing-masing tanah[i], program dapat mencari luas rumah dengan ukuran minimum N

## Kamus
# tanah : array of int in range(0, M)
# M, N, i, j, jawaban : int
# ketemu : bool

## Algoritma

# Deklarasikan variabel dan isi array
M = int(input("Masukkan banyak data: "))
tanah = [0 for i in range(M)]

# Input isi array
for i in range (M) :
    tanah[i] = int(input(f"Masukkan luas tanah ke-{i+1}: "))

# Input nilai minimum 
N = int(input(f"Tentukan luas tanah minimum: "))

# Urutkan array dari yang terkecil
for i in range (M) :
    for j in range (i + 1, M) :
        if tanah[i] > tanah[j] :
            tanah[i], tanah[j] = tanah[j], tanah[i]

# Iterasi hingga nilai minimum ditemukan
i = 0
ketemu = False
jawaban = 0
while (i < M and not ketemu) :
    if (tanah[i] >= N) :
        ketemu = True
        jawaban = tanah[i]
    i += 1

# Keluarkan hasil jika ketemu atau tidak
if ketemu : 
    print(f"Luas tanah terkecil yang dapat dipilih adalah {jawaban}.")
else :
    print("Tuan Leo tidak dapat membangun rumah.")