from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from ..controllers import OrderController

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
def create_order():
    order, error = OrderController.create(request.json)
    response = order if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    order, error = OrderController.get_by_id(_id)
    response = order if not error else {'error': error}
    status_code = 200 if order else 404 if not error else 400
    return jsonify(response), status_code


@order.route('/', methods=GET)
def get_all_orders():
    orders, error = OrderController.get_all()
    response = orders if not error else {'error': error}
    status_code = 200 if orders else 404 if not error else 400
    return jsonify(response), status_code


@order.route('/report/most-saled-ingredient', methods=GET)
def get_max_ingredient_saled():
    ingredient, error = OrderController.get_max_ingredient_saled()
    response = ingredient if not error else {'error': error}
    status_code = 200 if ingredient else 404 if not error else 400
    return jsonify(response), status_code


@order.route('/report/highest-earning-month', methods=GET)
def get_highest_earning_month():
    month, error = OrderController.get_highest_earning_month()
    response = month if not error else {'error': error}
    status_code = 200 if month else 404 if not error else 400
    return jsonify(response), status_code


@order.route('/report/best-three-customers', methods=GET)
def get_three_best_customers():
    customers, error = OrderController.get_three_best_customers()
    response = customers if not error else {'error': error}
    status_code = 200 if customers else 404 if not error else 400
    return jsonify(response), status_code
