# Praktikum 3 - Problem 3
# Nama    : Muhammad Akmal 
# NIM     : 19624235
# Tanggal : 7 Desember 2024

# Program Arsip Digital
# Mengarsipkan secara digital file

# Kamus

# Algoritma
def inisialisasi_tipe():
    # Fungsi inisialisasi tipe yang menyiapkan tipe dokumen dari masukan pengguna dan mengeluarkan tipe dokumen dan penghitung urutannya

    jumlah = int(input("Masukkan jumlah tipe dokumen: "))
    tipe = ["" for i in range(jumlah)]
    for i in range(jumlah):
        tipe[i] = input(f"Masukkan tipe dokumen ke-{i+1}: ")

    tipe_counter = [0 for i in range(jumlah)]
    return tipe, tipe_counter

def inisialisasi_rak(tipe, tipe_counter):
    # Fungsi inisialisasi rak yang membuat rak dan mengisinya dengan isi rak yang sudah ada
    # Fungsi mengembalikan slot dan banyaknya slot yang terisi
    jumlah = int(input("Masukkan jumlah slot rak arsip: "))
    slot = ["" for i in range(jumlah)]
    isi = 0

    print("Masukkan isi rak arsip saat ini!")
    for i in range(jumlah):
        slot[i] = input(f"Slot {i+1}: ") 
        # Asumsi masukan slot sudah pasti benar
        if (slot[i] != ""):
            counter = int(slot[i][-2:])
            # Saya asumsikan di sini penomoran tidak lebih dari 99
            if counter < 0:
                counter *= -1
            indeks = cari(slot[i][:-3], tipe)
            if indeks != False:
                tipe_counter[indeks - 1] = max(counter, tipe_counter[indeks - 1])
            else :
                indeks = cari(slot[i][:-2], tipe)
                tipe_counter[indeks - 1] += max(counter, tipe_counter[indeks - 1])
            isi += 1
    return slot, isi

def cari(dok, tipe):
    # Fungsi pencarian dokumen yang mengembalikan indeks di mana dokumen ditemukan, jika tidak mengembalikan False

    for i in range(len(tipe)):
        if dok == tipe[i]:
            return i + 1
    return False

def isi_rak(slot, jumlah, tipe, tipe_counter): 
    # Prosedur mengisi raak sampai penuh atau sampai user bilang selesai
    while jumlah < len(slot):
        dokumen = input("Masukkan dokumen baru: ")
        if dokumen == "selesai":
            break
        
        indeks = cari(dokumen, tipe)
        if indeks:
            for i in range(len(slot)) :
                if slot[i] == "":
                    tipe_counter[indeks - 1] += 1
                    slot[i] = dokumen + "-" + str(tipe_counter[indeks - 1])
                    jumlah += 1
                    break
        else:
            print(f"Tipe dokumen {dokumen} tidak valid!")
    else:
        print("Rak arsip sudah penuh!")

def cari_rak(slot):
    # Prosedur mencari dokumen di rak hingga user bilang selesai
    masukan = input("Masukkan tipe dokumen yang ingin dicari: ")
    while masukan != "selesai":
        ditemukan = False
        for i in range(len(slot)):
            if slot[i][:-3] == masukan:
                print(f"Dokumen {slot[i]} ditemukan pada slot {i + 1}")
                ditemukan = True
            elif slot[i][:-2] == masukan:
                print(f"Dokumen {slot[i]} ditemukan pada slot {i + 1}")
                ditemukan = True
        if not ditemukan:
            print("Dokumen tidak ditemukan")
        masukan = input("Masukkan tipe dokumen yang ingin dicari: ")


# Program Utama

tipe, counter = inisialisasi_tipe()
print("")
slot, isi = inisialisasi_rak(tipe, counter)
print("")
isi_rak(slot, isi, tipe, counter)
print("")
cari_rak(slot)