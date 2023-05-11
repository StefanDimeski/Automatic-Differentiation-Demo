from core.node import Node

class Multiplication(Node):

	def __init__(self, n1, n2):
		super().__init__()
		self.leftNode = n1
		self.rightNode = n2

		self.leftNode.parents.append(self)
		self.rightNode.parents.append(self)

	def perform(self):
		if self.value != None:
			return self.value

		self.value = self.leftNode.perform() * self.rightNode.perform()
		return self.value

	def derivative(self, wrt):
		if self == wrt:
			return 1

		return self.leftNode.perform() * self.rightNode.derivative(wrt) + self.leftNode.derivative(wrt) * self.rightNode.perform()

	def toString(self):
		return self.leftNode.toString() + " * " + self.rightNode.toString()