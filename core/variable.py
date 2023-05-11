from core.node import Node

class Variable(Node):

	varNum = 0

	def __init__(self, val, name=""):
		super().__init__()

		self.name = name

		if self.name == "":
			Variable.varNum += 1
			self.name = "v" + str(Variable.varNum)

		self.value = val

	def perform(self):
		return self.value

	def derivative(self, wrt):
		if self == wrt:
			return 1
		else:
			return 0

	# def derivativeReverse(self, of):
	# 	for parent in self.parents:
	# 		self.reverseDeriv += parent.derivativeReverse(of) * parent.derivative(self)

	# 	return self.reverseDeriv

	def toString(self):
		return self.name