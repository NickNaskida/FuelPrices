from flask import Blueprint, render_template

from app.main.models import FuelPriceModel


main_blueprint = Blueprint(
		'main',
		__name__,
		template_folder='templates/main'
	)


@main_blueprint.route('/')
def index():
	return render_template('index.html')
