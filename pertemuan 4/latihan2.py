#latihan 4.2
bilangan = int(input("masukan suatu bilangan"))
try: 
    hasil = "Positif" if bilangan > 0 else "Negatif" if bilangan < 0 else "nol"
    print(hasil)
except:
        print("inputan tidak valid. masukan angka")