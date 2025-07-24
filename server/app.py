from flask import Flask, jsonify
from server.routes import app_routes
from server.models import db
from flask_cors import CORS

from dotenv import load_dotenv

load_dotenv()

#initializing flask and the database
app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")

#CORS allows for frontend request without missmatch (localhost 3000 and 5000)
CORS(app)
app.config.from_object('configuration.config')
app.register_blueprint(app_routes)
db.init_app(app)

#create the tables in the database - if you change the model you have to recreate the table
with app.app_context():
    db.create_all()

#so that I dont have to read enchantment table language when things go wrong
@app.errorhandler(400)
def handle_error_badRequest(e):
    return jsonify({"error": "Bad Request", "message": str(e)}), 400

"""
#for debugging - REMOVE THIS UPON DEPLOYMENT
if __name__ == '__main__':
    app.run() #without debug mode
    # app.run(host='0.0.0.0', port=5000, debug=True) #making flask accessible to other devices
    #app.run(debug=True, threaded=True) #threaded stops bad versioned requests
"""