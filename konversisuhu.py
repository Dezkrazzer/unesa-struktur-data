def konversi_suhu(): # Mendefinisikan fungsi konversi_suhu
    # Menampilkan pilihan konversi suhu
    print("1. Celcius ke Fahrenheit") 
    print("2. Fahrenheit ke Celcius")

    pilihan = input("Masukkan pilihan (1/2): ") # Meminta input pilihan

    if pilihan == '1': # Jika pilihan adalah 1
        celcius = float(input("Masukkan suhu dalam celcius: ")) # Meminta input suhu dalam celcius
        fahrenheit = (celcius * 9/5) + 32 # Menghitung suhu dalam fahrenheit
        print(f"Suhu dalam fahrenheit adalah {fahrenheit} F") # Print suhu dalam fahrenheit
    elif pilihan == '2': # Jika pilihan adalah 2
        fahrenheit = float(input("Masukkan suhu dalam fahrenheit: ")) # Meminta input suhu dalam fahrenheit
        celcius = (fahrenheit - 32) * 5/9 # Menghitung suhu dalam celcius
        print(f"Suhu dalam celcius adalah {celcius} C") # Print suhu dalam celcius
    else: # Jika pilihan tidak valid
        print("Pilihan tidak valid") # Print pilihan tidak valid
        return

konversi_suhu() # Memanggil fungsi konversi_suhu