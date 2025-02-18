from flask import Flask
from server.routes import app_routes
from server.models import db

#initializing flask and the database
app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(app_routes)
db.init_app(app)

#create the tables in the database
with app.app_context():
    db.create_all()

#for debugging
if __name__ == '__main__':
    app.run(debug=True)