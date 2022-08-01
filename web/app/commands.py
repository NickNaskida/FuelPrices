import click

from flask.cli import with_appcontext

from app.extensions import db
from app.crontab.main import parse_data


@click.command('fill_db')
@with_appcontext
def fill_db():
	parse_data()


@click.command("create_db")
@with_appcontext
def create_db():
	db.drop_all()
	db.create_all()
	db.session.commit()
