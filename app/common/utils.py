from faker import Faker
from typing import Any, Union
from datetime import date

import random
import string


faker = Faker()

ingredients_names = ['pineapple','tuna','sauce','cheese','Garlic','chicken','mushroom','spicy','bacon','onion']
sizes_names = ['x-small','normal','long','extra long','giant']
beverages_names = ['water','wine','beer','juice','soda']

min_value_randon_number = 1111111111
max_value_randon_number = 9999999999


def check_required_keys(keys: tuple, element: dict):
    return all(element.get(key) for key in keys)


def get_random_name():
    return faker.name()


def get_random_number(min_value_randon_number, max_value_randon_number) -> int:
    return random.randint(min_value_randon_number, max_value_randon_number)


def get_random_address() -> str:
    return faker.address()


def get_random_phone_number() -> str:
    return str(get_random_number(min_value_randon_number, max_value_randon_number))


def get_random_price() -> str:
    return get_random_number(1, 10)


def get_random_date():
    return faker.past_datetime("-100d")


def get_random_ingredient(index):
    return {
        "name": ingredients_names[index],
        "price": random.randint(1, 10)
    }


def get_random_size(index):
    return {
        "name": sizes_names[index],
        "price": random.randint(1, 10)
    }


def get_random_beverage(index):
    return {
        "name": beverages_names[index],
        "price": random.randint(1, 10)
    }


def get_random_list_names(size_list):
    customers_randoms_name = []
    for _ in range(size_list):
        customers_randoms_name.append(get_random_name())
    return customers_randoms_name


def get_random_list_dni_customers(size_list):
    customers_randoms_dni = []
    for _ in range(size_list):
        customers_randoms_dni.append(get_random_number(min_value_randon_number, max_value_randon_number))
    return customers_randoms_dni


def get_random_list_phone_customers(size_list):
    customers_randoms_phone = []
    for _ in range(size_list):
        customers_randoms_phone.append(get_random_phone_number())
    return customers_randoms_phone


def get_random_list_address_customers(size_list):
    customers_randoms_address = []
    for _ in range(size_list):
        customers_randoms_address.append(get_random_address())
    return customers_randoms_address


def get_random_order(customer_name, customer_dni, customer_phone, customer_address, total_price, size_id):
    return {
        "client_name": customer_name,
        "client_dni": customer_dni,
        "client_phone": customer_phone,
        "client_address": customer_address,
        "date": get_random_date(),
        "total_price": total_price,
        "size_id": size_id
    }


def get_random_order_detail(ingredient_price, order_id, ingredient_id, beverage_price, beverage_id):
    return {
        "ingredient_price": ingredient_price,
        "order_id": order_id,
        "ingredient_id": ingredient_id,
        "beverage_price": beverage_price,
        "beverage_id": beverage_id
    }


def get_random_string() -> str:
    letters = list(string.ascii_lowercase)
    random.shuffle(letters)
    return ''.join(letters[:10])


def get_random_choice(choices: Union[tuple, list]) -> Any:
    return random.choice(choices)


def shuffle_list(choices: list) -> list:
    choice_copy = choices.copy()
    random.shuffle(choice_copy)
    return choice_copy


def get_random_email() -> str:
    return f"{get_random_string()}@{get_random_choice(['hotmail.com', 'gmail.com', 'test.com'])}"


def get_random_sequence(length: int = 10) -> str:
    digits = list(map(str, range(10)))
    sequence = [digits[random.randint(0, 9)] for _ in range(length)]
    return ''.join(sequence)


def get_random_phone() -> str:
    return get_random_sequence(10)
