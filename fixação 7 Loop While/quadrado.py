# while True:
#     numero = float(input("Digite um número (ou -1 para sair): "))
    
#     if numero == -1:
#         break
    
#     quadrado = numero ** 2
#     print("O quadrado de", numero, "é", quadrado)

    # ==============================================

# num = 0
# while(num != -1):
#     num = int(input("Digite o numero "))
#     print(num**2)
# ===================================
quadrados = []

while True:
    numero = float(input("Digite um número (ou -1 para sair): "))
    
    if numero == -1:
        break
    
    quadrado = numero ** 2
    quadrados.append(quadrado)

print("Quadrados dos números digitados:")
print(quadrados)

