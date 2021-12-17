from flask import Flask
from flask_migrate import Migrate

from config import DevelopmentConfig

from flask_sqlalchemy import SQLAlchemy

# create an instance of the extension with initializing it
db = SQLAlchemy()

# instance of migrate flask
migrate = Migrate()

def app_pembelians(config=DevelopmentConfig):
  app = Flask(__name__)
  app.config.from_object(config)
  
  # initialize extension instances
  db.init_app(app)
  db.app = app
  
  # migrate initialization
  migrate.init_app(app, db)
  migrate.app = app
  
    
  # ----------register blueprints of applications-----------
  
  # SUPLIER
  from app_pembelians.entry.suplier import app_suplier as suplier
  app.register_blueprint(suplier)
  
  # BARANG
  from app_pembelians.entry.barang import app_barang as barang
  app.register_blueprint(barang)
  
  # pembelian
  from app_pembelians.entry.pembelian import app_pembelian as pembelian
  app.register_blueprint(pembelian)
  
  
  return app 