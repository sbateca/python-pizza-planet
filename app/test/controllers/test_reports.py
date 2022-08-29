import pytest

from app.controllers import order
from ..database import _db
from populate_db import *
from app.controllers.reports import ReportController

def test_get_valid_data_report_most_saled_ingredient(app):
    response = ReportController.get_max_ingredient_saled()
    data_response = response[0]
    for key in data_response:
        assert(key is not None)
    