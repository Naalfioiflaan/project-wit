# def bmi(tinggi_badan, berat_badan):
#     c = berat_badan /(tinggi_badan**2)
#     return c
# hasil = bmi(50,160)
# print(hasil)

# menggunakan list sebagai argumen
# def sapa(nama):
#     for i in nama:
#         print('Hallo',i)
# sapa(['tasia','zulfa','dea'])

# fungsi rekursif
# def faktorial(n):
#     # kasus dasar
#     if n <= 1 :
#         return 1
#     # kasus rekursif
#     else :
#         return n * faktorial(n-1)

# print(faktorial(5)) 
#5*4*3*2*1

# def hitung_jumlah(n):
#     # kasus dasar
#     if n == 1 :
#         return n
#     # kasus rekursif
#     else :
#        return n + hitung_jumlah(n-1)
# print(hitung_jumlah(5))

# fungsi rekursif pada perulangan
# def faktorial_while(n):
#     hasil = 1
#     while n > 0 :
#         hasil = hasil*n
#         n = n-1
#     return hasil
# print(faktorial_while(4))

# fungsi
# def kali_dua(a):
#     return a*2
# print(kali_dua(2))

# lambda ekspression
# kali_dua = lambda a : a*2
# print(kali_dua(2))

# def lipat_ganda(x):
#     return x*2
# list_awal = [10,20,30]
# list_ganda = list(map(lipat_ganda,list_awal))
# print(f'list_awal:{list_awal}')
# print(f'list_akhir:{list_ganda}')

# def tambah(a,b):
#     c = a+b
#     return c
# print(tambah(5,6))

# tambah = lambda a,b : a+b
# print(tambah(5,6))

# number = [1,2,3,4,5]
# filter_number = list(filter(lambda x : x%2 = 0, number))
# print(filter_number)

# sayuran = ['kangkung','bayam','buncis','brokoli','kol','sawi','kacang panjang']
# print(sayuran[1])
# print(sayuran[-1])
# print(sayuran[1:3])
# if 'buncis' in sayuran :
#     print('buncis merupakan sayur')
# sayuran[1:3] = ['sawi','buncis']
# print(sayuran)
# sayuran = ['kangkung']
# sayuran.append('kol')
# print(sayuran)

# makanan = ['nasi goreng','bakso', 'sate', 'ayam']
# print(makanan.index('ayam'))
# print(makanan[1:4])
# makanan.sort(reverse=True)
# print(makanan)

# dict_harga = {'pensil':1000, 'pena':2000, 'penghapus': 1500}
# # print(dict_harga['pensil'])
# print(dict_harga.keys())

makanan = {'bakso' : 10000, 'sate': 5000, 'soto': 8000}
item_list = makanan.items()
for key, value in item_list :
    print(key +"=" + str(value))