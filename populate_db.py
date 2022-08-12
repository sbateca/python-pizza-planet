from app.common.utils import (generate_random_list_dni_customers, get_random_size, get_random_ingredient,
                              get_random_beverage, generate_random_list_names, generate_random_list_phone_customers,
                              generate_random_list_address_customers, generate_random_order, generate_random_order_detail)
from sqlalchemy import create_engine, MetaData, text

import os
import random


def populate_size_table(meta_data):
    size_data = get_random_size()
    table = meta_data.tables['size']
    new_size_db = table.insert().values(size_data).return_defaults()
    new_size_db.execute()
    
    
def populate_ingredient_table(meta_data):
    ingredient_data = get_random_ingredient()
    table = meta_data.tables['ingredient']
    new_ingredient_db = table.insert().values(ingredient_data).return_defaults()
    new_ingredient_db.execute()


def populate_beverage_table(meta_data):
    beverage_data = get_random_beverage()
    table = meta_data.tables['beverage']
    new_beverage_db = table.insert().values(beverage_data).return_defaults()
    new_beverage_db.execute()


def populate_table(meta_data, table_name, position):
    data = dict()
    table = None
    
    if table_name == 'size':
        data = get_random_size(position)
        table = meta_data.tables['size']
    elif table_name == 'beverage':
        data = get_random_beverage(position)
        table = meta_data.tables['beverage']
    else:
        data = get_random_ingredient(position)
        table = meta_data.tables['ingredient']
    
    new_data_db = table.insert().values(data).return_defaults()
    result = new_data_db.execute()
    return result.inserted_primary_key_rows[0]


def populate_table_order_order_detail(meta_data, data, table_name):
    table = meta_data.tables[table_name]
    new_data_db = table.insert().values(data).return_defaults()
    result = new_data_db.execute()
    return result.inserted_primary_key_rows[0]


def get_element_by_id(conn, table_name, id):
    query_text = f"select * from {table_name} where _id = {id}"
    result = conn.execute(query_text).fetchall()
    return dict(result[0])


def get_list_elements_by_random_id(table_name, new_id_list):
    quantity_elements = random.randint(1, len(id_new_sizes))
    choosed_elements = []
    for _ in range(quantity_elements):
        position_id_random_element = random.randint(0, len(new_id_list)-1)
        choosed_element = get_element_by_id(conn, table_name, new_id_list[position_id_random_element])
        choosed_elements.append(choosed_element)
    return choosed_elements


def calculate_price(size_choosed, new_ingredients_list, new_beverages_list):
    
    total_price = size_choosed['price']
    for ingredient in new_ingredients_list:
        total_price += ingredient['price']
        
    for beverage in new_beverages_list:
        total_price += beverage['price']
        
    return total_price


def insert_order_order_detail_fake_data():
     # select one size for the order
    id_size_random = random.choice(id_new_sizes)
    size_choosed = get_element_by_id(conn,'size',id_size_random) 
    
    # get ingredients and beverage by id (random)
    new_ingredients_list = get_list_elements_by_random_id('ingredient', id_new_ingredients)
    new_beverages_list =get_list_elements_by_random_id('beverage', id_new_beverages)
    
    total_price = calculate_price(size_choosed, new_ingredients_list, new_beverages_list)
    order_data = generate_random_order(customers_names[random.randint(0, len(customers_names)-1)],
                                       customers_dni[random.randint(0, len(customers_dni)-1)],
                                       customers_phones[random.randint(0, len(customers_phones)-1)],
                                       customers_address[random.randint(0, len(customers_address)-1)],
                                       total_price,
                                       size_choosed['_id'])
    
    order_id = populate_table_order_order_detail(meta_data,order_data, 'order')
    
    # generate order detail
    for ingredient in new_ingredients_list:
        order_detail_data = generate_random_order_detail(ingredient['price'], order_id[0], ingredient['_id'], None, None)
        populate_table_order_order_detail(meta_data, order_detail_data, 'order_detail')
    
    for beverage in new_beverages_list:
        order_detail_data = generate_random_order_detail(None, order_id[0], None, beverage['price'], beverage['_id'])
        populate_table_order_order_detail(meta_data, order_detail_data, 'order_detail')
           

if __name__ == "__main__":
    
    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pizza.sqlite'), echo=False)
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    meta_data = MetaData(bind=engine)
    MetaData.reflect(meta_data)
    conn = engine.connect()

    # select_table_example(conn)
    customers_quantity = 15
    customers_names = generate_random_list_names(customers_quantity)
    customers_dni = generate_random_list_dni_customers(customers_quantity)
    customers_phones = generate_random_list_phone_customers(customers_quantity)
    customers_address = generate_random_list_address_customers(customers_quantity)
    
    id_new_sizes = []
    id_new_ingredients = []
    id_new_beverages = []
    
    for index in range(5):
        id_size = populate_table(meta_data, 'size', index )
        id_new_sizes.append(id_size[0])
        
    for index in range(10):
        id_ingredients = populate_table(meta_data, 'ingredient', index)
        id_new_ingredients.append(id_ingredients[0])
        
    for index in range(5):
        id_beverages = populate_table(meta_data, 'beverage', index)
        id_new_beverages.append(id_beverages[0])
    
    for _ in range(150):
        insert_order_order_detail_fake_data()
