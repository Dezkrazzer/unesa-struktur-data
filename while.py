i = 2 # Inisialisasi variabel i dengan nilai 2
while(i < 100): # Perulangan while dengan kondisi i kurang dari 100
    j = 2 # Inisialisasi variabel j dengan nilai
    while(j <= (i/j)): # Perulangan while dengan kondisi j kurang dari sama dengan i/j
        if not(i%j): break # Jika i mod j tidak sama dengan 0, maka hentikan perulangan
        j = j + 1 # Increment j
    if (j > i/j): print(i, " bilangan prima") # Jika j lebih besar dari i/j, maka print i bilangan prima
    i = i + 1 # Increment i

print("Selesai")