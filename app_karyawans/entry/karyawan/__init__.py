# add views (endpoints) 
from flask import Blueprint

app_karyawan = Blueprint('karyawan', __name__, template_folder='templates')

from app_karyawans.entry.karyawan import view_karyawan