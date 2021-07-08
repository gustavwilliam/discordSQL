from dsql.api.models import Component


class Column(Component):
	def __init__(self, id: str) -> None:
		super().__init__(id)
		self.id = id
		# TODO: Fetch and set column (channel) name
