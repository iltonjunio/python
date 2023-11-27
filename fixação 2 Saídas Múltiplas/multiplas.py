import math


a = float(input("Informe o valor de a? "))
b = float(input("Informa o valor de b? "))
c = float(input("Informe o  valor de c? "))

delta = (b ** 2) - 4 * a * c

x1 = (- b - math.sqrt(delta)) / (2 * a)
x2 = (- b + math.sqrt(delta)) / (2 * a)

print("valor de x1: ", x1)
print("valor de x2: ", x2)
print("valor de delta: ", delta)