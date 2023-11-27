idade = int(input("Digite sua idade"))
if(idade >= 6 and idade <= 11):
    print("infantil", idade)
elif(idade >= 12 and idade <= 17):
    print("juvenil", idade)

elif(idade >= 18 and idade <= 45):
    print("adulto", idade)
else:
    print("erro idade não conrresponde")