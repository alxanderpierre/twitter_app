from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

SQLALCHEMY_TRACK_MODIFICATIONS = False

from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

def create_app():

    app = Flask(__name__)

    # configuring the database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/alxander44/Desktop/web_app_done/web_app_4444.db"
    db.init_app(app)
    migrate.init_app(app,db)


    class Book(db.Model):
        __table_args__ = {'extend_existing': True}
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(128))
        author_id = db.Column(db.String(128))

    # reqistering routes:
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)

    return app
