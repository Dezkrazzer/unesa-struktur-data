print("===================================")
print("         KALKULATOR PHYTON         ")
print("===================================")

angka_1 = int(input("» Masukkan angka pertama: "))
angka_2 = int(input("» Masukkan angka kedua: "))
operator = input("» Pilih Operator (+, -, x, /): ")

if operator == "+":
    tambah = angka_1 + angka_2
    print(f"\nHasil {angka_1} + {angka_2} = {tambah}")
elif operator == "-":
    kurang = angka_1 - angka_2
    print(f"\nHasil {angka_1} - {angka_2} = {kurang}")
elif operator == "x":
    kali = angka_1 * angka_2
    print(f"\nHasil {angka_1} x {angka_2} = {kali}")
elif operator == "/":
    bagi = angka_1 / angka_2
    print(f"\nHasil {angka_1} / {angka_2} = {bagi}")
else:
    print("\n[ERROR] Operator yang Anda pilih tidak valid")