from flask import Blueprint, render_template

from app.main.models import FuelPriceModel

main_blueprint = Blueprint(
		'main',
		__name__,
		template_folder='templates/main'
	)


@main_blueprint.app_context_processor
def inject_today_prices():
	return dict(
		today_prices=FuelPriceModel.read_today_prices()
	)


@main_blueprint.route('/')
def index():
	return render_template('index.html')


@main_blueprint.route('/about')
def about():
	return render_template('about.html')


@main_blueprint.route('/api')
def api():
	return render_template('api.html')
