nama = "rudin" # Inisiasi variabel nama
kunci = "ndeso" # Inisiasi variabel kunci
a = 0 # Inisiasi variabel a

while a!=3: # Perulangan ketika a kurang dari 3
    username = input("Masukkan username: ") # Input username
    password = input("Masukkan password: ") # Input password
    if username == nama and password == kunci: # Jika username = nama dan pass = kunci
        print("Password benar") # Print password benar
        break # selesai
    elif username == nama or password == kunci: # jika username = nama atau pass = kunci
        print("Salah satu input salah") # print salah satu input salah
    else: # jika semua salah
        print("Credentials salah") # print credentials salah
        a = a+1 # Increment a + 1

if a == 3: # Jika a sudah = 3
    print("Anda telah mencoba 3 kali. Silakan coba lagi nanti") # Print sudah mencoba 3x