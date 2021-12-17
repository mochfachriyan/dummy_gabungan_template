from app_pembelians.entry import suplier
from app_pembelians import response
from app_pembelians.entry.barang import controller_barang, model_barang
from app_pembelians.entry.suplier import model_suplier
from flask import jsonify, request, redirect, url_for, flash
from app_pembelians import db


# -------------------------------- MENAMPILKAN SEMUA DATA SUPLIER --------------------------------#
def suplierData(): # deff adalah function
  # select * FROM
  suplier = model_suplier.suplier.query.all() # ini kalau di Oracle macem Select * from suplier
  return suplier # ngereturn dari response.py kelas succes
 
# -------------------------------- MENAMPILKAN DETAIL DATA SUPLIER --------------------------------#
def suplierDataDetail(id_suplier):
  suplier = model_suplier.suplier.query.filter_by(id_suplier=id_suplier)
  data = formatArray(suplier) #
  return jsonify(data) # ngereturn dari response.py kelas succes

# -------------------------------- TAMBAH DATA SUPLIER --------------------------------#
def tambahSuplier():
  nama = request.form['nama']
  no_telp = request.form['no_tlp']
  alamat = request.form['alamat']
  suplier = model_suplier.suplier(nama,no_telp,alamat)
  db.session.add(suplier)
  db.session.commit()   
  flash('You have successfully created a new suplier')
  return redirect(url_for('suplier.suplier'))
  
# -------------------------------- EDIT DATA SUPLIER --------------------------------#
def editSuplier():
  suplier = model_suplier.suplier.query.get(request.form.get('id_suplier'))
  suplier.nama_suplier = request.form['nama']
  suplier.no_telp = request.form['no_tlp']
  suplier.alamat = request.form['alamat']

  db.session.commit()
  flash("Employee Updated Successfully")
  return redirect(url_for('suplier.suplier'))
  
# -------------------------------- HAPUS DATA SUPLIER --------------------------------#
def hapusSuplier(id_suplier):
  suplier = model_suplier.suplier.query.get(id_suplier)
  db.session.delete(suplier)
  db.session.commit()
  flash("Employee Deleted Successfully")
  return redirect(url_for('suplier.suplier'))


    



# function format array
def formatArray(datas):
  array = []
  for i in datas:
    array.append(singleObject(i)) # INGAT pelajaran di w3school tentang Lists, Tuples, Sets, DIctionaries ? nah ini method yang ada di Lists
  # menambahkan di arraynya
  # membuat Function singleDosen dulu
  return array

# function format suplier
def singleObject(data):
  data={
    'id_suplier':data.id_suplier,
    'nama_suplier':data.nama_suplier,
    'no_telp':data.no_telp,
    'alamat':data.alamat
  }
  return data
