
def jumlahkan_semua(daftar_angka):
    akumulasi = 0
    for nilai in daftar_angka:
        akumulasi += nilai
    return akumulasi

def uji_pembagian(daftar_angka):
    total_keseluruhan = jumlahkan_semua(daftar_angka)
    separuh = total_keseluruhan / 2
    penjumlahan_sementara = 0

    for i in range(len(daftar_angka)):
        penjumlahan_sementara += daftar_angka[i]
        if penjumlahan_sementara == separuh:
            return True
    return False

def tampilkan_daftar(daftar_angka):
    if not daftar_angka:
        print("Daftar angka masih kosong.")
    else:
        print("Daftar angka saat ini:", daftar_angka)

def tambahkan_data(daftar_angka):
    try:
        masukan = input("Masukkan angka, dispisah dengan spasi: ")
        masukan = masukan.replace(",", " ").split()
        for item in masukan:
            if item.isdigit():
                daftar_angka.append(int(item))
                print(f"Angka {item} berhasil ditambahkan.")
            else:
                print(f"'{item}' bukan angka, di-skip.")
    except ValueError:
        print("Input tidak valid!")

def ubah_daftar(daftar_angka):
    tampilkan_daftar(daftar_angka)
    if not daftar_angka:
        return
        
    try:
        indeks_pilihan = int(input("Masukkan indeks angka yang ingin diubah: "))
        if 0 <= indeks_pilihan < len(daftar_angka):
            angka_baru = input("Masukkan angka baru: ")
            if angka_baru.isdigit():
                daftar_angka[indeks_pilihan] = int(angka_baru)
                print("Data berhasil diubah.")
            else:
                print("Input harus berupa angka!")
        else:
            print("Indeks tidak ditemukan.")
    except ValueError:
        print("Input tidak valid!")

def hapus_daftar(daftar_angka):
    tampilkan_daftar(daftar_angka)
    if not daftar_angka:
        return
        
    try:
        indeks_pilihan = int(input("Masukkan indeks angka yang ingin dihapus: "))
        if 0 <= indeks_pilihan < len(daftar_angka):
            daftar_angka.pop(indeks_pilihan)
            print("Data berhasil dihapus.")
        else:
            print("Indeks tidak ditemukan.")
    except ValueError:
        print("Input tidak valid!")

def tampilan_menu():
    koleksi_angka = []
    while True:
        print("\n== PROGRAM ==")
        print("1. Tambah Angka")
        print("2. Tampilkan Angka")
        print("3. Ubah Angka")
        print("4. Hapus Angka")
        print("5. Cek Pembagian Dua Bagian Sama Besar")
        print("6. Keluar")
        
        pilihan_pengguna = input("Pilih menu: ")

        if pilihan_pengguna == "1":
            tambahkan_data(koleksi_angka)
        elif pilihan_pengguna == "2":
            tampilkan_daftar(koleksi_angka)
        elif pilihan_pengguna == "3":
            ubah_daftar(koleksi_angka)
        elif pilihan_pengguna == "4":
            hapus_daftar(koleksi_angka)
        elif pilihan_pengguna == "5":
            tampilkan_daftar(koleksi_angka)
            if uji_pembagian(koleksi_angka):
                print("True, deretan dapat dibagi menjadi dua bagian dengan jumlah yang sama")
            else:
                print("False, deretan tidak dapat dibagi menjadi dua bagian dengan jumlah yang sama")
        elif pilihan_pengguna == "6":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak tersedia")

tampilan_menu()