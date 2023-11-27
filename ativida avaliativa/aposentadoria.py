
nome = input("Digite o nome do empregado: ")
ano_nascimento = int(input("Digite o ano de nascimento do empregado: "))
ano_inicio_trabalho = int(input("Digite o ano de início de sua jornada de trabalho: "))

idade = 2023 - ano_nascimento
tempo_de_trabalho = 2023 - ano_inicio_trabalho

if (idade >= 65) or (tempo_de_trabalho >= 30) or (idade >= 60 and tempo_de_trabalho >= 25):
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Tempo de trabalho: {tempo_de_trabalho} anos")
    print("Pode requerer aposentadoria.")
else:
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Tempo de trabalho: {tempo_de_trabalho} anos")
    print("Não pode requerer aposentadoria.")
