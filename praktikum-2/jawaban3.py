# Praktikum 2 - Problem 3
# Nama    : Muhammad Akmal 
# NIM     : 19624235
# Tanggal : 31 Oktober 2024

## Program Pembuat ID 
# Program membuat daftar ID yang valid dari rentang yang diberikan (x s.d. y inklusif) dengan ketentuan ID merupakan kelipatan minimal 1 faktor prima dari nomor urut yang diberikan


## Kamus
# no_urut, x, y, i, j, k, l, id : int
# bilangan : array of bool in range(0, no_urut + 1)
# daftar_id : array of int in range(x, y + 1)
# ada, stop, pertama : bool

## Algoritma

# Terima masukan
no_urut = int(input("Masukkan nomor urut: "))
x = int(input("Masukkan batas bawah (x): "))
y = int(input("Masukkan batas atas (y): "))

# Cari faktor prima
bilangan = [True for i in range(no_urut + 1)]

for i in range (2, no_urut + 1) :
    if bilangan[i] : 
        for j in range (i, no_urut + 1, i) :
            bilangan[j] = False
        if (no_urut % i == 0) :
            bilangan[i] = True


# Cari ID dari faktor prima yang ada:
daftar_id = [0 for j in range(x, y + 1)]
ada = False

j = 0
for k in range (x, y + 1) :
    stop = False
    l = 2
    while (l < no_urut and not stop) :
        if (bilangan[l] and k % l == 0) :
            daftar_id[j] = k
            ada = True
            stop = True
            j += 1
        l += 1

# Cetak ID yang valid
if ada :
    print("Id Pengguna yang valid = [", end="")
    pertama = True
    for id in daftar_id :
        if id :
            if pertama :
                print(id, end="")
                pertama = False
            else :
                print(f", {id}", end="")
    print("]")
else :
    print("Tidak ada Id Pengguna yang valid.")
