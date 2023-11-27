# soma_notas = 0
# contador = 0

# while True:
#     nota = float(input("Digite a nota do aluno (ou -1 para encerrar): "))
    
#     if nota == -1:
#         break 
    
#     soma_notas += nota
#     contador += 1

# if contador > 0:
#     media = soma_notas / contador
#     print("A média das notas dos alunos é:", media)
# else:
#     print("Nenhuma nota foi inserida.")
# ========================================================

# qtde = 0
# soma = 0
# n = float(input("Digite a nota do aluno (ou -1 para encerrar): "))
# while (n != -1):
#     soma += n
#     qtde += 1
#     n = float(input(""))
#     media = soma / qtde
#     print("A média das notas dos alunos é:", media)
# ==========================================================
notas = []

while True:
    nota = float(input("Digite a nota do aluno (ou -1 para encerrar): "))
    
    if nota == -1:
        break 
    
    notas.append(nota)

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print("A média das notas dos alunos é:", media)
else:
    print("Nenhuma nota foi inserida.")

print("Lista de notas dos alunos:", notas)

