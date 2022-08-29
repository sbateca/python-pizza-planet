from ..database import _db

import pytest


@pytest.fixture
def database_mock():
    return _db.DB()