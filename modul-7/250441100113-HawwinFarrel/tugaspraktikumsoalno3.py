# Dictionary kupon
kupon = {
    "SHOPEE10": 10,
    "TOKOPEDIA20": 20,
    "TIKTOK30": 30
}

def tampilkan_kupon():
    print("\n--- KUPON YANG TERSEDIA ---")
    if not kupon:
        print("Tidak ada kupon tersedia.")
    else:
        for kode, diskon in kupon.items():
            print(f"{kode} → {diskon}% diskon")

def input_barang():
    keranjang = {}
    print("\n--- INPUT BARANG ---")
    while True:
        nama_barang = input("Masukkan nama barang (atau ketik 'selesai' untuk lanjut): ").strip()
        if nama_barang.lower() == 'selesai':
            break

        try:
            harga_barang = float(input(f"Masukkan harga satuan untuk '{nama_barang}': Rp "))
            if harga_barang < 0:
                print("Harga tidak boleh negatif. Silakan masukkan ulang.")
                continue
        except ValueError:
            print("Input harga tidak valid. Harap masukkan angka.")
            continue

        try:
            jumlah = int(input(f"Masukkan jumlah {nama_barang}: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0. Silakan masukkan ulang.")
                continue
        except ValueError:
            print("Input jumlah tidak valid. Harap masukkan angka bulat.")
            continue

        keranjang[nama_barang] = [harga_barang, jumlah]
        print(f"{jumlah} {nama_barang}(s) dengan harga satuan Rp {harga_barang:,.0f} ditambahkan ke keranjang.")
    
    return keranjang

def hitung_total_belanja(keranjang):
    total = 0
    for barang, (harga_satuan, jumlah) in keranjang.items():
        subtotal = harga_satuan * jumlah
        total += subtotal
    return total

def cetak_rincian_belanja(keranjang):
    total = 0
    print("\n--- RINCIAN BELANJA ---")
    for barang, (harga_satuan, jumlah) in keranjang.items():
        subtotal = harga_satuan * jumlah
        total += subtotal
        print(f"{jumlah} {barang} x Rp {harga_satuan:,.0f} = Rp {subtotal:,.0f}")
    print(f"\nTotal Belanja: Rp {total:,.0f}")
    return total

def proses_kupon(keranjang, total_belanja):
    if not kupon:
        print("\nTidak ada kupon tersedia untuk digunakan.")
        print(f"Total Belanja: Rp {total_belanja:,}")
        return total_belanja

    gunakan_kupon = input("\nApakah Anda ingin menggunakan kupon? (y/n): ").strip().lower()
    if gunakan_kupon != 'y':
        print("\nTransaksi selesai tanpa menggunakan kupon.")
        print(f"Total Belanja: Rp {total_belanja:,}")
        return total_belanja

    tampilkan_kupon()
    kode_input = input("Masukkan kode kupon: ").strip().upper()

    if kode_input not in kupon:
        print("\nKupon tidak valid atau sudah digunakan.")
        print(f"Total yang harus dibayar: Rp {total_belanja:,}")
        return total_belanja

    cetak_rincian_belanja(keranjang)

    diskon_persen = kupon[kode_input]
    potongan = total_belanja * (diskon_persen / 100)
    total_akhir = total_belanja - potongan

    print(f"\nKupon {kode_input} berhasil digunakan!")
    print(f"Potongan: Rp {potongan:,}")
    print(f"Total yang harus dibayar: Rp {total_akhir:,}")

    del kupon[kode_input]
    print(f"Kupon {kode_input} telah dihapus dan tidak bisa dipakai lagi.")

    return total_akhir

def proses_transaksi():
    keranjang = input_barang()
    if not keranjang:
        print("\nKeranjang belanja kosong. Transaksi dibatalkan.")
        return

    total_belanja = hitung_total_belanja(keranjang)
    total_akhir = proses_kupon(keranjang, total_belanja)


while True:
    print("\n=== PROGRAM KASIR SEDERHANA ===")
    print("1. Tampilkan kupon")
    print("2. Proses transaksi baru")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ").strip()

    if pilihan == "1":
        tampilkan_kupon()
    elif pilihan == "2":
        proses_transaksi()
    elif pilihan == "3":
        print("\nTerima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
