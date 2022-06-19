"""Desenvolva um programa contendo uma função que liste, por país, a estimativa de variação do
PIB, em percentual, entre 2013 e 2020. """

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

def solicitar_PIB(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15):
    rotulos, dados = extracao_dados('Planilha.csv')
    ano_2013 = rotulos.index('2013')
    ano_2020 = rotulos.index('2020')
    indice_pais = rotulos.index('País')

    for elemento in dados:

        #PAÍS: EUA
        if elemento[indice_pais] == x1:
            ano_max = float(elemento[ano_2020])
            ano_min = float(elemento[ano_2013])
            PIB = round((ano_max/ano_min)*100) - 100
            print(f"A variação do PIB nos EUA é {PIB}%, entre os anos de 2013 e 2020.")

        # PAÍS: China
        if elemento[indice_pais] == x2:
            ano_max = float(elemento[ano_2020])
            ano_min = float(elemento[ano_2013])
            PIB = round((ano_max/ano_min)*100) - 100
            print(f"A variação do PIB na China é {PIB}%, entre os anos de 2013 e 2020.")

        # PAÍS: Japão
        if elemento[indice_pais] == x3:
            ano_max = float(elemento[ano_2020])
            ano_min = float(elemento[ano_2013])
            PIB = round((ano_max/ano_min)*100) - 100
            print(f"A variação do PIB no Japão é {PIB}%, entre os anos de 2013 e 2020.")

        # PAÍS: Alemanha
        if elemento[indice_pais] == x4:
            ano_max = float(elemento[ano_2020])
            ano_min = float(elemento[ano_2013])
            PIB = round((ano_max/ano_min)*100) - 100
            print(f"A variação do PIB na Alemanha é {PIB}%, entre os anos de 2013 e 2020.")

        # PAÍS: Reino Unido
        if elemento[indice_pais] == x5:
            ano_max = float(elemento[ano_2020])
            ano_min = float(elemento[ano_2013])
            PIB = round((ano_max/ano_min)*100) - 100
            print(f"A variação do PIB no Reino Unido é {PIB}%, entre os anos de 2013 e 2020.")

        # PAÍS: França
        if elemento[indice_pais] == x6:
            ano_max = float(elemento[ano_2020])
            ano_min = float(elemento[ano_2013])
            PIB = round((ano_max/ano_min)*100) - 100
            print(f"A variação do PIB na França é {PIB}%, entre os anos de 2013 e 2020.")

        # PAÍS: Brasil
        if elemento[indice_pais] == x7:
            ano_max = float(elemento[ano_2020])
            ano_min = float(elemento[ano_2013])
            PIB = round((ano_max/ano_min)*100) - 100
            print(f"A variação do PIB no Brasil é {PIB}%, entre os anos de 2013 e 2020.")

        # PAÍS: Itália
        if elemento[indice_pais] == x8:
            ano_max = float(elemento[ano_2020])
            ano_min = float(elemento[ano_2013])
            PIB = round((ano_max/ano_min)*100) - 100
            print(f"A variação do PIB na Itália é {PIB}%, entre os anos de 2013 e 2020.")

        # PAÍS: Índia
        if elemento[indice_pais] == x9:
            ano_max = float(elemento[ano_2020])
            ano_min = float(elemento[ano_2013])
            PIB = round((ano_max/ano_min)*100) - 100
            print(f"A variação do PIB na Índia é {PIB}%, entre os anos de 2013 e 2020.")

        # PAÍS: Rússia
        if elemento[indice_pais] == x10:
            ano_max = float(elemento[ano_2020])
            ano_min = float(elemento[ano_2013])
            PIB = round((ano_max / ano_min) * 100) - 100
            print(f"A variação do PIB na Rússia é {PIB}%, entre os anos de 2013 e 2020.")

        # PAÍS: Canadá
        if elemento[indice_pais] == x11:
            ano_max = float(elemento[ano_2020])
            ano_min = float(elemento[ano_2013])
            PIB = round((ano_max/ano_min)*100) - 100
            print(f"A variação do PIB no Canadá é {PIB}%, entre os anos de 2013 e 2020.")

        # PAÍS: Coreia do Sul
        if elemento[indice_pais] == x12:
            ano_max = float(elemento[ano_2020])
            ano_min = float(elemento[ano_2013])
            PIB = round((ano_max/ano_min)*100) - 100
            print(f"A variação do PIB na Coreia do Sul é {PIB}%, entre os anos de 2013 e 2020.")

        # PAÍS: Espanha
        if elemento[indice_pais] == x13:
            ano_max = float(elemento[ano_2020])
            ano_min = float(elemento[ano_2013])
            PIB = round((ano_max/ano_min)*100) - 100
            print(f"A variação do PIB na Espanha é {PIB}%, entre os anos de 2013 e 2020.")

        # PAÍS: México
        if elemento[indice_pais] == x14:
            ano_max = float(elemento[ano_2020])
            ano_min = float(elemento[ano_2013])
            PIB = round((ano_max/ano_min)*100) - 100
            print(f"A variação do PIB no México é {PIB}%, entre os anos de 2013 e 2020.")

        # PAÍS: Indonésia
        if elemento[indice_pais] == x15:
            ano_max = float(elemento[ano_2020])
            ano_min = float(elemento[ano_2013])
            PIB = round((ano_max/ano_min)*100) - 100
            print(f"A variação do PIB na Indonésia é {PIB}%, entre os anos de 2013 e 2020.")

solicitar_PIB('EUA','China','Japão','Alemanha','Reino Unido','França','Brasil','Itália','Índia','Rússia','Canadá','Coreia do Sul','Espanha','México','Indonésia')
