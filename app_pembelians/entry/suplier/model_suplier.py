from app_pembelians import db
from flask import flash, request

from app_pembelians.entry.suplier import view_suplier

class suplier(db.Model):
    # __tablename__ = 'suplier'
    id_suplier = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_suplier = db.Column(db.String(30))
    no_telp = db.Column(db.String(15))
    alamat = db.Column(db.String(100))
    
    def __init__(self, nama_suplier, no_telp, alamat):
      self.nama_suplier  = nama_suplier
      self.no_telp       = no_telp
      self.alamat        = alamat
    
    def __repr__(self):
      return '<suplier {}>'.format(self.name)