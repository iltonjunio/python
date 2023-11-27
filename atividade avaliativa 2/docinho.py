total_docinhos = 200

while total_docinhos > 0:
    quantidade_desejada = int(input("Quantos docinhos você deseja pegar? "))
    if quantidade_desejada > total_docinhos:
        print("Desculpe, não há docinhos suficientes. Você pode pegar no máximo", total_docinhos)
        break  
    total_docinhos -= quantidade_desejada
    print("Você pegou", quantidade_desejada, "docinhos. Restam", total_docinhos, "docinhos.")

print("Todos os docinhos foram distribuídos.")
