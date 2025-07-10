# Praktikum 3 - Problem 1
# Nama    : Muhammad Akmal 
# NIM     : 19624235
# Tanggal : 7 Desember 2024

# Program Pengecek Faktor Prima
# Program menerima dua bilangan lalu memberikan output jumlah semua faktor prima terbesar dari rentang kedua bilangan tersebut

# Kamus
# m: int -> batas bawah
# n: int -> batas atas
# prima: list[bool] -> daftar keprimaan bilangan
# jawaban: int -> jawaban dari soal

# Algoritma

def sieve(p: int):
    # Fungsi generator bilangan prima dengan algoritma Sieve of Erathoreness
    
    # Parameter
    # p: int -> batas atas generator bilangan prima

    # Kembalian
    # prima: list[bool] -> daftar keprimaan bilangan

    # Kamus Lokal
    # i, j, p: int 

    prima = [True for i in range(p + 1)]
    prima[0] = False
    prima[1] = False
    i = 2
    while i < p + 1:
        if prima[i] == True:
            j = i + i
            while j < p + 1:
                prima[j] = False
                j += i
        i += 1
    return prima

def faktor_terbesar(x: int, prima: list):
    # Fungsi mencari faktor prima terbesar suatu bilangan

    # Parameter 
    # x: int -> bilangan yang akan dicari
    # prima: list[bool] -> daftar keprimaan bilangan

    # Kembalian
    # faktor: int -> faktor prima terbesar bilangan tersebut

    # Kamus Lokal
    # i: int

    i = 2
    faktor = 0
    while i < x + 1:
        if (prima[i] and (x % i == 0)):
            faktor = i
        i += 1
    return faktor

m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))

prima = sieve(n)
jawaban = 0
for i in range(m, n + 1):
    jawaban += faktor_terbesar(i, prima)

print(f"Jumlah faktor prima terbesar adalah {jawaban}")