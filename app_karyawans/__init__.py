from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig

# import extensions instance
# from app_karyawans.entry.gaji.model_gaji import db
db = SQLAlchemy()
migrate = Migrate()

def gaji_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    
    # initialize extension instances
    db.init_app(app)
    db.app = app
    
    # initialize extension instances
    migrate.init_app(app, db)
    migrate.app = app    
    
    
    # ----------register blueprints of applications-----------
    
    # # GAJI
    from app_karyawans.entry.gaji import app_gaji as gaji
    app.register_blueprint(gaji)
        
    # # KARYAWAN
    from app_karyawans.entry.karyawan import app_karyawan as karyawan
    app.register_blueprint(karyawan)
    
    return app
