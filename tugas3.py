def hitung_total(barang) : 
  total_harga = 0

  for x in barang :
    sub_total = (x['jumlah']*x['harga'])
    total_harga = total_harga + sub_total
  
  return total_harga

barang = [
  {
    'nama' : 'jilbab',
    'jumlah' : 3,
    'harga' : 20000
  },
  {
    'nama' : 'ciput',
    'jumlah' : 3,
    'harga' : 5000
  },
]

print(hitung_total(barang))


