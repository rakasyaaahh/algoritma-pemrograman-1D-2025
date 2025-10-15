n = int(input("Masukkan n: "))
for angka in range(2, n):
    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            break
    else:
        print(angka)
