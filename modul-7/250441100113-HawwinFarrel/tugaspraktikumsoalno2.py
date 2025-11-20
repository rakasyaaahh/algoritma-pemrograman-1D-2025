inventaris = {}

def tampilkan_menu():
    print("\n=== INVENTARIS GUDANG ===")
    print("1. Tampilkan Semua Barang")
    print("2. Cari Barang Berdasarkan ID")
    print("3. Tambah Barang Baru")
    print("4. Perbarui Stok Barang")
    print("5. Hapus Barang")
    print("6. Keluar")

def tampilkan_semua():
    if not inventaris:
        print("Inventaris kosong.")
        return
    else:
        print("\nDaftar Barang:")
    for id_barang, data in inventaris.items():
        nama, harga, stok = data
        print(f"ID: {id_barang} | Nama: {nama} | Harga: Rp{harga} | Stok: {stok}")

def cari_barang():
    if not inventaris:
        print("Belum ada barang yang ditambahkan")
        return
    id_cari = input("Masukkan ID barang: ").strip()
    if id_cari not in inventaris:
        print("Barang tidak ditemukan.")
        return
    nama, harga, stok = inventaris[id_cari]
    print(f"\nDitemukan: ID={id_cari}, Nama={nama}, Harga=Rp{harga}, Stok={stok}")

def tambah_barang():
    id_baru = input("ID barang: ").strip()
    if id_baru in inventaris:
        print("ID sudah ada. Gunakan ID lain.")
        return
    nama = input("Nama barang: ").strip()
    harga = float(input("Harga: "))
    stok = int(input("Stok awal: "))
    if stok < 0:
        print("Stok tidak boleh negatif.")
        return
    inventaris[id_baru] = [nama, harga, stok]
    print(f"Barang '{nama}' berhasil ditambahkan.")

def perbarui_stok():
    if not inventaris:
        print("Tambah barang terkebih dahulu")
        return
    id_update = input("ID barang yang ingin diperbarui stoknya: ").strip()
    if id_update not in inventaris:
        print("Barang tidak ditemukan.")
        return
    else:
        stok_baru = int(input("Stok baru: "))
    if stok_baru < 0:
        print("Stok tidak boleh negatif.")
        return
    inventaris[id_update][2] = stok_baru
    print("Stok berhasil diperbarui.")

def hapus_barang():
    if not inventaris:
        print("Belum ada barang yang di tambahkan")
        return
    id_hapus = input("ID barang yang ingin dihapus: ").strip()
    if id_hapus not in inventaris:
        print("Barang tidak ditemukan.")
        return
    del inventaris[id_hapus]
    print("Barang berhasil dihapus.")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-6): ").strip()

    if pilihan == '1':
        tampilkan_semua()
    elif pilihan == '2':
        cari_barang()
    elif pilihan == '3':
        tambah_barang()
    elif pilihan == '4':
        perbarui_stok()
    elif pilihan == '5':
        hapus_barang()
    elif pilihan == '6':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")