from app_pembelians import db

class barang(db.Model):
    # __tablename__ = 'barang'
    id_barang = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_barang = db.Column(db.String(30))
    harga = db.Column(db.Float)
    id_suplier = db.Column(db.Integer)
    keterangan = db.Column(db.String(200))
    
    def __init__(self, nama_barang, harga, id_suplier, keterangan):
      self.nama_barang = nama_barang
      self.harga       = harga
      self.id_suplier  = id_suplier
      self.keterangan  = keterangan
      
    def __repr__(self):
      return '<barang {}>'.format(self.name)