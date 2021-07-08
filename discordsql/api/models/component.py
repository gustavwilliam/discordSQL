from discordsql.api.models import Snowflake


class Component:
    """
    Base class for components used in the database, such as Database, Table and Column.
    """
    def __init__(self, id: Snowflake) -> None:
        self.id = id
        # TODO: Set created date (from snowflake)
        