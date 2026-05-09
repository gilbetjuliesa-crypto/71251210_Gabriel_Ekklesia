dictionary_words = {}

fname = input("Masukkan nama file : ")

try:
    fhand = open(fname)
except FileNotFoundError:
    print("File tidak bisa dibuka !!", fname)
    exit()

for line in fhand:
    if not line.startswith("From "):
        continue

    words = line.split()
    email = words[1]

    dictionary_words[email] = dictionary_words.get(email, 0) + 1

print(dictionary_words)

