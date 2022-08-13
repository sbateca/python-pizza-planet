from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request

from .base_service import BaseService
from ..controllers.factory_controller import FactoryController
from ..controllers import BeverageController

beverage = Blueprint('beverage', __name__)
base_service = BaseService()
controller = FactoryController.get_controller('beverage')


@beverage.route('/',methods=POST)
def create_beverage():
    return base_service.create(controller)


@beverage.route('/', methods=PUT)
def update_beverage():
    return base_service.update(controller)


@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return base_service.get_by_id(_id, controller)


@beverage.route('/', methods=GET)
def get_beverages():
    return base_service.get_all(controller)
