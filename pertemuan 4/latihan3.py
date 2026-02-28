#latihan 4.3
bulan = int(input("masukan bulan (1-12): "))
try:
    if bulan <1 or bulan > 12:
        print("Bulan tidak valid")
    else:
        if bulan == 2:
            print("Jumlah hari: 29")
        elif bulan in [4, 6, 9, 11]:
            print("Jumlah hari: 30")
        else: 
            print("Jumlah hari: 31")
except: 
    print("input tidak valid. masukan angka 1-12.")