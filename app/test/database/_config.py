import typing


class Config(typing.NamedTuple):

    DB_CONNECTION_STRING: str

    
def load_config():
    str_connection: str = "sqlite:///file:memory?mode=memory&cache=shared&uri=true"
    return Config(
        str_connection
    )
