def rata_rata():
    data = []
    
    n = int(input("Berapa banyak angka: "))
    
    for i in range(n):
        angka = int(input("Masukkan angka: "))
        data.append(angka)
    
    if len(data) > 0:
        print("Rata-rata:", sum(data) / len(data))
    else:
        print("Tidak ada data")

rata_rata()


