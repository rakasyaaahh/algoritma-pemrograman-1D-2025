while True:
    nama = input("Nama pembeli: ")
    while not nama.replace(" ", "").isalpha():
        print("Nama hanya boleh huruf dan spasi.")
        nama = input("Nama pembeli: ")

    total = 0
    daftar = ""

    while True:
        barang = input("Nama barang (ketik 'selesai'): ")
        if barang == "selesai":
            break
        while barang.isdigit() or barang.strip() == "":
            print("Nama barang tidak boleh hanya angka atau kosong.")
            barang = input("Nama barang (ketik 'selesai'): ")

        while True:
            harga_input = input("Harga barang: ")
            if harga_input.isdigit():
                harga = int(harga_input)
                break
            else:
                print("Harga harus berupa angka.")

        total += harga
        daftar += f"- {barang}: {harga}\n"

    print("\n== Struk Pembelian IndoMei ==")
    print("Nama Pembeli:", nama)
    print(daftar, end="")
    print("Total Harga:", total)
    print("Terima kasih telah berbelanja di IndoMei.\n")

    if input("Ada pembeli berikutnya? (y/n): ") != "y":
        break
