from app_pembelians.entry import pembelian
from app_pembelians.entry.pembelian import model_pembelian
from flask import jsonify

def pembelianData(): # deff adalah function
  # select * FROM
  pembelian = model_pembelian.pembelian.query.all() # ini kalau di Oracle macem Select * from suplier
  data = formatArray(pembelian) #
  return jsonify(data) # ngereturn dari response.py kelas succes
  
# ---------------------------------DATA USER------------------------------------------#
def userData(): 
  user = model_pembelian.user.query.all()
  dataUser = user
  return jsonify(dataUser) # ngereturn dari response.py kelas
# ------------------------------------------------------------------------------------#
    

# function untuk format array nya Dosen
def formatArray(datas):
  array = []
  for i in datas:
    array.append(singleObject(i)) # INGAT pelajaran di w3school tentang Lists, Tuples, Sets, DIctionaries ? nah ini method yang ada di Lists
  # menambahkan di arraynya
  # membuat Function singleDosen dulu
  return array


# function format untuk menampilkan Dosen
def singleObject(data):
  data={
  'id_pembelian':data.id_pembelian,
  'id_user':data.id_user,
  'id_barang':data.id_barang,
  'tanggal':data.tanggal,
  'keterangan':data.keterangan
  }
  return data