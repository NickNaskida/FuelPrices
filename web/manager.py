from flask.cli import FlaskGroup

from app import create_app
from app.extensions import db

app = create_app()
cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
