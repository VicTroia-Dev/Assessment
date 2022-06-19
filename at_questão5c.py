"""Desenvolva uma função que, para um país, exiba o gráfico da evolução do PIB ao longo dos anos."""

# Importação que possibilita a criação de gráficos
import matplotlib.pyplot as plt

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

def exibir_grafico_PIB(pais):
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
  anos = [2013,2014,2015,2016,2017,2018,2019,2020]
  PIB = []

  for elemento in dados:
      if elemento[indice_pais] == pais:
          PIB.append(elemento[ano_2013])
          PIB.append(elemento[ano_2014])
          PIB.append(elemento[ano_2015])
          PIB.append(elemento[ano_2016])
          PIB.append(elemento[ano_2017])
          PIB.append(elemento[ano_2018])
          PIB.append(elemento[ano_2019])
          PIB.append(elemento[ano_2020])
  exibir_grafico(anos,PIB)

def exibir_grafico(x,y):
  plt.plot(x,y)
  plt.show()

#Capta um país para apresentar o gráfico do comportamento do PIB respectivo
país = str(input("Digite um país, para visualizar o seu gráfico do PIB:"))
exibir_grafico_PIB(país)
