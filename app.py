from flask import Flask
from pymongo import MongoClient
from app.routes import main_routes

app = Flask(__name__)
app.register_blueprint(main_routes)

if __name__ == '__main__':
    app.run()
