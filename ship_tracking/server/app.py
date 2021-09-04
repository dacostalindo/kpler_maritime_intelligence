from datetime import datetime
from flask import Flask, request, jsonify
import requests
from flask_cors import CORS, cross_origin
from flask_restful import abort
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vessel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Vessel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vessel_id = db.Column(db.Integer, nullable=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    time = db.Column(db.DateTime, nullable=False)

    def __init__(self, vessel_id, latitude, longitude, time):
        self.vessel_id = vessel_id
        self.latitude = latitude
        self.longitude = longitude
        self.time = time

# Vessel Schema
class VesselSchema(ma.Schema):
    class Meta:
        fields = ('id', 'vessel_id', 'latitude', 'longitude', 'time')

#init schema
vessel_schema = VesselSchema()
vessels_schema = VesselSchema(many = True)


def __check_entry_validity(entry_dict):
    

    if entry_dict['vessel_id'] <= 0:
        return False
    if entry_dict['latitude'] < -90.0 or entry_dict['latitude'] > 90.0:
        return False
    if entry_dict['longitude'] < -180.0 or entry_dict['longitude'] > 180.0:
        return False
    try:
        entry_dict['received_time_utc'] = datetime.strptime(request.args['received_time_utc'], "%Y-%m-%d %H:%M:%S.%f")
    except:
        if entry_dict['received_time_utc'] > datetime.now() :
            return False
    else:
        return True

def __exists_duplicate(entry_dict):
    result = Vessel.query.filter_by(vessel_id=entry_dict['vessel_id'],
                                            latitude=entry_dict['latitude'], 
                                            longitude=entry_dict['longitude'], 
                                            time=entry_dict['received_time_utc']).first()
    duplicate_entry = vessel_schema.dump(result)

    if duplicate_entry:
        return True
    else:
        return False
    

# TODO: How to create an error handling system for the API
@app.route("/insert", methods=["POST"])
@cross_origin()
def insertNewEntry():
    entry_dict = dict(request.args)
    entry_dict['vessel_id'] = int(request.args['vessel_id'])
    entry_dict['latitude'] = float(request.args['latitude'])
    entry_dict['longitude'] = float(request.args['longitude'])
    

    if __check_entry_validity(entry_dict):
        newEntry = Vessel(entry_dict['vessel_id'], entry_dict['latitude'], entry_dict['longitude'], entry_dict['received_time_utc'])
        if __exists_duplicate(entry_dict):
            return vessel_schema.jsonify(newEntry), 409
        else:
            db.session.add(newEntry)
            db.session.commit()
            return vessel_schema.jsonify(newEntry)
    else:
        print(entry_dict)
        return  entry_dict, 404
        
    


@app.route("/vessels", methods=["GET"])
@cross_origin()
def getAllVessels():
    ## TODO: Change to distinct values
    all_vessels = Vessel.query.distinct(Vessel.vessel_id).all()
    result = vessels_schema.dump(all_vessels)
    if not result:
        abort(404, message="Couldn't find vessel with that id")
    return jsonify(result), 201


@app.route("/vessels/<int:vessel_id>", methods=['GET'])
@cross_origin()
def getVessel(vessel_id):
    ## TODO: Add sort by asc vessel id
    vessel = Vessel.query.filter_by(vessel_id=vessel_id).order_by(asc(Vessel.time)).all()
    result = vessels_schema.dump(vessel)
    if not result:
        abort(404, message="Couldn't find vessel with that id")
    return jsonify(result), 201


## TODO: Take debug off for production
if __name__ == "__main__":
    app.run(debug= True)
    