from . import db

class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    weaponType = db.Column(db.String(20))
    damage = db.Column(db.Integer, )
    status = db.Column(db.String(20))
    level = db.Column(db.String(20))
