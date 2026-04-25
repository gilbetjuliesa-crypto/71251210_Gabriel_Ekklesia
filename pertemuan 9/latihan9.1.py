f1 = open("Test1.txt", "r")
f2 = open("Test2.txt", "r")

data1 = f1.readlines()
data2 = f2.readlines()

i = 0
maks = max(len(data1), len(data2))

while i < maks:
    if i < len(data1):
        a = data1[i].strip()
    else:
        a = ""

    if i < len(data2):
        b = data2[i].strip()
    else:
        b = ""

    if a != b:
        print("beda di baris", i+1)
        print("file1:", a)
        print("file2:", b)
        print()

    i += 1

f1.close()
f2.close()