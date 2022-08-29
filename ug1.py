print("="*5, "PROGRAM KALKULATOR SEDERHANA" ,"="*5)
print("1. Penambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print()
print("Tekan tombol Q bila ingin keluar aplikasi ini")
print()

def tambah(a, b):
    return a + b
def kurang(a, b):
    return a - b
def kali(a, b):
    return a * b
def bagi(a, b):
    return a / b

while(True):
    pilih = input("Silahkan pilih kalkulasi : ")
    if pilih == "Q":
        break
    elif int(pilih) < 1 or int(pilih) > 4:
        print("Maaf, anda salah pilih opsi kalkulasi silahkan pilih ulang")
    else:
        a = int(input("Masukkan angka pertama : "))
        b = int(input("Masukkan angka kedua : "))
        if int(pilih) == 1:
            print("Hasil dari penambahannya adalah : ",tambah(a,b))
        elif int(pilih) == 2:
            print("Hasil dari pengurangannya adalah : ",kurang(a,b))
        elif int(pilih) == 3:
            print("Hasil dari perkaliannya adalah : ",kali(a,b))
        else:
            print("Hasil dari pembagiannya adalah : ",bagi(a,b))
