# baca = open('pertemuan4.txt','w')
# # print(baca.read()) # mencetak seluruh isi file pertemuan4.txt
# # print(baca.read(10))
# # print(baca.readline())
# # print(baca.readline())
# # for x in baca:
# #     print(x)

# baca.write('Hallo, Nama saya Nadira Alifia Ionendri. Hobi saya membaca')
# baca.close()

# import os
# if os.path.exists('pertemuan4.txt'):
#     os.remove('pertemuan4.txt')
# else : 
#     print('file tidak ditemukan')

# menghapus folder
# import os
# import shutil
# shutil.rmtree('D:\other file\Mini Bootcamp\WIT Python & Cyber Security\delete')

# import os
# os.rmdir('tes')

# hop = open('hop.txt')
# # for x in hop:
#     # print(x)
# # print(hop.readline())
# print(hop.readline()[0].len())
# for x in hop:
#     a = x.len()
#     print(a)

# def jumlah_kata(text) : 
#   total_kata = 0

#   for x in text :
#     total_per_baris =len(x)
#     total_kata = total_kata + total_per_baris
  
#   return total_kata

# text = open('hop.txt')

# print(jumlah_kata(text))

# def hitung_jumlah_kata(nama_file):
#     try:
#         with open(nama_file, 'r') as file :
#             isi_file = file.read()
#             jumlah_kata = len(isi_file.split())
#             return jumlah_kata
#     except:
#         print('file tidak ditemukan')
#         return 0
# nama_file = 'hop.txt'
# jumlah_kata = hitung_jumlah_kata(nama_file)
# print('jumlah kata dalam file : ', jumlah_kata)

def hitung_jumlah_kata(nama_file):
    try:
        with open(nama_file, 'r') as file:
            isi_file = file.read()
            jumlah_kata = len(isi_file.split())
            return jumlah_kata
    except :
        print("File tidak ditemukan.")
        return 0

nama_file = 'hop.txt'
jumlah_kata = hitung_jumlah_kata(nama_file)
print("Jumlah kata dalam file:", jumlah_kata)


