fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("File tidak ditemukan!")
    exit()

counts = dict()

for line in fhand:
    line = line.strip()
    
    if line.startswith("From "):
        words = line.split()
        
        time = words[5]
        hour = time.split(":")[0]
        
        counts[hour] = counts.get(hour, 0) + 1

for hour in sorted(counts):
    print(hour, counts[hour])


    