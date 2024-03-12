from properties.config.db import db


class Ground(db.Model):
    __tablename__ = "ground"
    id = db.Column(db.String, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    address = db.Column(db.String)
    width = db.Column(db.Float)
    length = db.Column(db.Float)
    location = db.Column(db.String)
    price = db.Column(db.Float)
    currency = db.Column(db.String)
