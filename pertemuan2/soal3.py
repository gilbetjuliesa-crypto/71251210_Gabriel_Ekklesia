#latihan 2.3

#mengambil input 
gaji_per_jam = float(input("masukan gaji per jam yang diinginkan: "))
jam_kerja_minggu = float(input("masukan jam kerja per minggu: "))

#perhitungan 
pendapatan_bruto = gaji_per_jam * jam_kerja_minggu * 5

#pendapatan netto 
pajak = 0.14 * pendapatan_bruto
pendapatan_bersih = pendapatan_bruto - pajak

#belanja baju dan aksesoris (10% dari pendapatan bersih)
uang_baju = 0.01 * pendapatan_bersih

#belanja alat tulis (1% dari pendapatan bersih)
uang_belanja_alat_tulis = 0.01 * pendapatan_bersih

#sedekah (25% dari sisa uang belanja)
sisa_uang_belanja = pendapatan_bersih - uang_baju - uang_belanja_alat_tulis 
total_sedekah = 0.25 * sisa_uang_belanja 

#pembagian sedekah 
uang_anak_yatim = 0.30 * total_sedekah
uang_kaum_dhuafa = total_sedekah - uang_anak_yatim

print("\n" + "="*40)
print(f" pendapatan bruto budi : Rp {pendapatan_bruto:,.2f}")
print(f" pendapatan netto setelah pajak : Rp {pendapatan_bersih:,.2f}")
print(f" uang untuk belanja untuk membeli pakaian : Rp {uang_baju:,.2f}")
print(f" uang untuk membeli alat tulis : Rp {uang_belanja_alat_tulis:,.2f}")
print(f" total uang yang disedekahkan : RP {total_sedekah:,.2f}")
print(f" total sedekah untuk anak yatim : Rp {uang_anak_yatim:,.2f}")
print(f" uang sedekah untuk kaum dhufan : Rp {uang_kaum_dhuafa:,.2f}")
print("="*40)