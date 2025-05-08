def partition(array, low, high): # Definisi fungsi partition
    pivot = array[high] # Ambil elemen terakhir sebagai pivot
    i = low - 1 # Inisialisasi indeks i dari low - 1

    for j in range(low, high): # Perulangan dari low hingga high - 1
        if array[j] <= pivot: # Jika elemen saat ini lebih kecil atau sama dengan pivot
            i += 1 # Tambah indeks i 
            array[i], array[j] = array[j], array[i] # Tukar elemen array[i] dan array[j]

    array[i+1], array[high] = array[high], array[i+1] # Tukar elemen array[i+1] dan array[high]
    return i+1 # Kembalikan indeks pivot baru

def quicksort(array, low=0, high=None): # Definisi fungsi quicksort
    if high is None: # Jika high tidak diberikan, set ke panjang array - 1
        high = len(array) - 1 # Inisialisasi high dari panjang array - 1

    if low < high: # Jika low lebih kecil dari high
        pivot_index = partition(array, low, high) # Panggil fungsi partition untuk mendapatkan indeks pivot dengan low dan high
        quicksort(array, low, pivot_index-1) # Panggil quicksort untuk bagian kiri dari pivot
        quicksort(array, pivot_index+1, high) # Panggil quicksort untuk bagian kanan dari pivot

my_array = [64, 34, 25, 12, 22, 11, 90, 5] # Daftar yang akan diurutkan
quicksort(my_array) # Panggil fungsi quicksort untuk mengurutkan my_array
print("Sorted array:", my_array) # Print hasil quicksort