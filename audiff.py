import math

# The gist of AD is that it uses the chain rule to decompose complex derivatives
# into very elementary ones that we know. 

# derivative method uses forward-mode automatic differentiation, while
# derivativeReverse uses reverse-mode automatic differentiation

# For even more benefit of reverse-mode and generally for a better optimization
# I should cache performed operations so I can reuse them, instead of recomputing them
# every time

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


class Addition(Node):

	def __init__(self, n1, n2):
		super().__init__()

		self.leftNode = n1
		self.rightNode = n2

		self.leftNode.parents.append(self)
		self.rightNode.parents.append(self)

	def perform(self):
		if self.value != None:
			return self.value

		self.value = self.leftNode.perform() + self.rightNode.perform()
		return self.value

	def derivative(self, wrt):
		if self == wrt:
			return 1

		return self.leftNode.derivative(wrt) + self.rightNode.derivative(wrt)

	def toString(self):
		return "(" + self.leftNode.toString() + " + " + self.rightNode.toString() + ")"

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


v1, v2 = Variable(1), Variable(1)

# Forward mode
root = Addition(Logistic(Multiplication(Constant(3), v1)), Logistic(Addition(v1, v2)))

print("Forward-mode: ")
print("F = ", root.toString())
print("F = ", root.perform())
print("dF/dv1 = ", root.derivative(v1))
print("dF/dv2 = ", root.derivative(v2))

print("")

# Reverse mode
root = Addition(Logistic(Multiplication(Constant(3), v1)), Logistic(Addition(v1, v2)))

print("Reverse-mode: ")
print("F = ", root.toString())
print("F = ", root.perform())

# Even though I still need to call the deriv method twice (once for each variable), the second
# call is very cheap because most of what's needed for it is already calculated and cached

# Once I have called derivativeReverse(x), if i want to calculate derivativeReverse(y) i would
# have to reset the entire tree. Also the same thing with changing values of variables.
print("dF/dv1 = ", v1.derivativeReverse(root))
print("dF/dv2 = ", v2.derivativeReverse(root))