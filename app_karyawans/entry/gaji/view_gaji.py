from app_karyawans.entry.gaji import app_gaji, controller_gaji
from flask import render_template, jsonify, redirect, url_for, request

# @app_suplier.route('/suplier')
# def suplier():
#     return render_template('suplier/suplier.html')


## Menampilkan data berbentuk json  
@app_gaji.route('/gaji', methods=['GET', 'POST'])
def gaji_data():
  data = controller_gaji.tabelGajiGet()
  return jsonify(data)


@app_gaji.route('/gaji/<nik>', methods=['GET', 'POST'])
def gaji_data_nik(nik):
  data = controller_gaji.tabelGajiGetNik(nik)
  return jsonify(data)    # mending disini nih jsonify nya
 
 

## Menampilkan data di tabel tampilan
@app_gaji.route('/tabel-gaji', methods=['GET'])
def gajiDataTable():
  data = controller_gaji.tabelGajiGet()
  return render_template('/gaji/tabel-gaji.html', dummy=data)

@app_gaji.route('/insert-gaji-table-cek/<nik>', methods=['GET', 'POST'])
def gajiDataTableInsertCek(nik):
  data = controller_gaji.insertGajiTampilanCek(nik)
  # for row in data:
  #   print(row.get('salary'))
    
  # print(data)
  # return "jsonify(data)"
  return "asd"
  

# @app_gaji.route("/insert-gaji-table", methods=['GET', 'POST'])
# def gajiDataTableInsert():
#   # controller_gaji.insertGajiTampilan()
#   # return redirect(url_for('gaji.gajiDataTable'))
#   return controller_gaji.insertGajiTampilan()