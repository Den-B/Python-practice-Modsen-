from flask import Blueprint
from controllers.delete import delete

deleteRoute = Blueprint('routeDelete', __name__)

@deleteRoute.route('/document/<id>', methods=['GET'])
def delete(id):
    return delete(deleteRoute)