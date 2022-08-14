from typing import Any, List, Optional, Sequence

from sqlalchemy.sql import text, column
from sqlalchemy import create_engine, MetaData

from .models import Ingredient, Order, OrderDetail, Size, Beverage, db
from .serializers import (IngredientSerializer, OrderSerializer,
                          SizeSerializer, BeverageSerializer, ma)
from ..common.singleton import singleton

import os

@singleton
class ConnectDB:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(os.getcwd(),"pizza.sqlite"), echo=False)


    @classmethod
    def connect_db(cls):
        engine = create_engine(cls.SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False})
        meta_data = MetaData(bind=engine)
        MetaData.reflect(meta_data)
        conn = engine.connect()
        return conn    


class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session


    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
        return cls.get_by_id(_id)


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []
    
class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer
    
    connectDB = ConnectDB()
    
    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        for ingredient in ingredients:
            cls.session.add(OrderDetail(order_id=new_order._id, ingredient_id=ingredient._id, ingredient_price=ingredient.price,
                                                 beverage_id = None, beverage_price = None))
        for beverage in beverages:
            cls.session.add(OrderDetail(order_id=new_order._id, ingredient_id=None, ingredient_price=None,
                                                 beverage_id = beverage._id, beverage_price = beverage.price))
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def update(cls):
        raise NotImplementedError(f'Method not suported for {cls.__name__}')


    @classmethod
    def get_max_ingredient_saled(cls):
        conn = cls.connectDB.connect_db()
        query_text = "select max(CI.quantity) total_quantity, CI.name from (select count(ingredient_id) as quantity, ing.name as name from order_detail od, ingredient ing where ingredient_id is not null AND ing._id = od.ingredient_id group by ingredient_id) as CI"
        result = conn.execute(query_text).fetchall()
        return dict(result[0])


    @classmethod
    def get_highest_earning_month(cls):
        conn = cls.connectDB.connect_db()
        query_text = """select max(MS.total_price) total_price, MS.date_month month from (SELECT sum(total_price) as total_price, strftime('%Y %m',date) as date_month from "order" group by strftime('%Y %m',date)) as MS"""
        result = conn.execute(query_text).fetchall()
        return dict(result[0])


    @classmethod
    def get_three_best_customers(cls):
        conn = cls.connectDB.connect_db()
        query_text = """select count (client_name) as quantity, client_name from "order" group by client_name order by count (client_name) desc limit 3 offset 0"""
        result = conn.execute(query_text).fetchall()
        query_result = []
        for item in result:
            query_result.append(dict(item))
        return query_result


class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()
