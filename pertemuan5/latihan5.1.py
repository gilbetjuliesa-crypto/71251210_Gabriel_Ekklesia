def cek_angka(a, b, c):
    # apakah ada angka yang sama?
    if a == b or a == c or b == c:
        return False

    # penjumlahan
    elif a + b == c:
        return True
    elif a + c == b:
        return True
    elif b + c == a:
        return True
    else:
        return False


# test case
print(cek_angka(2, 3, 5))
print(cek_angka(4, 2, 6))
print(cek_angka(3, 7, 10))
print(cek_angka(5, 5, 10))
print(cek_angka(2, 4, 7))