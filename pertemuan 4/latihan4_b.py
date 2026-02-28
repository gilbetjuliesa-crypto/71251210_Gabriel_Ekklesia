#positif atau negatif 
bilangan = int(input("masukan suatu bilangan"))
try: 
    if bilangan > 0:
        print("positif")
    elif bilangan < 0:
        print("negatif")
    else:
        print("nol")
except:
    print("input tidak valid. masukan angka yang benar.")