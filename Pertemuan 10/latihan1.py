def tiga_terbaik(data):
    unik = list(set(data))     
    unik.sort(reverse=True)     
    return unik[:3]             

angka = [10, 5, 8, 20, 20, 4, 15]
hasil = tiga_terbaik(angka)

print(hasil)