from app.common.http_methods import GET
from flask import Blueprint, jsonify

from ..controllers.factory_controller import FactoryController


report = Blueprint('report', __name__)
controller = FactoryController.get_controller('report')


@report.route('/most-saled-ingredient', methods=GET)
def get_max_ingredient_saled():
    ingredient, error = controller.get_max_ingredient_saled()
    response = ingredient if not error else {'error': error}
    status_code = 200 if ingredient else 404 if not error else 400
    return jsonify(response), status_code


@report.route('/highest-earning-month', methods=GET)
def get_highest_earning_month():
    month, error = controller.get_highest_earning_month()
    response = month if not error else {'error': error}
    status_code = 200 if month else 404 if not error else 400
    return jsonify(response), status_code


@report.route('/best-three-customers', methods=GET)
def get_three_best_customers():
    customers, error = controller.get_three_best_customers()
    response = customers if not error else {'error': error}
    status_code = 200 if customers else 404 if not error else 400
    return jsonify(response), status_code
