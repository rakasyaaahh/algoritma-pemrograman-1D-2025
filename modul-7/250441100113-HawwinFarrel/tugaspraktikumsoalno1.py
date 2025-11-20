kontak = {}

def tampilkan_menu():
    print("\n=== CONTACT BOOK ===")
    print("1. Tampilkan Semua Kontak")
    print("2. Cari Kontak")
    print("3. Tambah Kontak Baru")
    print("4. Perbarui Email Kontak")
    print("5. Hapus Kontak")
    print("6. Keluar")

def tampilkan_semua_kontak():
    if not kontak:
        print("\nKontak kosong.")
    else:
        print("\nDaftar Kontak:")
        for nama, info in kontak.items():
            print(f"Nama: {nama} | Nomor: {info[0]} | Email: {info[1]}")

def cari_kontak():
    if not kontak:
        print("kontak kosong, tambah kontak terlebih dahulu")
        return
    nama = input("Masukkan nama kontak yang dicari: ")
    if nama in kontak:
        info = kontak[nama]
        print(f"\nDitemukan: {nama} | Nomor: {info[0]} | Email: {info[1]}")
    else:
        print(f"\nKontak '{nama}' tidak ditemukan.")

def tambah_kontak():
    while True:
        nama = input("Masukkan nama kontak: ")
        if nama in kontak:
            print(f"\nKontak '{nama}' sudah ada")
        else:
            while True:
                nomor = input("Masukkan nomor telepon: ").strip()
                if not nomor.isdigit():
                    print("Masukkan nomor hanya angka saja")
                else:
                    break  
            email = input("Masukkan email: ").strip()
            kontak[nama] = [nomor, email]
            print(f"\nKontak '{nama}' berhasil ditambahkan")
            lanjut = input("Tambahkan kontak lagi? (y/n): ").strip().lower()
        if lanjut != 'y':
            break

def perbarui_email():
    if not kontak:
        print("Tambahkan kontak terlebih dahulu")
        return
    nama = input("Masukkan nama kontak yang ingin diperbarui emailnya: ").strip()
    if nama in kontak:
        email_baru = input("Masukkan email baru: ").strip()
        kontak[nama][1] = email_baru
        print(f"\nEmail {nama} berhasil diperbarui!")
    else:
        print(f"\nKontak '{nama}' tidak ditemukan.")

def hapus_kontak():
    if not kontak:
        print("Tambahkan kontak terlebih dahulu")
    else:
        nama = input("Masukkan nama kontak yang ingin dihapus: ").strip()
        if nama in kontak:
            del kontak[nama]
            print(f"\nKontak '{nama}' berhasil dihapus!")
        else:
            print(f"\nKontak '{nama}' tidak ditemukan.")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-6): ").strip()

    if pilihan == "1":
        tampilkan_semua_kontak()
    elif pilihan == "2":
        cari_kontak()
    elif pilihan == "3":
        tambah_kontak()
    elif pilihan == "4":
        perbarui_email()
    elif pilihan == "5":
        hapus_kontak()
    elif pilihan == "6":
        print("\nTerima kasih")
        break
    else:
        print("\nPilihan tidak valid. Silakan pilih 1-6.")