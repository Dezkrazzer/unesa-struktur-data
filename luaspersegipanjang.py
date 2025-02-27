panjang = int(input("Masukkan panjang: ")) # Memasukkan panjang
lebar = int(input("Masukkan lebar: ")) # Memasukkan lebar
luas = panjang * lebar # Menghitung luas

if panjang == lebar: # jika panjang dan lebar sama, maka bukan persegi panjang
    print("Input yang anda masukkan bukan persegi panjang")
else: # jika panjang dan lebar berbeda, maka hitung luas
    print(f"Luas persegi panjang adalah {luas}")
