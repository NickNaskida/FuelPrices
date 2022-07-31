from app.extensions import db
from app.models.models import BaseModel


class FuelPriceModel(db.Model, BaseModel):
	__tablename__ = 'fuel_prices'

	provider = db.Column(db.String, nullable=False)
	name = db.Column(db.String, nullable=False)
	type_alt = db.Column(db.String, nullable=False)
	price = db.Column(db.Float, nullable=False)
	date = db.Column(db.Date, nullable=False)
