def kata_unik(nama_file):
    file = open(nama_file, "r")
    teks = file.read()
    file.close()
    
    kata = teks.split()        
    unik = list(set(kata))        
    
    print("Kata unik:")
    for k in unik:
        print(k)

kata_unik("berita.txt")