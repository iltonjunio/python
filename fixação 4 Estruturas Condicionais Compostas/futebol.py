time1 = input("Digite o nome do primeiro time: ")
gols_time1 = int(input(f"Quantos gols o {time1} marcou? "))

time2 = input("Digite o nome do segundo time: ")
gols_time2 = int(input(f"Quantos gols o {time2} marcou? "))

if gols_time1 > gols_time2:
    vencedor = time1

elif gols_time2 > gols_time1:
    vencedor = time2

else:
    vencedor = "EMPATE"

if vencedor == "EMPATE":
    print("A partida terminou em empate!")

else:
    print(f"O time vencedor é o {vencedor}!")
