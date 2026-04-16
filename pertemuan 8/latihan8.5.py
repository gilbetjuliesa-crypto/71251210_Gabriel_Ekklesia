import re
from datetime import datetime

teks = input("Masukkan teks: ")

tanggal_list = re.findall(r'\d{4}-\d{2}-\d{2}', teks)

sekarang = datetime.now()

for tgl in tanggal_list:
    tgl_obj = datetime.strptime(tgl, "%Y-%m-%d")
    selisih = (sekarang - tgl_obj).days
    
    print(tgl_obj, "selisih", selisih, "hari")