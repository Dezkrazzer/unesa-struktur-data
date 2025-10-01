# Program Laporan Pencampuran Warna

'''
    Description:
    Annis adalah seorang seniman digital yang sedang bereksperimen dengan warna. Annis ingin membuat sebuah program yang dapat mensimulasikan pencampuran dua warna dan menganalisis hasilnya. Warna direpresentasikan dalam model RGB (Red, Green, Blue), dengan nilai setiap komponen dari 0 hingga 255.
    Proses pencampuran dua warna didefinisikan sebagai rata-rata dari setiap komponen warnanya (gunakan pembagian integer). Setelah mendapatkan warna baru, Anda ingin tahu:

    Apa nilai RGB dari warna hasil campuran?
    Apakah warna tersebut merupakan warna abu-abu (grayscale)? (Kondisi: R = G = B)
    Jika bukan abu-abu, komponen warna mana (R, G, atau B) yang paling dominan?

    Input Format
    Satu baris berisi enam integer yang dipisahkan spasi: r1 g1 b1 r2 g2 b2

    r1 g1 b1: komponen RGB dari warna pertama
    r2 g2 b2: komponen RGB dari warna kedua
    Fungsi utama: process(r1, g1, b1, r2, g2, b2)

    Membaca input
    Membuat objek warna
    Mencampur dan menganalisis
    Menampilkan output sesuai format

    Constraints
    Semua input adalah integer valid

    Output Format
    Baris 1: Tiga integer dipisahkan spasi: r g b (warna hasil campuran)
    Baris 2: Sebuah string yang merupakan salah satu dari:

    "Abu-abu" (jika warna hasil adalah grayscale)
    "Dominan Merah" (jika komponen merah paling dominan)
    "Dominan Hijau" (jika komponen hijau paling dominan)
    "Dominan Biru" (jika komponen biru paling dominan)

    Sample Input 0:
    200 100 50 100 100 250

    Sample Output 0:
    150 100 150
    Dominan Merah

    Sample Input 1:
    10 200 200 10 200 200

    Sample Output 1:
    10 200 200
    Dominan Hijau

    Sample Input 2:
    -1 200 3 4 5 6

    Sample Output 2:
    Input tidak valid
'''

# Konstruktor: MakeWarna(r, g, b)


def MakeWarna(r, g, b):
    return (r, g, b)

# Selektor


def Red(W):
    return W[0]


def Green(W):
    return W[1]


def Blue(W):
    return W[2]

# Operator


def Mix(W1, W2):
    r_mixed = (Red(W1) + Red(W2)) // 2  # Pembagian integer
    g_mixed = (Green(W1) + Green(W2)) // 2
    b_mixed = (Blue(W1) + Blue(W2)) // 2
    return MakeWarna(r_mixed, g_mixed, b_mixed)

# Predikat


def IsGray(W):
    return Red(W) == Green(W) == Blue(W)

# Fungsi Analisis


def DominantChannel(W):
    if IsGray(W):
        return "Abu-abu"
    elif Red(W) >= Green(W) and Red(W) >= Blue(W):
        return "Dominan Merah"
    elif Green(W) >= Blue(W):
        return "Dominan Hijau"
    else:
        return "Dominan Biru"

# Fungsi validasi input
def is_valid_rgb(r, g, b):
    return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

# Fungsi untuk memproses dan menampilkan hasil
def process(r1, g1, b1, r2, g2, b2):
    # Validasi input
    if not (is_valid_rgb(r1, g1, b1) and is_valid_rgb(r2, g2, b2)):
        print("Input tidak valid")
        return
    
    # Membuat objek warna
    warna1 = MakeWarna(r1, g1, b1)
    warna2 = MakeWarna(r2, g2, b2)
    
    # Mencampur warna
    warna_campuran = Mix(warna1, warna2)
    
    # Menampilkan hasil RGB
    print(f"{Red(warna_campuran)} {Green(warna_campuran)} {Blue(warna_campuran)}")
    
    # Menganalisis dan menampilkan dominansi
    analisis = DominantChannel(warna_campuran)
    print(analisis)


# JANGAN DIHAPUS
data = list(map(int, input().split()))
process(data[0], data[1], data[2], data[3], data[4], data[5])
