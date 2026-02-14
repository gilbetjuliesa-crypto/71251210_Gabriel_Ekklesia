#latihan 2.1

#mengambil input
tinggi_m = float(input("masukan tinggi badan (meter): "))
target_bmi = float(input("masukan nilai bmi: "))

#perhitungan 
berat_yang_diperlukan = target_bmi * (tinggi_m ** 2)

# hasil 
print("-" * 35)
print(f"mencari BMI {target_bmi},")
print(F"berat badan yang diperlukan adalah: {berat_yang_diperlukan:.2f} kg")
