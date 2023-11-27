salarios = []

while True:
    salario = float(input("Digite o salário (ou um valor negativo para encerrar): "))
    
    if salario < 0:
        break
    
    salarios.append(salario)

if not salarios:
    print("Nenhum salário foi inserido.")
else:

    media_salarial = sum(salarios) / len(salarios)
    
    menor_salario = min(salarios)
    
    maior_salario = max(salarios)

    percentual_menor_media = (len([salario for salario in salarios if salario < media_salarial]) / len(salarios)) * 100
    
    percentual_maior_media = (len([salario for salario in salarios if salario > media_salarial]) / len(salarios)) * 100
    
    print("a) Média salarial:", media_salarial)
    print("b) Menor salário:", menor_salario)
    print("c) Maior salário:", maior_salario)
    print("d) Percentual de pessoas com salário menor do que a média:", percentual_menor_media, "%")
    print("e) Percentual de pessoas com salário maior do que a média:", percentual_maior_media, "%")
