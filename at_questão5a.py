"""Desenvolva um programa contendo uma função que permita ao usuário solicitar o PIB de um país para um determinado ano."""

# Extrai os dados da Planilh em CSV disponibilizado
def extracao_dados(caminho_base):
    base = open(caminho_base, 'r', encoding='utf8')

    conteudo = base.read()

    base.close()
    conteudo = conteudo.splitlines()
    rotulos = conteudo[0]
    rotulos = rotulos.split(',')
    conteudo = conteudo[1:]
    dados = []
    for elemento in conteudo:
        elemento = elemento.split(',')
        dados.append(elemento)
    return rotulos, dados


def solicitar_PIB(ano, país):
    rotulos, dados = extracao_dados('Planilha.csv')
    ano_2013 = rotulos.index('2013')
    ano_2014 = rotulos.index('2014')
    ano_2015 = rotulos.index('2015')
    ano_2016 = rotulos.index('2016')
    ano_2017 = rotulos.index('2017')
    ano_2018 = rotulos.index('2018')
    ano_2019 = rotulos.index('2019')
    ano_2020 = rotulos.index('2020')
    indice_pais = rotulos.index('País')

    for elemento in dados:
        #ANO: 2020
        if elemento[indice_pais] == país and ano == 2020:
            print(elemento[ano_2020])

        #ANO: 2019
        elif elemento[indice_pais] == país and ano == 2019:
            print(elemento[ano_2019])

        # ANO: 2018
        elif elemento[indice_pais] == país and ano == 2018:
            print(elemento[ano_2018])

        # ANO: 2017
        elif elemento[indice_pais] == país and ano == 2017:
            print(elemento[ano_2017])

        # ANO: 2016
        elif elemento[indice_pais] == país and ano == 2016:
            print(elemento[ano_2016])

        # ANO: 2015
        elif elemento[indice_pais] == país and ano == 2015:
            print(elemento[ano_2015])

        # ANO: 2014
        elif elemento[indice_pais] == país and ano == 2014:
            print(elemento[ano_2014])

        # ANO: 2013
        elif elemento[indice_pais] == país and ano == 2013:
            print(elemento[ano_2013])


# Capta o ano para avaliação do PIB
ano = int(input("Digite um ano entre 2013 e 2020: "))

# Avalia se o ano dado está dentro do período presente na base
if ano < 2013 or ano > 2020:
    print("Ano inválido")
    exit()

# Capta o país para avaliaçaõ do PIB
país = str(input("Digite um país:"))

# Avalia se o país dado está dentro do período presente na base
if país != 'EUA'or'China'or'Japão'or'Alemanha'or'Reino Unido'or'França'or'Brasil'or'Itália'or'Índia'or'Rússia'or'Canadá'or'Coreia do Sul'or'Espanha'or'México'or'Indonésia':
    print("País inválido")
solicitar_PIB(ano, país)
