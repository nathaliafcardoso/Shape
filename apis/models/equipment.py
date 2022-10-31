from apis.models.model import db

class equipment(db.Model):
    __tablename__ = 'equipments'

    id = db.Column(db.BigInteger, primary_key=True)
    vessel_id = db.Column(db.BigInteger, db.ForeignKey('vessels.id'))
    name = db.Column(db.String(256))
    code = db.Column(db.String(8), unique=True)
    location = db.Column(db.String(256))
    active = db.Column(db.Boolean)

def __init__(self, id, vessel_id, name, code, location, active):
    self.id =  id
    self.vessel_id = vessel_id
    self.name = name
    self.code = code
    self.location = location
    self.active = active