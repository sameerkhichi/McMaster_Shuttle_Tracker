from flask import Flask
from routes import app_routes
from models import db

#initializing flask and the database
app = Flask(__name__)
app.register_blueprint(app_routes)
app.config.from_object('config')
db.init_app(app)

#create the tables in the database
with app.app_context():
    db.create_all()

#for debugging
##if __name__ == '__main__':
##    app.run(debug=True)