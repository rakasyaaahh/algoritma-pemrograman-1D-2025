def hitung_gaji_bersih(nama, jabatan, gaji_pokok):
    pajak = 0.05 * gaji_pokok
    if jabatan == "manager":
        tunjangan = 0.10 * gaji_pokok
    elif jabatan == "staff":
        tunjangan = 0.05 * gaji_pokok
    gaji_bersih = (gaji_pokok - pajak) + tunjangan

    print("=== Rincian perhitungan gaji ===")
    print(f"Nama Karyawan : {nama}")
    print(f"Jabatan      : {jabatan}")
    print(f"Gaji Pokok   : Rp{gaji_pokok}")
    print(f"PPh (5%)     : Rp{pajak}")
    print(f"Tunjangan    : Rp{tunjangan}")
    print(f"Gaji Bersih  : Rp{gaji_bersih}")

while True:
    while True:
        nama = input("Masukkan nama karyawan: ")
        if not nama.replace(" ", "").isalpha():
            print("Nama harus berupa huruf saja!")
            continue
        break
    

    while True:
        jabatan = input("Masukkan jabatan karyawan (maanager/staff): ").lower()
        if not jabatan.isalpha():
            print("jabatan hanya boleh huruf!")
            continue
        if jabatan not in ["manager", "staff"]:
            print("jabatan harus diisi dengan 'manager' atau 'staff'!")
            continue
        break
    
    while True:
        try:
            gaji_pokok = int(input("Masukkan gaji pokok: "))
            if gaji_pokok < 0:
                print ("gaji tidak boleh minus")
                continue  
        except ValueError:
            print("Gaji pokok harus angka yaa!")
        break

    hitung_gaji_bersih(nama, jabatan, gaji_pokok)
    
    lagi = input("Apakah ingin menghitung gaji karyawan lain? (y/n): ").lower()
    if lagi != 'y':
        break
