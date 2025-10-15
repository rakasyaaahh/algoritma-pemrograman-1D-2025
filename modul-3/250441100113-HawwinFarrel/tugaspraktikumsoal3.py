kalimat = input("Masukkan sebuah kalimat: ")

vokal = "aiueoAIUEO"
jumlah_vokal = 0
jumlah_konsonan = 0

for huruf in kalimat:
    if huruf.isalpha(): #memeriksa semua karakter dalam string adalah alfabet (huruf)
        if huruf in vokal:
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1

jumlah_kata = len(kalimat.split()) #menghitung kata dengan per spasi #len mengembalikan jumlah item

print("Jumlah huruf vokal:", jumlah_vokal)
print("Jumlah huruf konsonan:", jumlah_konsonan)
print("Jumlah kata:", jumlah_kata)

