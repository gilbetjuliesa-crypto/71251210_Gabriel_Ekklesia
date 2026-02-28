#nilai terbesar 
x = int(input("masukan bilangan pertama"))
y = int(input("masukan bilangan kedua"))
z = int(input("masukan bilangan ketiga"))

try:
    if x > y and z:
        print("nilai terbesar", x)
    elif y > x and y > z:
        print("nilai terbesar", y)
    else:
        print("nilai terbesar", z)
except: 
    print("input tidak valid. semua input harus angka")