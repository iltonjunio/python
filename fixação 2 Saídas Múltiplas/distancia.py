distancia = float(input("Informe a distancia em km? "))
horario_saida = float(input("Informe o horario de saída? "))
horario_chegada = float(input("Informe o horario de chegada? "))

duracao = horario_chegada - horario_saida

velocidade = distancia / duracao

print("A distancia é: " , velocidade,"km/h")
print("A duração é: ",duracao,"hrs")