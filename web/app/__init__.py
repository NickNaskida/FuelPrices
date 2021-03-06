from flask import Flask

from app.extensions import db, migrate


def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    from app.main.views import main_blueprint
    app.register_blueprint(main_blueprint)


def register_commands(app):
    from app.commands import fill_db, create_db
    app.cli.add_command(fill_db)
    app.cli.add_command(create_db)


