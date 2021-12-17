from app_pembelians.entry.barang import app_barang, controller_barang
from flask import render_template, url_for, redirect
  
@app_barang.route('/barang-json', methods=['GET'])
def barang_data():
  return controller_barang.barangData()

@app_barang.route('/barang-json/<id_suplier>', methods=['GET'])
def barang_data_detail(id_suplier):
  return controller_barang.barangDataDetail(id_suplier)  # --- DETAIL BARANG --- #
  

# -----------------------------FRONTEND--------------------------------# 

@app_barang.route('/barang')
def barang():
  data = controller_barang.barangData()
  return render_template('barang/barang.html', barang=data)