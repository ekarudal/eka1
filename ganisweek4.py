artikels = [
    'justin bieber adalah artis paling keren',
    'ariana grande adalah artis paling mantap',
    'harry style adalah personil 1d dulunya',
]

cari = input('Masukkan pencarian : ')
hasil_cari = [ ]
for artikel in artikels:
    if(cari in artikel):
        hasil_cari.append(artikel)


print(hasil_cari)