uf = str(input("Digite o UF que voce mora? "))
match uf:
    case "ac":
        print("Rio Branco	Acre")
    case "al":
        print("Maceió	Alagoas")
    case "ap":
        print("Macapá	Amapá")
    case "am":
        print("Manaus	Amazonas")
    case "ba":
        print("Salvador	Bahia")
    case "ce":
        print("Fortaleza	Ceará")
    case "df":
        print("Brasília*	Distrito Federal")
    case "es":
        print("Vitória	Espírito Santo")
    case "go":
        print("Goiânia	Goiás")
    case "ma":
        print("São Luís	Maranhão")
    case "mt":
        print("Cuiabá	Mato Grosso")
    case "ms":
        print("Campo Grande	Mato Grosso do Sul")
    case "mg":
        print("Belo Horizonte	Minas Gerais")
    case "pa":
        print("Belém	Pará")
    case "pr":
        print("Curitiba	Paraná")
    case "pb":
        print("João Pessoa	Paraíba")
    case "pe":
        print("Recife	Pernambuco")
    case "pi":
        print("Teresina	Piauí")
    case "rj":
        print("Rio de Janeiro	Rio de Janeiro")
    case "rn":
        print("Natal	Rio Grande do Norte")
    case "rs":
        print("Porto Alegre	Rio Grande do Sul")
    case "ro":
        print("Porto Velho	Rondônia")
    case "rr":
        print("Boa Vista	Roraima")
    case "sc":
        print("Florianópolis	Santa Catarina")
    case "sp":
        print("São Paulo	São Paulo")
    case "se":
        print("Aracaju	Sergipe")
    case "to":
        print("Palmas	Tocantins")
    case _:
        print("Opção invalida")
