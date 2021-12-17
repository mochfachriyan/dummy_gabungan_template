from flask.helpers import url_for
from werkzeug.wrappers import request
from app_karyawans.entry.karyawan import app_karyawan, controller_karyawan
from flask import render_template, jsonify, redirect, request

# @app_suplier.route('/suplier')
# def suplier():
#     return render_template('suplier/suplier.html')

@app_karyawan.route('/')                       # otomatis memetakan ke URL default (localhost) 127.0.0.1:5000
def home():                           # fungsi home() dipanggil ketika URL default di akses
  return render_template('home.html')

@app_karyawan.route('/karyawan', methods=['GET', 'POST'])
def karyawanData():
  data = controller_karyawan.tabelKaryawanGet()
  return jsonify(data)

@app_karyawan.route('/karyawan/<nik>', methods=['GET', 'POST'])
def karyawanGajiData(nik):
  data = controller_karyawan.tabelDetailKaryawanGajiGet(nik)
  return jsonify(data)
 
@app_karyawan.route("/tabel-karyawan", methods=['GET', 'POST'])
def karyawanDataTable():
  data = controller_karyawan.tabelKaryawanGet()
  return render_template("/karyawan/tabel-karyawan.html", dummy=data)

@app_karyawan.route("/insert-karyawan-table", methods=['GET', 'POST'])
def karyawanDataTableInsert():
  controller_karyawan.insertKaryawanTampilan()
  return redirect(url_for('karyawan.karyawanDataTable'))


@app_karyawan.route("/update-karyawan-table/<id>", methods=['GET', 'POST'])
def karyawanDataTableUpdate(id):
  try:
    controller_karyawan.updateKaryawanTampilan(id)
    return redirect(url_for('karyawan.karyawanDataTable'))
  except Exception as e:
    print(e)
  # asd = request.form.get('nik')
  
@app_karyawan.route("/delete-karyawan-table/<id>", methods=['GET', 'POST'])
def karyawanDataTableDelete(id):
  controller_karyawan.deleteKaryawanTampilan(id)
  return redirect(url_for('karyawan.karyawanDataTable'))