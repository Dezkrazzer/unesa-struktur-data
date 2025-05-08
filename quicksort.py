def quick_sort(arr): # Definisi fungsi quick_sort dengan parameter arr untuk daftar yang akan diurutkan
    if len(arr) <= 1: # Jika panjang arr kurang dari atau sama dengan 1
        return arr  # Return arr (tidak perlu diurutkan)

    pivot = arr[0]  # Ambil elemen pertama sebagai pivot (elemen acuan untuk pembagian)
    left = [x for x in arr[1:] if x < pivot] # Elemen yang lebih kecil dari pivot       
    right = [x for x in arr[1:] if x >= pivot] # Elemen yang lebih besar atau sama dengan pivot    

    return quick_sort(left) + [pivot] + quick_sort(right) # Gabungkan hasil quick_sort dari left, pivot, dan right

data = [64, 10, 55, 26, 33, 7, 18] # Daftar yang akan diurutkan
print("Data sebelum diurutkan:", data) # Print data sebelum diurutkan
sorted_data = quick_sort(data) # Panggil fungsi quick_sort untuk mengurutkan data
print("Hasil Quick Sort:", sorted_data) # Print hasil quick sort

# Contoh diatas, pivot adalah 33, left adalah [10, 26, 7, 18], dan right adalah [55, 64].












# Cara Kerja:
# 1. Fungsi quick_sort memeriksa apakah panjang arr kurang dari atau sama dengan 1. Jika ya, arr sudah terurut dan dikembalikan.
# 2. Jika tidak, elemen pertama arr diambil sebagai pivot.
# 3. Dua daftar baru dibuat: left untuk elemen yang lebih kecil dari pivot dan right untuk elemen yang lebih besar atau sama dengan pivot.
# Jika pivotnya paling besar, maka left berisi semua elemen dan right kosong.
# 4. Fungsi quick_sort dipanggil secara rekursif untuk left dan right, dan hasilnya digabungkan dengan pivot di tengah.
# 5. Proses ini berlanjut hingga semua elemen terurut.
# 6. Hasil akhir adalah daftar yang terurut.
# Keterangan: arr adalah array yang akan diurutkan, pivot adalah elemen acuan untuk pembagian, left adalah elemen yang lebih kecil dari pivot, dan right adalah elemen yang lebih besar atau sama dengan pivot. Fungsi quick_sort memanggil dirinya sendiri secara rekursif untuk mengurutkan left dan right.

# Singkatnya, cara kerja quick sort adalah membagi section. Pertama, pilih pivot, lalu bagi elemen menjadi dua bagian (kiri dan kanan) berdasarkan pivot. Kemudian, urutkan kedua bagian tersebut secara rekursif hingga semua elemen terurut.