from app_pembelians.entry.pembelian import app_pembelian, controller_pembelian
from flask import render_template

@app_pembelian.route('/pembelian')
def barang():
    return 'tes'
  
@app_pembelian.route('/pembelian-data', methods=['GET', 'POST'])
def pembelian_data():
  return controller_pembelian.pembelianData()
