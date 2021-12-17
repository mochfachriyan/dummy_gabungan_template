from app_pembelians import response
from app_pembelians.entry import barang
from app_pembelians.entry.barang import model_barang
from app_pembelians.entry.suplier import controller_suplier, model_suplier
from flask import jsonify

# ---------------------------MENAMPILKAN SEMUA DATA BARANG--------------------------------#
def barangDataJson(): 
  try:
    barang = model_barang.barang.query.all() # ini kalau di Oracle seperti Select * from barang
    data = formatArray(barang) 
    return response.success(data, "success")
  except Exception as e: 
    print(e)

def barangData(): # deff adalah function
  # select * FROM
  barang = model_barang.barang.query.all() # ini ksuplier.query.all() # ini kalau di Oracle macem Select * from suplier
  return barang # ngereturn dari response.py kelas succes
   

    
# ---------------------------MENAMPILKAN DETAIL DATA BARANG--------------------------------#    
# def barangDataDetail(id): 
#   try:
#     suplier = model_suplier.suplier.query.filter_by(id_suplier=id) # ini kalau di Oracle seperti Select * from barang
#     data = formatArray(suplier)  
    
#     if not barang: 
#       return response.badRequest([], 'Data Barang tidak ada !!')
    
#     # suplier = controller_suplier.suplierDataDetail(id_suplier)
#     return response.success(data, "success")
#   except Exception as e: 
#     print(e)
    





# function untuk format array nya data barang
def formatArray(datas):
  array = []
  for i in datas:
    array.append(singleObject(i)) # INGAT pelajaran di w3school tentang Lists, Tuples, Sets, DIctionaries ? nah ini method yang ada di Lists
  # menambahkan di arraynya
  # membuat Function singleObject dulu
  return array

# function format untuk menampilkan semua data siplier
def singleObject(data):
  data={
    'id_barang':data.id_barang,
    'nama_barang':data.nama_barang,
    'harga':data.harga,
    'id_suplier':data.id_suplier,
    'keterangan':data.keterangan
  }
  return data




        

