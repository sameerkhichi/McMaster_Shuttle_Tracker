#keep this private - database/Mysql configuration
import os

SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False