from flask import Flask
from routes.home import appRoute

server = Flask(__name__, static_folder='.', static_url_path='')
server.register_blueprint(appRoute)
server.run(port=5000, debug=True)