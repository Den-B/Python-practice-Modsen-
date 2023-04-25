from flask import Flask
from routes.home import homeRoute
from routes.delete import deleteRoute
from routes.search import searchRoute

server = Flask(__name__, static_folder='.', static_url_path='')
server.register_blueprint(homeRoute)
server.register_blueprint(searchRoute)
server.register_blueprint(deleteRoute)
server.run(port=5000, debug=True)