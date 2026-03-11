def perkalian(a, b):
    hasil = 0
    for i in range(a):
        hasil = hasil + b
    return hasil

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

print("Hasil perkalian:", perkalian(a,b))