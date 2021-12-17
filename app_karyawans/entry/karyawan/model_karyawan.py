# create an instance of the extension with initializing it
from app_karyawans import db

class zzz_dummy_karyawan (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nik = db.Column(db.String(6), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100))
    golongan = db.Column(db.String(6), nullable=False)
    tanggal_kerja = db.Column(db.DateTime)
    status_aktif = db.Column(db.String(6), nullable=False)
    tanggal_input = db.Column(db.DateTime)
    note = db.Column(db.String(100))
  
def __repr__(self):
  return '<zzz_dummy_karyawan {}>'.format(self.name) # return ke Salary {NIK} misalnya
    