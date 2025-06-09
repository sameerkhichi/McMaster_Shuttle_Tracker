from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BusLocation(db.Model):
    __tablename__ = 'bus_locations'
    bus_id = db.Column(db.String(50), primary_key=True)
    nearest_stop = db.Column(db.String(100), nullable = True)
    previous_stop = db.Column(db.String(100), nullable = False)
    next_stop = db.Column(db.String(100), nullable = True)
    eta = db.Column(db.Integer, nullable = True)
    time_stamp = db.Column(db.DateTime, nullable = False)

    def __repr__(self):
        return f"<BusLocation {self.bus_id} - {self.nearest_stop}, {self.eta}, {self.time_stamp}>"