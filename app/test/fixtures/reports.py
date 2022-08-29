import pytest

from ...common.utils import (get_random_list_dni_customers, get_random_size, get_random_ingredient,
                              get_random_beverage, get_random_list_names, get_random_list_phone_customers,
                              get_random_list_address_customers, get_random_order, get_random_order_detail)

@pytest.fixture
def highest_earning_month_uri():
    return '/highest-earning-month/'


@pytest.fixture
def get_highest_earning_month(client, highest_earning_month_uri) -> dict:
    highest_earning_month = client.get(highest_earning_month_uri)
    return highest_earning_month
