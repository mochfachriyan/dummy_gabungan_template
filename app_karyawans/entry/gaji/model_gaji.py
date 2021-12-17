# from flask_sqlalchemy import SQLAlchemy
from app_karyawans import db

# # create an instance of the extension with initializing it
# db = SQLAlchemy()

class zzz_dummy_salary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nik = db.Column(db.String(6), nullable=False)
    gaji_ke = db.Column(db.BigInteger, nullable=False)
    tanggal_gajian = db.Column(db.Date)
    salary = db.Column(db.Float, nullable=False)
    
def __repr__(self):
  return '<zzz_dummy_salary {}>'.format(self.name) # return ke Salary {NIK} misalnya
    