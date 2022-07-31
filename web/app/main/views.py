from flask import Blueprint, render_template


main_blueprint = Blueprint(
		'main',
		__name__,
		template_folder='templates/main'
	)


@main_blueprint.route('/')
def index():
	return render_template('index.html')


@main_blueprint.route('/about')
def about():
	return render_template('about.html')
