import os
import tempfile

import pytest
from app import create_app, register_blueprints
from app.plugins import db, ma
# flake8: noqa
from app.repositories.models import Ingredient, Order, OrderDetail, Size

from .fixtures.ingredient import (ingredient_mock, ingredient_uri,
                                  ingredient, ingredients,
                                  create_ingredient, create_ingredients)
from .fixtures.order import (client_data_mock, order_uri, client_data,
                             order, create_order, create_orders)
from .fixtures.size import (size_mock, size_uri, size, sizes,
                            create_size, create_sizes)
from .fixtures.beverage import (beverage_mock, beverage_uri, beverage,
                                beverages, create_beverage, create_beverages)


@pytest.fixture
def app():

    db_fd, dbpath = tempfile.mkstemp()

    class Config:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(dbpath)
        TESTING = True
        SQLALCHEMY_TRACK_MODIFICATIONS = False

    flask_app = create_app(Config)
    register_blueprints(flask_app)
    flask_app.app_context().push()
    db.init_app(flask_app)
    ma.init_app(flask_app)

    db.create_all()

    yield flask_app

    db.session.remove()
    db.drop_all()
    os.close(db_fd)
    os.remove(dbpath)


@pytest.fixture
def client(app):
    client = app.test_client()
    return client
