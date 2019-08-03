from flask import Flask


# blueprintsをappと関連
def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    # blueprintをappにbind
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.setting")
    app.config.from_object("app.config.secure")

    register_blueprints(app)

    return app