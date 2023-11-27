regiao = str(input("Digite a região que voce mora? "))
match regiao:
    case "nordeste":
        print("Maceió	Alagoas	AL	Nordeste, Salvador	Bahia	BA	Nordeste, Fortaleza	Ceará	CE	Nordeste, São Luís	Maranhão	MA	Nordeste, João Pessoa	Paraíba	PB	Nordeste, Recife	Pernambuco	PE	Nordeste, Teresina	Piauí	PI	Nordeste, Natal	Rio Grande do Norte	RN	Nordeste, Aracaju	Sergipe	SE	Nordeste ")
    case "sudeste":
        print("São Paulo	São Paulo	SP	Sudeste, Rio de Janeiro	Rio de Janeiro	RJ	Sudeste,Belo Horizonte	Minas Gerais	MG	Sudeste, Vitória	Espírito Santo	ES	Sudeste ")
    case "centro-oeste":
        print("Brasília*	Distrito Federal	DF	Centro-Oeste, Goiânia	Goiás	GO	Centro-Oeste, Cuiabá	Mato Grosso	MT	Centro-Oeste, Campo Grande	Mato Grosso do Sul	MS	Centro-Oeste, ")
    case "sul":
        print("Florianópolis	Santa Catarina	SC	Sul, Porto Alegre	Rio Grande do Sul	RS	Sul, Curitiba	Paraná	PR	Sul ")
    case "norte":
        print("Rio Branco	Acre	AC	Norte , Macapá	Amapá	AP	Norte, Manaus	Amazonas	AM	Norte, Belém	Pará	PA	Norte, Porto Velho	Rondônia	RO	Norte, Boa Vista	Roraima	RR	Norte, Palmas	Tocantins	TO	Norte ")
    case _:
        print("Opção invalida")