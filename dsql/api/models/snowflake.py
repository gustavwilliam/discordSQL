from datetime import datetime


class Snowflake:
	def __init__(self, id: str) -> None:
		self.id = id

		binary = format(int(id), '064b')
		unix_s = (int(binary[:42], 2) + 1420070400000) / 1000
		self.timestamp = datetime.fromtimestamp(unix_s)

	def __str__(self) -> str:
		return self.id

	def __int__(self) -> int:
		return int(self.id)
