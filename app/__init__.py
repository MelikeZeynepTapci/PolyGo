from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from app.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, ssl_args

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

    # Create the SQLAlchemy engine with SSL configuration
    engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args=ssl_args)

    # Bind the engine to SQLAlchemy and initialize it
    db.init_app(app)
    db.engine = engine  # Manually assign the engine to db

    return app






