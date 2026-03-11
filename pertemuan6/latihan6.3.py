jumlah = int(input("Masukkan jumlah mata kuliah: "))

total = 0

for i in range(jumlah):
    nilai = input("Masukkan nilai (A/B/C/D): ")

    if nilai == "A":
        total = total + 4
    elif nilai == "B":
        total = total + 3
    elif nilai == "C":
        total = total + 2
    elif nilai == "D":
        total = total + 1

ips = total / jumlah

print("IPS =", ips)