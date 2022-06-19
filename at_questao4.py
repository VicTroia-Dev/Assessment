"""Desenvolva um programa que calcula os juros composto de um percentual de rendimento
mensalmente, e apresenta o valor de aporte para cada período. Além de exibir um
gráfico da evolução do valor acumulado."""

# Realiza o calculo dos juros:
def juros_compostos(valor_entrada,percentual_rendimento,aporte,periodos,eixo_x,eixo_y):
    for a in range(1, periodos+1):
        novo_valor = round((valor_entrada + (percentual_rendimento * valor_entrada)/100) + aporte)
        valor_entrada = novo_valor
        eixo_x.append(novo_valor)
        eixo_y.append(a)
        print(f"\nApós {a} períodos, o montante será de R${round(novo_valor)}.")

# Cria o gráfico que aprenseta o rendimento:
import matplotlib.pyplot as plt
from questao4 import juros_compostos
def grafico(eixo_x,eixo_y):
    x = eixo_x
    y = eixo_y

    plt.plot(x,y)
    plt.show()
    exit()

# Programa que recebe os valores para o cálculo e geração do gráfico:
valor_entrada = float(input("Informe o valor de entrada, por favor: R$ "))
percentual_rendimento = float(input("Informe o percentual do seu rendimento (%): "))
aporte = float(input("Informe o aporte de cada período, por favor: R$ "))
periodos = int(input("Informe o total de períodos que você deseja verificar, por favor: "))

eixo_x = []
eixo_y = []
juros_compostos(valor_entrada,percentual_rendimento,aporte,periodos,eixo_x,eixo_y)
grafico(eixo_x,eixo_y)
