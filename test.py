# The Distance between Two points

'''
    Deskription:
    Kris dan Noelle akan melakukan perjalanan antariksa dari planet A menuju planet B menggunakan pesawat antariksa yang dilengkapi fitur-fitur canggih. Namun di hari mereka akan melakukan perjalanan tersebut, tiba-tiba saja matahari galaksi mereka mengeluarkan ledakan sinar-gamma dalam jumlah yang tak terduga. Hal ini membuat teknologi canggih yang akan mengcompute jarak perjalanan mereka ke planet B tidak stabil, sehingga tidak memungkinkan untuk menggunakan teknologi tersebut karena unreliable.
    Setelah berjam-jam mencari solusi alternatif, Noelle menemukan sebuah artefak misterius di basementnya: SEBUAH KOMPUTER LAWAS! Komputer ini masih menggunakan bit 0 dan 1 untuk melakukan komputasi, sehingga meski inefisien, tapi resistan terhadap gangguan sinar-gamma. Sayangnya, Noelle maupun Kris tidak bisa memrogram dalam bahasa lawas tersebut.
    Beruntungnya, mereka memiliki teman yang baik, yaitu ANDA, seorang sejarawan komputer. Bisakah kamu membantu mereka?

    Notes:
    Gunakan float(operand, 5) untuk membulatkan hasil ke 5 digit belakang.

    Input Format:
    DBT(tdp1, tdp2)

    Constraints:
    tdp1, tdp2: Point
    Jarak antara titik tdp1 dan tdp2 pasti ada

    Output Format:
    float

    Sample Input 0:
    DBT(Make3DPoint(0.0, 2.0, 5.0), Make3DPoint(7.0, 2.0, 3.0))

    Sample Output 0:
    7.28011

    Sample Input 1:
    DBT(Make3DPoint(1.5, -2.5, 3.5), Make3DPoint(-4.5, 5.5, -6.5))

    Sample Output 1:
    14.14214
'''

type ThreeDPoint = tuple[float, float, float]

def Make3DPoint(x: float, y: float, z: float) -> ThreeDPoint:
    return (x, y, z)

def getAbsis(p: ThreeDPoint) -> float:
    return p[0]

def getOrdinat(p: ThreeDPoint) -> float:
    return p[1]

def getApotema(p: ThreeDPoint) -> float:
    return p[2]

def DBT(tdp1: ThreeDPoint, tdp2: ThreeDPoint) -> float:
    # Mendapatkan koordinat dari titik pertama
    x1 = getAbsis(tdp1)
    y1 = getOrdinat(tdp1)
    z1 = getApotema(tdp1)
    
    # Mendapatkan koordinat dari titik kedua
    x2 = getAbsis(tdp2)
    y2 = getOrdinat(tdp2)
    z2 = getApotema(tdp2)
    
    # Menghitung jarak menggunakan rumus Euclidean 3D
    # jarak = √[(x2-x1)² + (y2-y1)² + (z2-z1)²]
    jarak = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
    
    # Membulatkan hasil ke 5 digit belakang koma
    return round(jarak, 5)


print(DBT(Make3DPoint(0.0, 2.0, 5.0), Make3DPoint(7.0, 2.0, 3.0)))
print(DBT(Make3DPoint(1.5, -2.5, 3.5), Make3DPoint(-4.5, 5.5, -6.5)))