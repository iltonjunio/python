# Solicita ao usuário os valores dos lados do triângulo
A = float(input("Digite o valor do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do lado C: "))

if A == B and B == C:
    tipo = "equilátero"
elif A == B or B == C or A == C:
    tipo = "isósceles"
else:
    tipo = "escaleno"

print(f"O triângulo com lados A={A}, B={B} e C={C} é um triângulo {tipo}.")

# --------------------------------------------------
# A = float(input("Digite o valor do lado A: "))
# B = float(input("Digite o valor do lado B: "))
# C = float(input("Digite o valor do lado C: "))

# if A == B and B == C:
#     print("equilátero")
# elif A == B or B == C or A == C:
#     print ("isósceles")
# else:
#     print("escaleno")