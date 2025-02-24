print("===================================")
print("         KALKULATOR PHYTON         ")
print("===================================")

angka_1 = int(input("Masukkan angka pertama: "))
angka_2 = int(input("Masukkan angka kedua: "))
operator = input("\n[1] Tambah\n[2] Kurang\n[3] Kali\n[4] Bagi\n\nPilih Operator (1/2/3/4): ")

if operator == "1":
    tambah = angka_1 + angka_2
    print(f"Hasil {angka_1} + {angka_2} = {tambah}")
elif operator == "2":
    kurang = angka_1 - angka_2
    print(f"Hasil {angka_1} - {angka_2} = {kurang}")
elif operator == "3":
    kali = angka_1 * angka_2
    print(f"Hasil {angka_1} * {angka_2} = {kali}")
elif operator == "4":
    bagi = angka_1 / angka_2
    print(f"Hasil {angka_1} / {angka_2} = {bagi}")
else:
    print("Operator yang Anda pilih tidak valid")