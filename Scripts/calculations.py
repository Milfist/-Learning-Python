from modules.operations import *

a, b, c, d = (10, 5, 0, "Hola")

print("{} + {} = {}".format(a, b, sum_(a, b)))
print("{} - {} = {}".format(b, d, subtraction(b, d)))
print("{} * {} = {}".format(b, b, multiply(b, b)))
print("{} / {} = {}".format(a, c, partition(a, c)))
