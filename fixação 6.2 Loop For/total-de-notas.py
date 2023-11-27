n = int( input("Informe a quantidade de notas: "))
soma = 0
for i in range(n):
    nota = float(input("Digite a nota? "))
    soma += nota
    media = soma / n
print(media)