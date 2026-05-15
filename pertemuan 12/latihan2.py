data = ('Gabriel Ekklesia', '71251210', 'kalimantan tengah')
print("Data:", data)

nama, nim, alamat = data

print("NIM :", nim)
print("NAMA :", nama)
print("ALAMAT :", alamat)

nim_tuple = tuple(nim)
print("NIM:", nim_tuple)

nama_depan = tuple(nama.split()[0][1:])
print("NAMA DEPAN:", nama_depan)

nama_terbalik = tuple(nama.split()[::-1])
print("NAMA TERBALIK:", nama_terbalik)

