from flask import Blueprint
from controllers.home import home

homeRoute = Blueprint('routeHome', __name__)

@homeRoute.route('/', methods=['GET'])
def home():
    return home(homeRoute)