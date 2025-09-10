# Mean Olympic

# Misal terdapat angka 8, 12, 10, 20
# Maka angka 8 dan 20 dihilangkan
# Rata-rata dari 12 dan 10 adalah 11
# Bilanganya numerik dan real

def max2 (a,b) : # fungsi untuk mencari nilai maksimum dari dua bilangan
    return (a  + b + abs(a-b)) / 2
def min2 (a,b) : # fungsi untuk mencari nilai minimum dari dua bilangan
    return (a  + b - abs(a-b)) / 2
def max4 (i,j,k,l) : 
    return max2(max2(i,j),max2(k,l))
def min4 (i,j,k,l) : 
    return min2(min2(i,j),min2(k,l))

def meanolymp (u,v,w,x) :
    return (u + v + w + x - max4(u,v,w,x) - min4(u,v,w,x)) / 2

# contoh penggunaan
print(meanolymp(8,12,10,20))  # Output: 11.0