from sqlalchemy.exc import SQLAlchemyError

from ..common.utils import check_required_keys
from ..repositories.managers import ReportManager


class ReportController():


    @classmethod
    def get_max_ingredient_saled(cls):
        try:
            return ReportManager.get_max_ingredient_saled(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)


    @classmethod
    def get_highest_earning_month(cls):
        try:
            return ReportManager.get_highest_earning_month(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)


    @classmethod
    def get_three_best_customers(cls):
        try:
            return ReportManager.get_three_best_customers(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
