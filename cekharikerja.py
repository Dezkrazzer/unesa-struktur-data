def cek_hari_kerja(hari): # Mendefinisikan fungsi cek_hari_kerja
    hari_kerja = ['senin', 'selasa', 'rabu', 'kamis', 'jumat'] # Membuat list hari kerja

    if hari in hari_kerja: # Jika hari yang diinputkan ada di list
        return "Hari ini adalah hari kerja" # Maka print hari tersebut adalah hari kerja
    elif hari == "sabtu" or hari == "minggu": # Jika hari yang diinputkan adalah sabtu atau minggu
        return "Hari ini adalah hari libur" # Maka print hari tersebut adalah hari libur
    else:
        return "Hari yang Anda masukkan tidak valid" # Jika hari yang diinputkan tidak valid, maka print hari tersebut tidak valid
    
input = input("Masukkan hari: ") # Meminta input hari
hasil = cek_hari_kerja(input) # Memanggil fungsi cek_hari_kerja dengan input sebagai parameter
print(hasil) # Print hasil dari fungsi cek_hari_kerja