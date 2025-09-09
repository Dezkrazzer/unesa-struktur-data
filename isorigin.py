# membuat fungsi untuk mengecek apakah sebuah titik adalah origin (0, 0)
def is_origin(x, y):
    return x == 0 and y == 0
# contoh penggunaan
titik1 = (1, 0)
print(is_origin(*titik1))  # Output: True