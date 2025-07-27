#keep this private - database/Mysql configuration
import os

SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_pre_ping': True, #preping to ensure active status
    'pool_recycle': 14400 #recycle connecting every 4 hours avoiding sql timing out
}