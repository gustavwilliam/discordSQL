from discordsql.api.models import Component, Snowflake


class Table(Component):
    def __init__(self, id: Snowflake) -> None:
        super().__init__(id)
        self.id = id
        # TODO: Fetch and set table (category) name