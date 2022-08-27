from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request

from .base_service import BaseService

from ..controllers.factory_controller import FactoryController


ingredient = Blueprint('ingredient', __name__)
base_service = BaseService()
controller = FactoryController.get_controller('ingredient')


@ingredient.route('/', methods=POST)
def create_ingredient():
    return base_service.create(controller)


@ingredient.route('/', methods=PUT)
def update_ingredient():
    return base_service.update(controller)


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return base_service.get_by_id(_id, controller)


@ingredient.route('/', methods=GET)
def get_ingredients():
    return base_service.get_all(controller)
