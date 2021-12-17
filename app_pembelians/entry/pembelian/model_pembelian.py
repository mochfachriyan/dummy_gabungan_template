from app_pembelians import db

class pembelian(db.Model):
    # __tablename__ = 'pembelian'
    id_pembelian = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer)
    id_barang = db.Column(db.Integer)
    tanggal = db.Column(db.DateTime)
    keterangan = db.Column(db.String(200))
    
    def __repr__(self):
      return '<pembelian {}>'.format(self.name)
    
    
class user(db.Model):
    # __tablename__ = 'user'
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(25))
    username = db.Column(db.String(25))
    password = db.Column(db.String(25))
    email = db.Column(db.String(25))
    
    def __repr__(self):
      return '<user {}>'.format(self.name)