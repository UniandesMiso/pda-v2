from contracts.config.db import db


class Sale(db.Model):
    __tablename__ = "sale"
    id = db.Column(db.String, primary_key=True)
    property_id = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String, nullable=False)
    executed_at = db.Column(db.DateTime, nullable=False)
