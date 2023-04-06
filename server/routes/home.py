from flask import Blueprint
from controllers.home import home
from controllers.test import test

appRoute = Blueprint('route', __name__)

@appRoute.route('/')
def home():
    return home(appRoute)

@appRoute.route('/echo/<thing>')
def echo(thing):
    return test(appRoute,thing)