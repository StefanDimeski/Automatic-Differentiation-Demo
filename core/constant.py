from core.node import Node

class Constant(Node):

	def __init__(self, val):
		super().__init__()

		self.value = val

	def perform(self):
		return self.value

	def derivative(self, wrt):
		return 0

	def toString(self):
		return str(self.value)