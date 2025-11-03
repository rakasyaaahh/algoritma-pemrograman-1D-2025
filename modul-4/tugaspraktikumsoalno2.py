total_jam_lembur = 0
total_bonus_malam = 0
total_gaji = 0

for hari in range(1, 8):
    while True:
        try:
            jam = int(input(f"Masukkan jam lembur hari ke-{hari}: "))
            shift = input(f"Apakah shift malam hari ke-{hari}? (y/n): ").lower()
            if jam < 0 or jam > 24 or shift not in ['y', 'n']:
                print("Input tidak valid, coba lagi.")
                continue
            break
        except:
            print("Input tidak valid, coba lagi.")

    if jam > 8:
        print("Lembur melebihi batas, tidak dihitung.")
        jam = 0
 
    if 1 <= jam <= 3:
        tambah_lembur = jam * 25000
    elif jam == 4:
        tambah_lembur = 100000
    elif jam == 6:
        tambah_lembur = 200000
    elif jam == 8:
        tambah_lembur = 300000
    else:
        tambah_lembur = 0

    if shift == "y":
        bonus_malam = 50000
    else:
        bonus_malam = 0

    total_jam_lembur += jam
    total_bonus_malam += bonus_malam
    total_gaji += 100000 + tambah_lembur + bonus_malam

print(f"\nTotal jam lembur seminggu: {total_jam_lembur}")
print(f"Total bonus shift malam: Rp{total_bonus_malam}")
print(f"Total gaji selama seminggu: Rp{total_gaji}")

