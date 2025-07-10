# Praktikum 1 - Problem 1
# Nama    : Muhammad Akmal 
# NIM     : 19624235
# Tanggal : 17 Oktober 2024

#DISCLAIMER: Saya hanya mengikuti perintah dari soal dan mengidenifikasi kasus dari test case serta menggunakan tools yang sudah dipelajari di kelas saja. 

# Program Rata-Rata Kuis
# Mencari rata-rata ketiga kuis dan memberikan predikat kelulusan

# Kamus
# k1 -> int
# k2 -> int
# k3 -> int
# avg -> float

# Algoritma
k1 = int(input("Masukkan nilai kuis pertama : "))
k2 = int(input("Masukkan nilai kuis kedua : "))
k3 = int(input("Masukkan nilai kuis kegita : "))

avg = (k1 + k2 + k3)/3

if avg >= 80 :
    print("Tuan Leo mendapatkan nilai Lulus Memuaskan.")
elif avg >= 70 :
    print("Tuan Leo mendapatkan nilai Lulus.")
else :
    print("Tuan Leo mendapatkan nilai Tidak Lulus.")