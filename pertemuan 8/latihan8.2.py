kalimat = input("Masukkan kalimat: ")
kata_dicari = input("Masukkan kata yang dicari: ")

kalimat = kalimat.lower()
kata_dicari = kata_dicari.lower()

kalimat = kalimat.replace(".", "")

kata_list = kalimat.split()
jumlah = kata_list.count(kata_dicari)

print(kata_dicari, "ada", jumlah, "buah")