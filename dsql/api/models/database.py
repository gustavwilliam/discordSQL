from dsql.api.models import Component, Snowflake


class Database(Component):
    def __init__(self, id: Snowflake) -> None:
        super().__init__(id)
        self.id = id
        # TODO: Fetch and set database (server) name
