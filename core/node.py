class Node:

	def __init__(self):
		self.value = None
		self.reverseDeriv = None
		self.forwardDeriv = None

		self.leftNode = None
		self.rightNode = None

		self.parents = []

	def perform(self):
		print("Warning: Unintended call of base class perform method")
		return None

	def derivative(self, wrt):
		print("Warning: Unintended call of base class derivative method")
		return None

	# This reverse-mode method makes use of the forward-mode f-on .derivative for simple derivatives
	# so that we don't have to reimplement them again
	def derivativeReverse(self, of):
		if self.reverseDeriv != None:
			return self.reverseDeriv

		self.reverseDeriv = 0
		for parent in self.parents:
			if parent == of:
				self.reverseDeriv = parent.derivative(self)
				break
			else:
				self.reverseDeriv += parent.derivativeReverse(of) * parent.derivative(self)

		return self.reverseDeriv

	def toString(self):
		print("Warning: Unintended call of base class toString method")