def kalkulator():
    print("Kalkulator Sederhana")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))

    if pilihan == '1':
        hasil = angka1 + angka2
    elif pilihan == '2':
        hasil = angka1 - angka2
    elif pilihan == '3':
        hasil = angka1 * angka2
    elif pilihan == '4':
        hasil = angka1 / angka2
    else:
        print("Pilihan tidak valid")
        return
    
    print(f"Hasil: {hasil}")

kalkulator()