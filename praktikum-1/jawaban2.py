# Praktikum 1 - Problem 2
# Nama    : Muhammad Akmal 
# NIM     : 19624235
# Tanggal : 17 Oktober 2024

#DISCLAIMER: Saya hanya mengikuti perintah dari soal dan mengidenifikasi kasus dari test case serta menggunakan tools yang sudah dipelajari di kelas saja. 

# Program Hadiah Lomba Lari
# Memberi hadiah dollar kompeng kepada peserta lomba yang memenuhi syarat waktu lari kurang dari T detik
# Disclaimer, asumsikan dollar tidak dapat dibagi secara desimal sehingga jika terdapat desimal akan dibulatkan ke bawah

# Kamus
# N -> int
# T -> int
# n1 -> int
# n2 -> int
# n3 -> int
# count -> int
# prize -> int

# Algoritma
N = int(input("Masukkan nilai N: "))
T = int(input("Masukkan nilai T: "))
n1 = int(input("Masukkan waktu lari Tuan Leo: "))
n2 = int(input("Masukkan waktu lari Nona Deb: "))
n3 = int(input("Masukkan waktu lari Nona Sal: "))

count = 0
if n1 <= T :
    count += 1
if n2 <= T :
    count += 1
if n3 <= T :
    count += 1

if count :
    prize = int (N / count)
    print (f"Terdapat {count} peserta yang terkualifikasi dan masing -masing akan mendapatkan {prize} dollar kompeng.")
else :
    print("Tidak ada peserta yang terkualifikasi")