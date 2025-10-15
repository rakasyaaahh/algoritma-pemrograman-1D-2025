pin_benar = "25113"

for i in range(3):
    pin = input("Masukkan PIN (5 digit angka): ")
    if not (pin.isdigit() and len(pin) == 5):
        print("PIN salah, coba lagi.")
        if i == 2:
            print("Akses ditolak, kartu diblokir")
        continue
    if pin == pin_benar:
        print("PIN benar, akses diterima")
        break
    elif i == 2:
        print("Akses ditolak, kartu diblokir")
    else:
        print("PIN salah, coba lagi")
