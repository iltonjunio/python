lista=[]
for i in range(10):
    notas = float(input("Digite as notas dos alunos? "))
    lista.append(notas)
print(lista)


for notas in lista:
    if ( notas >= 6):
        print(notas)


for notas in lista:
    notas = notas + 1
    print(notas)
for i in range(len(lista)):
    lista [i] += 10


soma = 0
for notas in lista:
    soma += notas
    media = soma / 10
print (media)
soma = 0
for notas in lista:
    soma += notas
    media = soma / len(lista)
print (media)

media = sum (lista)/ len (lista)
print(media)
