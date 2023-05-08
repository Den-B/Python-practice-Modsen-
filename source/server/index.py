from flask import Flask
from source.server.routes.delete import deleteRoute
from source.server.routes.search import searchRoute

def runServer(port):
    server = Flask(__name__, static_folder='.', static_url_path='')
    server.register_blueprint(searchRoute)
    server.register_blueprint(deleteRoute)
    server.run(port=port, debug=True)