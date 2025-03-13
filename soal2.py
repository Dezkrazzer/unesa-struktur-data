import random

angka_rahasia = random.randint(1, 50)
tebakan = -1
percobaan = 0

while tebakan != angka_rahasia:
    tebakan = int (input("Tebak angka (1-50): "))
    percobaan += 1

    if tebakan < angka_rahasia:
        print("Tebakan terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Tebakan terlalu besar!")
    else:
        print("Selamat! Anda menebak dengan benar dalam", percobaan, "percobaan")

# Kesalahan:
# 1. Input dari user tidak diubah ke integer
# 2. Terdapat karakter tidak dikenal pada print("Selamat! Anda menebak dengan benar dalam", percobaan, "percobaan") yang harus dihapus
