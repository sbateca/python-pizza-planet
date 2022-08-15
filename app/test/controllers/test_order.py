import pytest
from app.controllers import (IngredientController, OrderController,
                             SizeController, BeverageController)
from app.controllers.base import BaseController
from app.test.utils.functions import get_random_choice, shuffle_list


def __order(ingredients: list, size: dict, beverages: list, client_data: dict):
    ingredients = [ingredient.get('_id') for ingredient in ingredients]
    beverages = [beverage.get('_id') for beverage in beverages]
    size_id = size.get('_id')
    return {
        **client_data,
        'ingredients': ingredients,
        'beverages': beverages,
        'size_id': size_id
    }


def __create_items(items: list, controller: BaseController):
    created_items = []
    for ingredient in items:
        created_item, _ = controller.create(ingredient)
        created_items.append(created_item)
    return created_items


def __create_sizes_and_ingredients(ingredients: list, sizes: list, beverages: list):
    created_ingredients = __create_items(ingredients, IngredientController)
    created_beverages = __create_items(beverages, BeverageController)
    created_sizes = __create_items(sizes, SizeController)
    return created_sizes if len(created_sizes) > 1 else created_sizes.pop(), created_ingredients, created_beverages


def test_create(app, ingredients, size, beverages, client_data):
    created_size, created_ingredients, created_beverages = __create_sizes_and_ingredients(ingredients, [size], beverages)
    order = __order(created_ingredients, created_size, created_beverages, client_data)
    created_order, error = OrderController.create(order)
    size_id = order.pop('size_id', None)
    ingredient_ids = order.pop('ingredients', [])
    beverages_ids = order.pop('beverages', [])
    pytest.assume(error is None)
    for _ in order.items():
        pytest.assume(order['client_name'] == created_order['client_name'])
        pytest.assume(order['client_address'] == created_order['client_address'])
        pytest.assume(order['client_dni'] == created_order['client_dni'])
        pytest.assume(order['client_phone'] == created_order['client_phone'])
        pytest.assume(size_id == created_order['size']['_id'])
        detail_ingredients_id = []
        detail_beverages_id = []
        detail = created_order['detail']
        for element in detail:
            if element['ingredient'] is not None:
                detail_ingredients_id.append(element['ingredient']['_id'])        
            if element['beverage'] is not None:
                detail_beverages_id.append(element['beverage']['_id'])        
        pytest.assume(detail_ingredients_id==ingredient_ids)
        pytest.assume(detail_beverages_id==beverages_ids)


def test_calculate_order_price(app, ingredients, beverages, size, client_data):
    created_size, created_ingredients, created_beverages = __create_sizes_and_ingredients(ingredients, [size], beverages)
    order = __order(created_ingredients, created_size, created_beverages, client_data)
    created_order, _ = OrderController.create(order)
    pytest.assume(created_order['total_price'] == round(created_size['price'] + sum(ingredient['price'] for ingredient in created_ingredients) + sum(beverage['price'] for beverage in created_beverages), 2))


def test_get_by_id(app, ingredients, beverages, size, client_data):
    created_size, created_ingredients, created_beverages = __create_sizes_and_ingredients(ingredients, [size], beverages)
    order = __order(created_ingredients, created_size, created_beverages, client_data)
    created_order, _ = OrderController.create(order)
    order_from_db, error = OrderController.get_by_id(created_order['_id'])
    size_id = order.pop('size_id', None)
    ingredient_ids = order.pop('ingredients', [])
    beverages_ids = order.pop('beverages', [])
    pytest.assume(error is None)
    pytest.assume(created_order['client_name'] == order_from_db['client_name'])
    pytest.assume(created_order['client_address'] == order_from_db['client_address'])
    pytest.assume(created_order['client_dni'] == order_from_db['client_dni'])
    pytest.assume(created_order['client_phone'] == order_from_db['client_phone'])
    pytest.assume(size_id == order_from_db['size']['_id'])
    detail_ingredients_id = []
    detail_beverages_id = []
    detail = order_from_db['detail']
    for element in detail:
        if element['ingredient'] is not None:
            detail_ingredients_id.append(element['ingredient']['_id'])        
        if element['beverage'] is not None:
            detail_beverages_id.append(element['beverage']['_id'])        
    pytest.assume(detail_ingredients_id==ingredient_ids)
    pytest.assume(detail_beverages_id==beverages_ids)


def test_get_all(app, ingredients, sizes, beverages, client_data):
    created_sizes, created_ingredients, created_beverages = __create_sizes_and_ingredients(ingredients, sizes, beverages)
    created_orders = []
    for _ in range(5):
        order = __order(shuffle_list(created_ingredients)[:3], get_random_choice(created_sizes), shuffle_list(created_beverages)[:3], client_data)
        created_order, _ = OrderController.create(order)
        created_orders.append(created_order)

    orders_from_db, error = OrderController.get_all()
    searchable_orders = {db_order['_id']: db_order for db_order in orders_from_db}
    pytest.assume(error is None)
    for created_order in created_orders:
        current_id = created_order['_id']
        assert current_id in searchable_orders
        for param, value in created_order.items():
            pytest.assume(searchable_orders[current_id][param] == value)
