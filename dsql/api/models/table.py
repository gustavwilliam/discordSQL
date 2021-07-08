from dsql.api.models import Component


class Table(Component):
	def __init__(self, id: str) -> None:
		super().__init__(id)
		# TODO: Fetch and set table (category) name
