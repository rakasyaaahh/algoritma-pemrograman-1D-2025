jumlah_baris = int(input("Masukkan jumlah baris lampu: "))

for i in range(jumlah_baris):
    lampu = int(input(f"Masukkan jumlah lampu di baris {i+1}: "))
    
    for j in range(lampu):
        if (j + 1) % 3 == 0:
            print(f"Lampu ke-{j+1} pada baris {i+1} rusak.")
        else:
            print(f"Lampu ke-{j+1} pada baris {i+1} menyala.")
    
    if i == jumlah_baris - 1:
        print("Periksa sambungan daya utama.")
