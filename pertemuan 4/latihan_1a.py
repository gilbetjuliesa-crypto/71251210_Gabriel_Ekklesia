#latihan 4.1 
#Demam atau tidak
suhu = int(input("masukan suhu tubuh: "))
try:
    if suhu >= 38:
        print("anda demam")
    else:
        print("anda tidak demam")
except: 
    print("input tidak valid. masukan angka suhu yang tidak benar.")