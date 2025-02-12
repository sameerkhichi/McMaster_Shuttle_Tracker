from flask import Flask, request, jsonify, redirect, url_for
from models import db

#initializing flask and the database
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

#create the tables in the database
with app.app_context():
    db.create_all()