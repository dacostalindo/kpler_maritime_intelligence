from flask import Flask, request
from flask_restful import Api, Resource, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vessel_database.db'
db = SQLAlchemy(app)

class VesselModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vessel_id = db.Column(db.Integer, nullable=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    time = db.Column(db.DateTime, nullable=False)

# db.create_all()

resource_fields = { 
    'id': fields.Integer,
    'vessel_id': fields.Integer,
    'latitude': fields.Float,
    'longitude': fields.Float,
    'time': fields.DateTime,
}


class Vessel(Resource):

    @marshal_with(resource_fields)
    def get(self, vessel_id):
        result = VesselModel.query.filter_by(vessel_id=vessel_id).order_by(asc(VesselModel.time)).all()
        if not result:
            abort(404, message="Couldn't find vessel with that id")
        return result

    def put(self, vessel_id):
        pass

api.add_resource(Vessel, "/ship/<int:vessel_id>")

    
## TODO: Take debug off for production
if __name__ == "__main__":
    app.run(debug=True)
    