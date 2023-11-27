# total = 0

# while True:
#     preco = float(input("Digite o preço do produto (ou -1 para encerrar): "))
    
#     if preco == -1:
#         break 
    
#     total += preco

# print("O valor final da soma dos preços é:", total)

# ===========================================

# soma = 0
# preco =  float(input("Digite o preço do produto (ou -1 para encerrar): "))
# while (preco != -1):
#     soma +=preco
#     preco = float(input("Digite o preço do produto (ou -1 para encerrar): "))
# print(soma)
# =========================================
precos = []

while True:
    preco = float(input("Digite o preço do produto (ou -1 para encerrar): "))
    
    if preco == -1:
        break 
    
    precos.append(preco)

total = sum(precos)

print("Lista de preços inseridos:", precos)
print("O valor final da soma dos preços é:", total)

