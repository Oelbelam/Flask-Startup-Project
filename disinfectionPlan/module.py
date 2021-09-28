import datetime
from disinfectionPlan import db


class Room(db.Model):
    ##------------ Change This code ------------##
    id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(200))
    people_count = db.Column(db.Integer)
    def __init__(self, people_count):
        self.people_count = people_count