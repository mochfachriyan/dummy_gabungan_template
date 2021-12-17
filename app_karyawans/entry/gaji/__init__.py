# add views (endpoints) 
from flask import Blueprint

app_gaji = Blueprint('gaji', __name__, template_folder='templates')

from app_karyawans.entry.gaji import view_gaji 