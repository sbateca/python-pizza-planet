from ._config import load_config
from sqlalchemy import create_engine, MetaData


class DB():


    config = load_config()


    def __init__(self):
        self.engine = create_engine(self.config.DB_CONNECTION_STRING)
        self.meta_data = MetaData(bind=self.engine)
        MetaData.reflect(self.meta_data)
        self.connection = self.engine.connect()
