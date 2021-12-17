from flask.helpers import flash
from app_karyawans import db
from app_karyawans.entry.gaji import model_gaji
from app_karyawans.entry.karyawan import model_karyawan, response
from app_karyawans.entry.gaji import controller_gaji   # untuk import gaji per nik
from flask import request
import datetime

# def tabel_gaji_get_nik(nik):  # Simpan dulu
#   # select * FROM
#   v_gaji_nik = gajiModel.zzz_dummy_salary.query.filter_by(nik = nik).all()
#   data = formatArray(v_gaji_nik) #
#   return jsonify(data) # ngereturn dari response.py kelas succes

def tabelKaryawanGetTampilan(): # deff adalah function
  # select * FROM
  v_all_karyawan = model_karyawan.zzz_dummy_karyawan.query.all() # ini kalau di Oracle macem Select * from Dosen
  # return response.success(data, "success") # ngereturn dari response.py kelas succes
  return v_all_karyawan


def insertKaryawanTampilan():
  try:
    nik = request.form.get('nik')         # Ini yang bikin lama, gara2 lupa konsep dictionary. Kebingungan syntax untuk manggil nama kolomnya
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    golongan = request.form.get('golongan')
    tanggal_kerja = request.form.get('tgl_kerja')
    status_aktif = request.form.get('status_aktif')
    # tanggal_input = request.form.get('tgl_input')
    # v_tgl_kerja = datetime.datetime.strptime(row[4], "%m/%d/%Y %H:%M")
    sysdate = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    
    v_karyawan = model_karyawan.zzz_dummy_karyawan(nik=nik, first_name=first_name, last_name=last_name, golongan=golongan, tanggal_kerja=tanggal_kerja, status_aktif=status_aktif, tanggal_input=sysdate)
    db.session.add(v_karyawan)    # add sama dengan insert into # karena sudah di tampung di 'dosens' value nya, maka langsung saja spt itu
    db.session.commit()
    # return response.success('', 'Sukses menambahkan data dosen')
    return flash("Berhasil insert data !!!")
  except Exception as e:
    print(e)
    

def updateKaryawanTampilan(id):
  try:
    # if request.method == 'POST': ### ini ya
    q_update = model_karyawan.zzz_dummy_karyawan.query.get_or_404(id)
    nik = request.form.get('nik')         # Ini yang bikin lama, gara2 lupa konsep dictionary. Kebingungan syntax untuk manggil nama kolomnya
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    golongan = request.form.get('golongan')
    tanggal_kerja = request.form.get('tgl_kerja')
    status_aktif = request.form.get('status_aktif')
    # tanggal_input = request.form.get('tgl_input')
    # v_tgl_kerja = datetime.datetime.strptime(row[4], "%m/%d/%Y %H:%M")
    # sysdate = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    q_update.nik = nik
    q_update.first_name = first_name
    q_update.last_name = last_name
    q_update.golongan = golongan
    q_update.tanggal_kerja = tanggal_kerja
    q_update.status_aktif = status_aktif
    # db.session.add(v_karyawan)    # add sama dengan insert into # karena sudah di tampung di 'dosens' value nya, maka langsung saja spt itu
    db.session.commit()
    # return response.success('', 'Sukses menambahkan data dosen')
    return flash("Berhasil Update data !!!")
  except Exception as e:
    print(e)
    

def deleteKaryawanTampilan(id):
  try:
    # if request.method == 'POST': ### ini ya
    q_delete = model_karyawan.zzz_dummy_karyawan.query.get_or_404(id)
    db.session.delete(q_delete)
    db.session.commit()
    # return response.success('', 'Sukses menambahkan data dosen')
    return flash("Berhasil Delete data !!!")
  except Exception as e:
    print(e)


def tabelKaryawanGet(): # deff adalah function
  # select * FROM
  v_all_karyawan = model_karyawan.zzz_dummy_karyawan.query.all() # ini kalau di Oracle macem Select * from Dosen
  data = formatArray(v_all_karyawan) #
  # return response.success(data, "success") # ngereturn dari response.py kelas succes
  return data
 

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
  'id':data.id,
  'nik':data.nik,
  'first_name':data.first_name,
  'last_name':data.last_name,
  'golongan':data.golongan,
  'tanggal_kerja':data.tanggal_kerja,
  'status_aktif':data.status_aktif,
  'tanggal_input':data.tanggal_input,
  'note':data.note
  }
  return data



### Combine data json belum berhasil
def tabelDetailKaryawanGajiGet(v_nik):
  v_kary = model_karyawan.zzz_dummy_karyawan.query.filter_by(nik=v_nik)
    # Code ini sama seperti Select * from karyawan where dosen_satu = :id OR dosen_dua = :id
    # v_gaji = model_gaji.zzz_dummy_salary.query.filter(model_gaji.zzz_dummy_salary.nik == nik)
  data_kary = formatArray(v_kary)
  
  if not data_kary:
    # return response.badRequest([], 'Tidak ada data dosen')
    return "tidak ada data karyawan !!!"
  
  data_gaji_nik = controller_gaji.tabelGajiGetNik(v_nik)
  # data_kary_single = singleDetailMahasiswa(v_kary)
  
  # return response.success(data, "success") # data = singleDetailMahasiswa(dosen, datamahasiswa)
  return data_kary
  
    

def singleDetailMahasiswa(karyawan):   # var mahasiswa berasal dari function formatMahasiswa yang tadi sudah dibuat
  data = {
    'karyawan':karyawan
    # 'id':karyawan.id,
    # 'nik':karyawan.append("nik")
    # 'first_name':karyawan.first_name,
    # 'last_name':karyawan.last_name,
    # 'golongan':karyawan.golongan,
    # 'status_aktif':karyawan.status_aktif
    # 'det_gaji': gaji# nah function tadi itu (singleDetailMahasiswa) ditempatkan disini, jadi nested di jsonnya
  }
  return data


