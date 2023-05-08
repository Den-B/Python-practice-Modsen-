from flask import Blueprint
from source.server.controllers.delete import deleterRecord

deleteRoute = Blueprint('routeDelete', __name__)

@deleteRoute.route('/document/<id>', methods=['DELETE'])
def delete(id):
    return deleterRecord(id)