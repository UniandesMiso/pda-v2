from contracts.config.db import db


class Saga(db.Model):
    __tablename__ = "saga"
    id = db.Column(db.String, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)
    index = db.Column(db.Integer)
    is_first = db.Column(db.Boolean)
    is_last = db.Column(db.Boolean)
    event = db.Column(db.String)
    command = db.Column(db.String)
