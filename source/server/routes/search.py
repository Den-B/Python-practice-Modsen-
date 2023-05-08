from flask import Blueprint
from flask import request
from source.server.controllers.search import searchRecords
import json

searchRoute = Blueprint('routeSearch', __name__)

@searchRoute.route('/search', methods=['GET'])
def search():
    return searchRecords(request.args["query"])
