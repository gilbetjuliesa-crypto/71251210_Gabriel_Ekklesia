data = input("Masukkan angka, pisahkan dengan spasi: ")
tA = tuple(map(int, data.split()))
status = True

for i in range(len(tA)):
    if tA[i] != tA[0]:
        status = False

print(status)

