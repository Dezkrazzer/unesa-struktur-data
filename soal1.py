jumlah = int (input("Masukkan jumlah bilangan: "))
ganjil = 0
genap = 0

for i in range(1, jumlah + 1): 
    bil = int (input(f"Masukkan bilangan ke {i}:"))  
    
    if bil % 2 == 0 : 
        genap += 1  
        print(bil, "adalah bilangan genap")  
    else: 
        ganjil += 1  
        print(bil, "adalah bilangan ganjil")  

print("\nHasil Perhitungan:")  
print("Bilangan Genap:", genap)  
print("Bilangan Ganjil:", ganjil)
          
# Kesalahan:
# 1. Pada baris 1, jumlah harus diubah menjadi integer dengan cara int(jumlah)
# 2. Inisiasi ganjil dan genap
# 3. Menambahkan +1 pada for i range(1, jumlah) karena range tidak termasuk jumlah
# 4. Mengubah bil = int(input(f"Masukkan bilangan ke {i}:")) karena hanya boleh 1 argument dalam input
# 5. Menambahkan titik dua pada if dan else
# 6. Menghapus for j range(0, jumlah) karena tidak diperlukan
# 7. Mengubah print("Bilangan Genap:", genap) menjadi print("Bilangan Genap:", genap) karena ada spasi
# 8. Mengubah print("Bilangan Ganjil:", ganjil) menjadi print("Bilangan Ganjil:", ganjil) karena ada spasi