from apis.models.model import db


class vessel(db.Model):
    __tablename__ = 'vessels'

    id = db.Column(db.BigInteger, primary_key=True)
    code = db.Column(db.String(8), unique=True)


def __init__(self,id, code):

    self.id = id
    self.code = code
   