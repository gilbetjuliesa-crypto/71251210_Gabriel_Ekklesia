kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

kata1 = kata1.lower()
kata2 = kata2.lower()

if len(kata1) != len(kata2):
    print("Bukan anagram")
else:
    if sorted(kata1) == sorted(kata2):
        print("Anagram")
    else:
        print("Bukan anagram")
