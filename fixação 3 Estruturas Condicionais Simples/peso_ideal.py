sexo = str(input("Informe o sexo f ou m: ").upper())
altura =  float(input("Informe a altura? "))

m = (72.7 * (altura)) - 58
f = (62.1 * (altura)) - 44.7

if (sexo == "M"):
    print("peso ideal é: ", + round(m,2))

elif(sexo == "F"):
    print("peso idela é:", + round(f,2))

else:
    print("sexo invalido")