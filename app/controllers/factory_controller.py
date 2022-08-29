from .beverage import BeverageController
from .size import SizeController
from .ingredient import IngredientController
from .order import OrderController
from .reports import ReportController

class FactoryController:

    @staticmethod
    def get_controller(controller_type):
        if controller_type == 'size':
            return SizeController
        elif controller_type == 'beverage':
            return BeverageController
        elif controller_type == 'ingredient':
            return IngredientController
        elif controller_type == 'order':
            return OrderController
        elif controller_type == 'report':
            return ReportController
        else:
            return None
