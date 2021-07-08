from dsql.api.models import Snowflake


class Component:
	"""
    Base class for components used in the database, such as Database, Table and Column.
    """
	def __init__(self, id: str) -> None:
		self.id = Snowflake(id)
		self.created_at = self.id.timestamp
