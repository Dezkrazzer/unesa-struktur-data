nama = "rudin"
kunci = "ndeso"
a = 0

while a!=3:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username == nama and password == kunci:
        print("Password benar")
        break
    elif username == nama or password == kunci:
        print("Salah satu input salah")
    else:
        print("Password salah")
        a = a+1

if a == 3:
    print("Anda telah mencoba 3 kali. Silakan coba lagi nanti")