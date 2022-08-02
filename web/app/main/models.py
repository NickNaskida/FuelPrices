from datetime import datetime, timedelta

from app.extensions import db
from app.models.models import BaseModel


class FuelPriceModel(db.Model, BaseModel):
	__tablename__ = 'fuel_prices'

	provider = db.Column(db.String, nullable=False)
	name = db.Column(db.String, nullable=False)
	type_alt = db.Column(db.String, nullable=False)
	price = db.Column(db.Float, nullable=False)
	date = db.Column(db.Date, nullable=False)
	last_updated = db.Column(db.DateTime, nullable=False)

	@classmethod
	def read_current_prices(cls):
		return cls.query.filter_by(date=datetime.utcnow().date()).order_by("type_alt")

	# @classmethod
	# def get_previous_day_price_change(cls):
	# 	prices = cls.query.filter_by(date=datetime.utcnow().date() - timedelta(days=1)).order_by("type_alt")
