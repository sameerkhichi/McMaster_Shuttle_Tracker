from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BusLocation(db.Model):
    __tablename__ = 'bus_locations'
    id = db.Column(db.Integer, primary_key = True)
    bus_id = db.Column(db.String(50), nullable = False)
    latitude = db.Column(db.Float, nullable = False)
    longitude = db.Column(db.Float, nullable = False)
    time_stamp = db.Column(db.DateTime, nullable = False)

    def __repr__(self):
        return f"<BusLocation {self.bus_id} - {self.latitude}, {self.longitude}>"