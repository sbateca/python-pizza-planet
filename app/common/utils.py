from faker import Faker

import random

faker = Faker()

ingredients_names = ['pineapple','tuna','sauce','cheese','Garlic','chicken','mushroom','spicy','bacon','onion']
sizes_names = ['x-small','normal','long','extra long','giant']
beverages_names = ['water','wine','beer','juice','soda']

min = 1111111111
max = 9999999999


def check_required_keys(keys: tuple, element: dict):
    return all(element.get(key) for key in keys)


def generate_random_name():
    return faker.name()


def generate_random_number(min, max) -> int:
    return random.randint(min, max)


def generate_random_address() -> str:
    return faker.address()


def get_random_phone_number() -> str:
    return str(generate_random_number(min, max))


def get_random_price() -> str:
    return generate_random_number(1, 10)


def generate_random_date():
    return faker.past_datetime("-100d")


def get_random_ingredient(position):
    return {
        "name": ingredients_names[position],
        "price": random.randint(1, 10)
    }

    
def get_random_size(position):
    return {
        "name": sizes_names[position],
        "price": random.randint(1, 10)
    }
    
    
def get_random_beverage(position):
    return {
        "name": beverages_names[position],
        "price": random.randint(1, 10)
    }
    

def generate_random_list_names(quantity):
    customers_randoms_name = []
    for _ in range(quantity):
        customers_randoms_name.append(generate_random_name())
    return customers_randoms_name


def generate_random_list_dni_customers(quantity):
    customers_randoms_dni = []
    for _ in range(quantity):
        customers_randoms_dni.append(generate_random_number(min, max))
    return customers_randoms_dni


def generate_random_list_phone_customers(quantity):
    customers_randoms_phone = []
    for _ in range(quantity):
        customers_randoms_phone.append(get_random_phone_number())
    return customers_randoms_phone


def generate_random_list_address_customers(quantity):
    customers_randoms_address = []
    for _ in range(quantity):
        customers_randoms_address.append(generate_random_address())
    return customers_randoms_address


def generate_random_order(customer_name, customer_dni, customer_phone, customer_address, total_price, size_id):
    return {
        "client_name": customer_name,
        "client_dni": customer_dni,
        "client_phone": customer_phone,
        "client_address": customer_address,
        "date": generate_random_date(),
        "total_price": total_price,
        "size_id": size_id
    }


def generate_random_order_detail(ingredient_price, order_id, ingredient_id, beverage_price, beverage_id):
    return {
        "ingredient_price": ingredient_price,
        "order_id": order_id,
        "ingredient_id": ingredient_id,
        "beverage_price": beverage_price,
        "beverage_id": beverage_id
    }
    