def binary_search(arr, target): # Definisi fungsi binary_search dengan dua parameter: arr (daftar yang sudah diurutkan) dan target (nilai yang dicari)
    low = 0 # Inisialisasi batas bawah
    high = len(arr) - 1 # Inisialisasi batas atas

    while low <= high: # Selama batas bawah kurang dari atau sama dengan batas atas
        mid = (low + high) // 2  # Hitung indeks tengah
        guess = arr[mid] # Ambil nilai pada indeks tengah

        if guess == target: # Jika nilai pada indeks tengah sama dengan target
            return mid  # target ditemukan
        elif guess < target: # Jika nilai pada indeks tengah kurang dari target
            low = mid + 1  # cari di bagian kanan
        else: # Jika nilai pada indeks tengah lebih besar dari target
            high = mid - 1  # cari di bagian kiri

    return -1  # target tidak ditemukan

# Contoh penggunaan
data = ["apel", "jeruk", "mangga", "pisang", "semangka"] # Daftar buah yang sudah diurutkan
cari = str(input("Masukkan buah yang ingin dicari: ")) # Meminta input dari user untuk mencari buah

hasil = binary_search(data, cari) # Memanggil fungsi binary_search dengan data dan cari sebagai parameter

if hasil != -1: # Jika hasil tidak sama dengan -1, berarti buah ditemukan
    print(f"Buah {cari} ditemukan pada indeks {hasil}.")
else:
    print(f"Buah {cari} tidak ditemukan dalam daftar.")
