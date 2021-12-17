import re
from app_pembelians.entry.suplier import app_suplier, controller_suplier, model_suplier
from flask import app, render_template, redirect, url_for, request
  
@app_suplier.route('/suplier-json', methods=['GET', 'POST'])
def suplierJson():
  return controller_suplier.suplierData()

@app_suplier.route('/suplier-json/<id_suplier>', methods=['GET'])
def suplierJsonDetails(id_suplier):
  return controller_suplier.suplierDataDetail(id_suplier)  # --- DETAIL SUPLIER --- #




# -----------------------------FRONTEND--------------------------------# 
@app_suplier.route('/')
def index():
  return redirect(url_for('suplier.home'))

@app_suplier.route('/home')
def home():
  return render_template('dashboard.html')
  
@app_suplier.route('/suplier')
def suplier():
  data = controller_suplier.suplierData()
  return render_template('suplier/suplier.html', suplier = data)

# TAMBAH SUPLIER  
@app_suplier.route('/tambah-suplier', methods=['GET', 'POST'])
def tambah_suplier():
  return controller_suplier.tambahSuplier()

# EDIT SUPLIER  
@app_suplier.route('/edit-suplier/', methods=['GET', 'POST'])
def edit_suplier():
  return controller_suplier.editSuplier()

# HAPUS SUPLIER  
@app_suplier.route('/hapus-suplier/<id_suplier>', methods=['GET', 'POST'])
def hapus_suplier(id_suplier):
  return controller_suplier.hapusSuplier(id_suplier)