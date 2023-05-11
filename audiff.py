from core import *

# The gist of AD is that it uses the chain rule to decompose complex derivatives
# into very elementary ones that we know. 

# derivative method uses forward-mode automatic differentiation, while
# derivativeReverse uses reverse-mode automatic differentiation

# For even more benefit of reverse-mode and generally for a better optimization
# I should cache performed operations so I can reuse them, instead of recomputing them
# every time

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