import pytz
from datetime import date, datetime, timezone

from .gulf_parser import parse_gulf_data
from .rompetrol_parser import parse_rompetrol_data
from .wissol_parser import parse_wissol_data
from .lukoil_parser import parse_lukoil_data
from .socar_parser import parse_socar_data

from app.extensions import db
from app.main.models import FuelPriceModel


def parsing_error_notify(message, exc=None):
	# TODO implement parsing error notify function
	print(message)
	pass


def parsed_data_confirmation(name, price, fuel_type):
	# name check

	names_list = [
		'დიზელ ენერჯი', 'ევრო დიზელი', 'ევრო რეგულარი', 'G-Force ევრო დიზელი', 'Efix ევრო დიზელი', 'ეკო დიზელი',
		'ნანო დიზელი', 'G-Force ევრო რეგულარი', 'G-Force პრემიუმი', 'Efix ევრო პრემიუმი',
		'ეკო პრემიუმი', 'პრემიუმ ავანგარდი', 'ნანო პრემიუმი', 'G-Force სუპერი', 'Efix სუპერი', 'ეკო სუპერი',
		'სუპერ ეკტო', 'ნანო სუპერი'
	]

	if name not in names_list:
		parsing_error_notify('NAME CHECK FAILED')
		return False

	# price check

	try:
		float(price)
	except Exception as exc:
		parsing_error_notify('PRICE CHECK FAILED', exc)
		return False

	# fuel type check
	if fuel_type is None:
		parsing_error_notify('FUEL TYPE CHECK FAILED')
		return False

	return True


def get_fuel_type(fuel_name):
	fuel_types = {
		'other': ['დიზელ ენერჯი'],
		'diesel': ['ევრო დიზელი'],
		'regular': ['ევრო რეგულარი'],
		'diesel_alt': ['G-Force ევრო დიზელი', 'Efix ევრო დიზელი', 'ეკო დიზელი', 'ნანო დიზელი'],
		'regular_alt': ['G-Force ევრო რეგულარი'],
		'premium_alt': ['G-Force პრემიუმი', 'Efix ევრო პრემიუმი', 'ეკო პრემიუმი', 'პრემიუმ ავანგარდი', 'ნანო პრემიუმი'],
		'super_alt': ['G-Force სუპერი', 'Efix სუპერი', 'ეკო სუპერი', 'სუპერ ეკტო', 'ნანო სუპერი']
	}

	for fuel_type, fuel_list in fuel_types.items():
		if fuel_name in fuel_list:
			return fuel_type

	return None


def write_fuel_to_db(name, price, provider):
	fuel_price_model = FuelPriceModel()
	fuel_type = get_fuel_type(name)

	if not parsed_data_confirmation(name, price, fuel_type):
		return

	fuel_price_objects = fuel_price_model.query.filter_by(provider=provider, type_alt=fuel_type, date=date.today())

	if fuel_price_objects.count() == 0:
		fuel_price_model.create(
			save=True,
			provider=provider,
			name=name,
			type_alt=fuel_type,
			price=price,
			date=datetime.now(pytz.timezone('Asia/Tbilisi')).date(),
			last_updated=datetime.now()
		)
	else:
		if float(fuel_price_objects[0].price) != float(price):
			fuel_price_objects[0].update(
				save=True,
				price=price,
			)

		fuel_price_objects[0].update(
			save=True,
			last_updated=datetime.now()
		)


def parse_data():
	try:
		for name, price in parse_gulf_data().items():
			write_fuel_to_db(name, price, 'Gulf')
	except Exception as exc:
		parsing_error_notify('MESSAGE_TEXT', exc)

	try:
		for name, price in parse_rompetrol_data().items():
			write_fuel_to_db(name, price, 'Rompetrol')
	except Exception as exc:
		parsing_error_notify('MESSAGE_TEXT', exc)

	try:
		for name, price in parse_wissol_data().items():
			write_fuel_to_db(name, price, 'Wissol')
	except Exception as exc:
		parsing_error_notify('MESSAGE_TEXT', exc)

	try:
		for name, price in parse_lukoil_data().items():
			write_fuel_to_db(name, price, 'Lukoil')
	except Exception as exc:
		parsing_error_notify('MESSAGE_TEXT', exc)

	try:
		for name, price in parse_socar_data().items():
			write_fuel_to_db(name, price, 'Socar')
	except Exception as exc:
		parsing_error_notify('MESSAGE_TEXT', exc)

	db.session.commit()
