#database/MySQL configuration
import os

SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_pre_ping': True,       #Checks if connection is alive before using
    'pool_recycle': 280,         #Recycle idle connections every ~5 minutes
    'pool_size': 5,              #Max 5 persistent connections (free-tier limit)
    'max_overflow': 0,           #Don't allow extra (temporary) connections
    'pool_timeout': 10           #Wait max 10 seconds before giving up on getting a connection
}
