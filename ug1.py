print("="*10, "PROGRAM KALKULATOR SEDERHANA" ,"="*10)
print("Masukkan input seperti 4 + 3 atau 1 * 2.")
print("Pastikan untuk menggunakan spasi pada setiap perhitungan.")
print()

try:
    while(True):
        kal = input("Masukkan input : ")
        if kal == "Q":
            print("Anda sudah keluar dari aplikasi ini")
            break       
        lst = kal.split()
        if lst[1] == "+":
            print("Hasil : ",int(lst[0]) + int(lst[2]))
        elif lst[1] == "-":
            print("Hasil : ",int(lst[0]) - int(lst[2]))
        elif lst[1] == "*":
            print("Hasil : ",int(lst[0]) * int(lst[2]))
        elif lst[1] == "/":
            print("Hasil : ",int(lst[0]) / int(lst[2]))
        else:
            print("Salah operator")
except:
    print("Salah input, silahkan ulangi")