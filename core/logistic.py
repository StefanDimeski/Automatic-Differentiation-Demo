import math

from core.node import Node

class Logistic(Node):

	def __init__(self, n1):
		super().__init__()

		self.leftNode = n1

		self.leftNode.parents.append(self)

	def perform(self):
		if self.value != None:
			return self.value

		self.value = 1 / (1 + math.exp(-self.leftNode.perform()))
		return self.value

	def derivative(self, wrt):
		if self == wrt:
			return 1

		return self.perform() * (1 - self.perform()) * self.leftNode.derivative(wrt)

	# def derivativeReverse(self, of):
	# 	pass

	def toString(self):
		return "logistic(" + self.leftNode.toString() + ")"