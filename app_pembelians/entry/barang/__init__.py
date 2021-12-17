# add views (endpoints) 
from flask import Blueprint

app_barang = Blueprint('barang', __name__, template_folder='templates', static_folder='static')

from app_pembelians.entry.barang import view_barang