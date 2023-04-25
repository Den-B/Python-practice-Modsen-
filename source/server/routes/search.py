from flask import Blueprint
from controllers.search import search

searchRoute = Blueprint('routeSearch', __name__)

@searchRoute.route('/', methods=['GET'])
def search():
    return search(searchRoute)