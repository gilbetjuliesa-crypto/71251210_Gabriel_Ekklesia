#latihan 2.2

#mengambil input 
x = int(input("masukan nilai x (bilangan bulat): "))

#perhitungan
if x !=0:
    hasil = (2 * (x ** 3)) + (2*x) + (15 / x)

#hasil
    print(f"hasil dari f({x}) adalah {hasil}")
else:
    print("eror: nilai x tidak boleh 0 karena akan terjadi pembagian dari nol")