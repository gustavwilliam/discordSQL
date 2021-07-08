from dsql.api.models import Component


class Database(Component):
	def __init__(self, id: str) -> None:
		super().__init__(id)
		# TODO: Fetch and set database (server) name
