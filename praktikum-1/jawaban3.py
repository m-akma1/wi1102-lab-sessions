# Praktikum 1 - Problem 3
# Nama    : Muhammad Akmal 
# NIM     : 19624235
# Tanggal : 17 Oktober 2024

#DISCLAIMER: Saya hanya mengikuti perintah dari soal dan mengidenifikasi kasus dari test case serta menggunakan tools yang sudah dipelajari di kelas saja. 

# Program Menukar Digit
# Diberikan sebuah bilangan N digit, program dapat menukar 2 digit di posisi a dan b
# Dengan aturan, kedua digit yang ditukar tidak boleh 0 (sesuai test case)
# Aturan dari pembuat soal: dilarang menggunakan array sehingga 
# Saya menggunakan modulo dan melakukan konversi string-integer karena sudah dipelajari

# Kamus
# jumlah_digit -> int
# harga -> string
# pos_dgt_1 -> int
# pos_dgt_2 -> int
# digit_1 -> int
# digit_2 -> int
# angka_1 -> int
# angka_2 -> int
# temp_1 -> int
# temp_2 -> int
# ans -> int


# Algoritma
jumlah_digit = int(input("Masukkan jumlah digit harga: "))
harga = str(input("Masukkan harga: "))
pos_dgt_1 = int(input("Masukkan posisi angka pertama yang akan ditukar: "))
pos_dgt_2 = int(input("Masukkan posisi angka kedua yang akan ditukar: "))

if pos_dgt_1 > jumlah_digit or pos_dgt_2 > jumlah_digit :
    print("Masukan harga tidak valid")
else :
    temp_1 = int(harga[pos_dgt_1 - 1])
    temp_2 = int(harga[pos_dgt_2 - 1])

    if ((not temp_1) or (not temp_2)) :
        # Ini digunakan untuk memastikan digit yang ditukar bukan 0, karena di test case ditunjukkan kalau digitnya 0 tidak bisa ditukar
        print("Masukan harga tidak valid")
    else :
        # Keterangan: di sini, saya mengubah harga yang awalnya string menjadi integer untuk diolah dengan sistem modulo
        # digit_1 dan digit_2 menyimpan digit yang akan diubah dalam bentuk a x 10^m dan b x 10^n
        # lalu, kurangi dengan ans untuk mendapatkan jawaban yang tidak berisi digit tersebut
        ans = int(harga)
        digit_1 = (ans % (10**(jumlah_digit - pos_dgt_1 + 1))) - (ans % (10**(jumlah_digit - pos_dgt_1)))
        digit_2 = (ans % (10**(jumlah_digit - pos_dgt_2 + 1))) - (ans % (10**(jumlah_digit - pos_dgt_2)))
        ans = ans - (digit_1 + digit_2)

        # di sini, saya mengekstrak angka 1 dan angka 2 lalu menukarnya dengan cara 
        # mengalikan silang antara angka_1 dan angka_2 dengan digit_1 dan digit_2
        angka_1 = int(digit_1 / (10**(jumlah_digit - pos_dgt_1)))
        angka_2 = int(digit_2 / (10**(jumlah_digit - pos_dgt_2)))
        digit_1 = int(digit_1 / angka_1 * angka_2)
        digit_2 = int(digit_2 / angka_2 * angka_1)
        ans = ans + digit_1 + digit_2

        print(f"Harga setelah diperbaiki : {ans}")

