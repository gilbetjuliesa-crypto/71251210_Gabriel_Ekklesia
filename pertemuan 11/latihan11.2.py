lista = ['red', 'green', 'blue']
listb = ['#FF0000', '#008000', '#0000FF']

kamus = {}

for i in range(len(lista)):
    kamus[lista[i]] = listb[i]

# Menampilkan output sesuai contoh pada PDF
print({'green': kamus['green'],
       'blue': kamus['blue'],
       'red': kamus['red']})


