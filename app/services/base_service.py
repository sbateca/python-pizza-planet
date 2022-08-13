from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request
from ..controllers.factory_controller import FactoryController
from ..controllers import SizeController

class BaseService:
    
    @classmethod
    def create(cls, controller):
        size, error = controller.create(request.json)
        response = size if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code


    @classmethod
    def update(cls, controller):
        size, error = controller.update(request.json)
        response = size if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code


    @classmethod
    def get_by_id(cls, _id: int, controller):
        size, error = controller.get_by_id(_id)
        response = size if not error else {'error': error}
        status_code = 200 if size else 404 if not error else 400
        return jsonify(response), status_code


    @classmethod
    def get_all(cls, controller):
        size, error = controller.get_all()
        response = size if not error else {'error': error}
        status_code = 200 if size else 404 if not error else 400
        return jsonify(response), status_code
