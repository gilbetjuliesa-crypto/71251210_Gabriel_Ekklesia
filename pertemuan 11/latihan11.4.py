days = dict()

fname = input("Masukkan nama file : ")

try:
    fhand = open(fname)
except:
    print("File tidak bisa dibuka !!", fname)
    exit()

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        day = words[2]   
        
        days[day] = days.get(day, 0) + 1

print("\nJumlah commit per hari :")
print(days)

