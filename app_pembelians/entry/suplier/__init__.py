# add views (endpoints) 
from flask import Blueprint

app_suplier = Blueprint('suplier', __name__, template_folder='templates', static_folder='static')

from app_pembelians.entry.suplier import view_suplier