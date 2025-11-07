# #list
# list = [1, 2, 3, 'cuuyy']
# print(list)

# #Menambah list
# list = [1, 2, 'jokowi', 'prabowo']
# list.append (3)
# list.append ('megawati')
# print(list)

# #Menghapus list
# list = [1, 2, 3, 4, 'apel']
# # list.remove ('apel')
# del list [4]
# print(list)

# #Operasi dasar pada list
# #Menghitung panjang pada list
# angka = [3,5,7,11,33]
# print("Panjang list adalah :", len(angka))

# #Menggabungkan dua list
# list1 = [1,2,3,4]
# list2 = [2,3,4,5]
# print (list1 + list2)

# #Mengulang list
# list =['gibran']
# print(list* 10)

# #Cek elemen yang ada di list 
# list = [1,2,3,4,'kecubung']
# print('semangka' in list)
# print (2 in list)

# #Perulangan dalam list (for)
# for y in[1,2,3,4,5]:
#     print (y)

# #Perulangan dalam list (while)
# # angka = [1,2,3,4,5,6]

# # i = 0
# # while i < len(angka):
# #     print(angka[i], end= ' ')
# #     i += 1

# #===============TUPLE============#
# # mengakses nilai pada tulpe
# nama = ('yanti','yanto','yareu')
# print(nama[2], end = ' ')

# #menambah 
# buah = ('mangga','apel','durian')
# buahbaru = buah + ('anggur',)
# print(buahbaru)

# #menghapus nilai pada tuple
# angka1=(1,2,3)
# buah = ('mangga','apel','durian')
# del buah
# print(angka1)

namamahasiswa = ('santoso','rudi','mas-amba')
mahasiswabaru = namamahasiswa + ('bambang','yantooo',)
print (mahasiswabaru, "Mahasiswa sekarang berjumlah", len(mahasiswabaru))
