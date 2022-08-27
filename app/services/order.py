from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from .base_service import BaseService
from ..controllers.factory_controller import FactoryController


order = Blueprint('order', __name__)
base_service = BaseService()
controller = FactoryController.get_controller('order')


@order.route('/', methods=POST)
def create_order():
    return base_service.create(controller)


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return base_service.get_by_id(_id, controller)


@order.route('/', methods=GET)
def get_all_orders():
    return base_service.get_all(controller)


@order.route('/report/most-saled-ingredient', methods=GET)
def get_max_ingredient_saled():
    ingredient, error = controller.get_max_ingredient_saled()
    response = ingredient if not error else {'error': error}
    status_code = 200 if ingredient else 404 if not error else 400
    return jsonify(response), status_code


@order.route('/report/highest-earning-month', methods=GET)
def get_highest_earning_month():
    month, error = controller.get_highest_earning_month()
    response = month if not error else {'error': error}
    status_code = 200 if month else 404 if not error else 400
    return jsonify(response), status_code


@order.route('/report/best-three-customers', methods=GET)
def get_three_best_customers():
    customers, error = controller.get_three_best_customers()
    response = customers if not error else {'error': error}
    status_code = 200 if customers else 404 if not error else 400
    return jsonify(response), status_code
