"""Crie um programa que dado um valor de renda mensal total, gastos totais com moradia,
gastos totais com transporte e gastos totais com educação, faça um diagnóstico da saúde
financeirado usuário."""

while True:

        #Print que coletaram os dados necessários para as contas
        renda_mensal = float(input("Informe sua renda mensal, por favor: R$"))
        gastos_moradia = float(input("Informe seus gastos com sua moradia, por favor: R$"))
        gastos_educacao = float(input("Informe seus gastos com educação, por favor: R$"))
        gastos_transporte = float(input("Informe seus gastos com transporte, por favor: R$"))

        #Calcula quanto cada parâmetro representa percentualmente na sua renda mensal
        porcentagem_moradia = (gastos_moradia * 100)/renda_mensal
        porcentagem_educacao = (gastos_educacao * 100)/renda_mensal
        porcentagem_transporte = (gastos_transporte * 100)/renda_mensal

        #Calcula a porcentagem ideal: 30% para moradia, 20% para educação e 15% para transporte
        ideal_moradia = (30 * renda_mensal)/100
        ideal_educacao = (20 * renda_mensal)/100
        ideal_transporte = (15 * renda_mensal)/100

        #Comparação para ditar o diagnóstico de gastos mensal
        print("\nO seu diagnóstico de gastos mensal é de:\n")

        #Seguindo o ideal
        if porcentagem_moradia <= 30 and porcentagem_educacao <= 20 and porcentagem_transporte <= 15:
            print("Ótima notícia! Seus gastos estão dentro da margem recomendada.\n")

        #Para moradia
        if porcentagem_moradia > 30:
            print(f"O máximo recomendado é de 30%. Portanto, o máximo ideal de sua renda comprometida com moradia deveria ser de R$ {ideal_moradia}. Seus gastos totais com moradia comprometem {porcentagem_moradia}% de sua renda total.\n")

        if porcentagem_moradia <= 30:
            print(f"Seus gastos totais com moradia comprometem {porcentagem_moradia}% de sua renda mensal total. O máximo recomendado é de 30%. Seus gastos estão dentro da margem recomendada.\n")

        #Para educação
        if porcentagem_educacao > 20:
            print(f"O máximo recomendado é de 20%. Portanto, o máximo ideal de sua renda comprometida com educação deveria ser de R$ {ideal_educacao}. Seus gastos totais com educação comprometem {porcentagem_educacao}% de sua renda total.\n")

        if porcentagem_educacao <= 20:
            print(f"Seus gastos totais com educação comprometem {porcentagem_educacao}% de sua renda mensal total. O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendada.\n")

        #Para transporte
        if ideal_transporte > 15:
            print(f"O máximo recomendado é de 15%. Portanto, o máximo ideal de sua renda comprometida com transporte deveria ser de R$ {ideal_transporte}. Seus gastos totais com transporte comprometem {porcentagem_transporte}% de sua renda total.\n")

        if ideal_transporte <= 15:
            print(f"Seus gastos totais com transporte comprometem {porcentagem_transporte}% de sua renda mensal total. O máximo recomendado é de 15%. Seus gastos estão dentro da margem recomendada.\n")

