from app_karyawans.entry.gaji import model_gaji, response
from flask import jsonify, request, flash
from app_karyawans import db
import datetime



## Menampilkan data berdasarkan NIK
def tabelGajiGetNik(nik):  # Simpan dulu
  # select * FROM
  v_gaji_nik = model_gaji.zzz_dummy_salary.query.filter_by(nik = nik).all()
  data = formatArray(v_gaji_nik) #
  return data # ngereturn dari response.py kelas succes
                        # Recommend menggunakan return data. Kalau sudah dibuat jsonify
                        # convert lg ke format array akan susah. MEnding di view nya saja kalau
                        # mau convert ke jsonify


## Menampilkan semua data gaji
def tabelGajiGet(): # deff adalah function
  # select * FROM
  v_all_gaji = model_gaji.zzz_dummy_salary.query.all() # ini kalau di Oracle macem Select * from Dosen
  data = formatArray(v_all_gaji) #
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
  'nik':data.nik,
  'gaji_ke':data.gaji_ke,
  'tanggal_gajian':data.tanggal_gajian,
  'salary':data.salary
  }
  return data



## Insert 1 data gaji
def insertGajiTampilanCek(nik):
  tes_gaji = model_gaji.zzz_dummy_salary.query.filter_by(nik='016881') # ini kalau di Oracle macem Select * 
  data = formatArray(tes_gaji)
  for row in data:
    tes = row.get('salary')
    # print(tes)
  # data = formatArray(tes_gaji)
  # return response.success(data, "success") # ngereturn dari response.py kelas succes
    return tes




# def insertGajiTampilan():
#   nik = request.form.get('nik')         # Ini yang bikin lama, gara2 lupa konsep dictionary. Kebingungan syntax untuk manggil nama kolomnya
#   tanggal_gajian = request.form.get('tgl_gajian')
#   gaji = request.form.get('gaji')
#   # sysdate = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S') 
  
#   v_cek = model_gaji.zzz_dummy_salary.query.get_or_404(nik)
#   v_cek2= v_cek.salary
  
#   # v_karyawan = model_gaji.zzz_dummy_salary(nik=nik, tanggal_gajian=tanggal_gajian, gaji_ke=4, salary=gaji )
#   # db.session.add(v_karyawan)    # add sama dengan insert into # karena sudah di tampung di 'dosens' value nya, maka langsung saja spt itu
#   # db.session.commit()
#   # return response.success('', 'Sukses menambahkan data dosen')
#   # return flash("Berhasil insert data !!!")
#   return nik
  