import pandas as pd

df_csv = pd.read_csv('steam_reviews.csv')

games = {}

#obter quantidade de reviews por jogo
"""
for i in df_csv.iterrows():
    if i[1].to_list()[-1] not in games:
        games[i[1].to_list()[-1]] = 1
    else:
        games[i[1].to_list()[-1]] = (games[i[1].to_list()[-1]]+1)
"""

#visualizar jogos e quantidades de reviews em ordem de inserção no dicionário
"""
for i in games:
    print(str(i) + " --- " + str(games[i]))
"""

#visualizar jogos e quantidades de reviews em ordem decrescente para crescente
"""
for item in sorted(games, key = games.get):
    print(item + " - " + str(games[item]))
"""

#obter quantidades de recomendações positivas e negativas por jogo
"""
for i in df_csv.iterrows():
    if i[1].to_list()[-1] not in games:
        games[i[1].to_list()[-1]] = [0, 0]

        if i[1].to_list()[-3] == "Recommended":
            games[i[1].to_list()[-1]][0] += 1

        elif i[1].to_list()[-3] == "Not Recommended":
            games[i[1].to_list()[-1]][1] += 1

    else:
        if i[1].to_list()[-3] == "Recommended":
            games[i[1].to_list()[-1]][0] += 1

        elif i[1].to_list()[-3] == "Not Recommended":
            games[i[1].to_list()[-1]][1] += 1
"""

#obtendo quantidades de horas jogadas por jogo
"""
for i in df_csv.iterrows():
    if i[1].to_list()[-1] not in games:
        games[i[1].to_list()[-1]] = i[1].to_list()[3]
    else:
        games[i[1].to_list()[-1]] += i[1].to_list()[3]
