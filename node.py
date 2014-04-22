class Node:
	def __init__(self, state, cameFrom, steps):
		self.state = state
		self.cameFrom = cameFrom
		self.steps = steps

	def __lt__(self, other):
		return self.score < other.score