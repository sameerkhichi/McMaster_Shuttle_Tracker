#keep this private - database/Mysql configuration
import os

DB_USERNAME = "sameer"
DB_PASSWORD = "E119!dataaccess"
DB_HOST = "localhost"
DB_NAME = "shuttle_tracker"

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False