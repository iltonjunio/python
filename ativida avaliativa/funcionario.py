nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário atual do funcionário: "))
nivel_senioridade = input("Digite o nível de senioridade (Estagiário, Júnior, Pleno ou Sênior): ")

taxa_reajuste = 0.0

if nivel_senioridade.lower() == "estagiário":
    taxa_reajuste = 0.05
elif nivel_senioridade.lower() == "júnior":
    taxa_reajuste = 0.075
elif nivel_senioridade.lower() == "pleno":
    taxa_reajuste = 0.10
elif nivel_senioridade.lower() == "sênior":
    taxa_reajuste = 0.125
else:
    print("Nível de senioridade inválido.")
    exit()

novo_salario = salario * (1 + taxa_reajuste)

print(f"O novo salário de {nome} após o reajuste é: R${novo_salario:.2f}")
