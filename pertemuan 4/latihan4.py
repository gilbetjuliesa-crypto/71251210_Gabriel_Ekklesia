s1 = int(input("masukan sisi 1: "))
s2 = int(input("masukan sisi 2: "))
s3 = int(input("masukan sisi 3: "))
try:
    if s1 <= 0 or s2 <= 0 or s3 <= 0:
        print("input tidak valid. sisi harus lebih dari 0.")
    else:
        if s1 == s2 == s3:
            print("semua sisi sama")
        elif s1 == s2 or s1 == s3 or s2 == s3:
            print("hanya 2 sisi yang sama")
        else: 
            print("tidak ada sisi yang sama")
except:
    print("input tidak valid. masukan angka bulat.")